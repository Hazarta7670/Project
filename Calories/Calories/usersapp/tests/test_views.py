from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Calories.contentapp.models import Meals, Drinks, Activities
from Calories.usersapp.models import Profile

TheUser = get_user_model()


class TestHomePage(TestCase):
    def test_correct_template(self):
        response = self.client.get(reverse('home page'))
        self.assertTemplateUsed(response, 'home_page.html')


class TestProfileView(TestCase):
    test_user = {
        'username': 'testuser',
        'password': '123456'
    }
    test_profile = {
        'first_name': 'hristo',
        'last_name': 'stoyanov',
        'email': 'hss1993@abv.bg',
        'age': 28,
        'weight': 85,
        'height': 182,
        'activity_level': 'Moderately loaded Exercises Two-Three times a Week',
        'sex': 'Male',
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('create profile'))
        self.assertTemplateUsed('create_profile.html')

    def test_correct_form(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        self.assertEqual('hristo', profile.first_name)
        self.assertEqual('stoyanov', profile.last_name)
        self.assertEqual('hss1993@abv.bg', profile.email)
        self.assertEqual(28, profile.age)
        self.assertEqual(182, profile.height)
        self.assertEqual(85, profile.weight)
        self.assertEqual('Moderately loaded Exercises Two-Three times a Week', profile.activity_level)
        self.assertEqual('Male', profile.sex)

    def test_same_user_for_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        self.assertEqual(user.pk, profile.user.pk)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        response = self.client.post(reverse('create profile'), {**self.test_profile,
                                                                'user': user})
        user.refresh_from_db()
        self.assertRedirects(response, reverse('profile details', kwargs={'pk': user.pk}))


class TestRegistrateUser(TestCase):
    test_user = {
        'username': 'testuser',
        'password': '123456'
    }

    def test_correct_template(self):
        response = self.client.get(reverse('registrate user'))
        self.assertTemplateUsed(response, 'create_user.html')

    def test_correct_username(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.assertEqual('testuser', user.username)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        response = self.client.post(reverse('registrate user'), {'username': 'testuser1',
                                                                 'password1': 1234567,
                                                                 'password2': 1234567}
                                    )
        user.refresh_from_db()
        self.assertRedirects(response, reverse('login page'))


class TestLogin(TestCase):
    test_user = {
        'username': 'testuser',
        'password': '123456'
    }
    test_profile = {
        'first_name': 'hristo',
        'last_name': 'stoyanov',
        'email': 'hss1993@abv.bg',
        'age': 28,
        'weight': 85,
        'height': 182,
        'activity_level': 'Moderately loaded Exercises Two-Three times a Week',
        'sex': 'Male',
    }

    def test_correct_template(self):
        self.client.login(**self.test_user)
        response = self.client.get(reverse('login page'))
        self.assertTemplateUsed(response, 'login_page.html')

    def test_success_url_with_no_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        response = self.client.post(reverse('login page'), {'username': 'testuser',
                                                            'password': '123456'})
        user.refresh_from_db()
        self.assertRedirects(response, reverse('create profile'))

    def test_success_url_with_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        self.client.login(**self.test_user)
        response = self.client.post(reverse('login page'), {'username': 'testuser',
                                                            'password': '123456'})
        user.refresh_from_db()
        self.assertRedirects(response, reverse('profile details', kwargs={'pk': profile.pk}))


class TestUpdateProfile(TestCase):
    test_user = {
        'username': 'testuser',
        'password': '123456'
    }
    test_profile = {
        'first_name': 'hristo',
        'last_name': 'stoyanov',
        'email': 'hss1993@abv.bg',
        'age': 28,
        'weight': 85,
        'height': 182,
        'activity_level': 'Moderately loaded Exercises Two-Three times a Week',
        'sex': 'Male',
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('edit profile', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('edit_profile.html')

    def test_with_changed_profile_info(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('edit profile', kwargs={'pk': profile.pk}),
                                    {'first_name': 'stanimir',
                                     'last_name': 'ivanov',
                                     'email': 'stanimir@abv.bg',
                                     'age': 55,
                                     'weight': 105,
                                     'height': 180,
                                     'activity_level': 'Moderately loaded Exercises Two-Three times a Week',
                                     'sex': 'Male',
                                     'user': user}
                                    )
        profile.refresh_from_db()
        self.assertEqual(profile.first_name, 'stanimir')
        self.assertEqual(profile.last_name, 'ivanov')
        self.assertEqual(profile.email, 'stanimir@abv.bg')
        self.assertEqual(profile.age, 55)
        self.assertEqual(profile.weight, 105)
        self.assertEqual(profile.height, 180)
        self.assertEqual(profile.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('edit profile', kwargs={'pk': profile.pk}),
                                    {'first_name': 'stanimir',
                                     'last_name': 'ivanov',
                                     'email': 'stanimir@abv.bg',
                                     'age': 55,
                                     'weight': 105,
                                     'height': 180,
                                     'activity_level': 'Moderately loaded Exercises Two-Three times a Week',
                                     'sex': 'Male',
                                     'user': user}
                                    )
        profile.refresh_from_db()
        self.assertRedirects(response, reverse('profile details', kwargs={'pk': profile.pk}))


class TestDeleteProfileView(TestCase):
    test_user = {
        'username': 'testuser',
        'password': '123456'
    }
    test_profile = {
        'first_name': 'hristo',
        'last_name': 'stoyanov',
        'email': 'hss1993@abv.bg',
        'age': 28,
        'weight': 85,
        'height': 182,
        'activity_level': 'Moderately loaded Exercises Two-Three times a Week',
        'sex': 'Male',
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('delete account', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('delete_account.html')

    def test_for_deleting_user_and_profile_at_the_same_time(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('delete account', kwargs={'pk': profile.pk}))
        try:
            profile.refresh_from_db()
            user.refresh_from_db()
        except:
            self.assert_(True)

    def test_redirect_to_home_after_deleting_user_and_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('delete account', kwargs={'pk': profile.pk}))
        self.assertRedirects(response, reverse('home page'))


class TestProfileDetailsView(TestCase):
    test_user = {
        'username': 'testuser',
        'password': '123456'
    }
    male_test_profile = {
        'first_name': 'hristo',
        'last_name': 'stoyanov',
        'email': 'hss1993@abv.bg',
        'age': 28,
        'weight': 85,
        'height': 182,
        'activity_level': 'Little or No Training',
        'sex': 'Male',
    }
    female_test_profile = {
        'first_name': 'ralica',
        'last_name': 'stoyanova',
        'email': 'ralica@abv.bg',
        'age': 23,
        'weight': 52,
        'height': 166,
        'activity_level': 'Little or No Training',
        'sex': 'Female'
    }
    one_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }
    one_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }
    one_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 300,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.male_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('profile_details.html')

    def test_with_male_test_profile_for_basal_metabolism(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.male_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['basal_metabolism'], 2223)

    def test_with_female_test_profile_for_basal_metabolism(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.female_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['basal_metabolism'], 1537.8)

    def test_with_male_test_profile_for_bmi(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.male_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['bmi'], 25.661152034778407)

    def test_with_female_test_profile_for_bmi(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.female_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['bmi'], 18.870663376397157)

    def test_with_male_test_profile_for_string_equality_of_bmi(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.male_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['normal'], 'Overweight')

    def test_with_female_test_profile_for_string_equality_of_bmi(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.female_test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['normal'], 'Healthy Weight')

    def test_for_correct_summary_of_daily_calories(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.female_test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.one_meal,
                                    user=user,
                                    )
        drink = Drinks.objects.create(**self.one_drink,
                                      user=user,
                                      )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['daily_cal'], 2100)

    def test_for_correct_summary_of_burned_calories(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.female_test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.one_activity,
                                             user=user,
                                             )
        response = self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))
        self.assertEqual(response.context['burned'], 300)
