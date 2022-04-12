from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Calories.contentapp.models import Meals, Drinks, Activities
from Calories.usersapp.models import Profile

TheUser = get_user_model()


class TestMealView(TestCase):

    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('add meal'))
        self.assertTemplateUsed('add_meal.html')

    def test_creating_meal(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        self.assertEqual(meal.meal, self.test_meal['meal'])
        self.assertEqual(meal.weight, self.test_meal['weight'])
        self.assertEqual(meal.calories, self.test_meal['calories'])
        self.assertEqual(meal.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('add meal'), {**self.test_meal,
                                                          'user': user})
        user.refresh_from_db()
        self.assertRedirects(response, reverse('meals details'))


class TestDrinkView(TestCase):

    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('add drink'))
        self.assertTemplateUsed('add_drink.html')

    def test_creating_drink(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user)
        self.assertEqual(drink.drink, self.test_drink['drink'])
        self.assertEqual(drink.weight, self.test_drink['weight'])
        self.assertEqual(drink.calories, self.test_drink['calories'])
        self.assertEqual(drink.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('add drink'), {**self.test_drink,
                                                           'user': user})
        user.refresh_from_db()
        self.assertRedirects(response, reverse('drinks details'))


class TestActivityView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 300,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('add activity'))
        self.assertTemplateUsed('add_activity.html')

    def test_creating_activity(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user)
        self.assertEqual(activity.activity, self.test_activity['activity'])
        self.assertEqual(activity.time, self.test_activity['time'])
        self.assertEqual(activity.calories, self.test_activity['calories'])
        self.assertEqual(activity.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.post(reverse('add activity'), {**self.test_activity,
                                                              'user': user})
        user.refresh_from_db()
        self.assertRedirects(response, reverse('activities details'))


class TestMealsDetailsView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
    test_user2 = {'username': 'testuser2',
                  'password': '1234567'}
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
    test_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }
    test_meal2 = {
        'meal': 'beef',
        'weight': 300,
        'calories': 1500,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('meals details'))
        self.assertTemplateUsed('meals_details.html')

    def test_correctly_taking_meals_by_user(self):
        user = TheUser.objects.create_user(**self.test_user)
        user2 = TheUser.objects.create_user(**self.test_user2)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user,
                                    )
        meal2 = Meals.objects.create(**self.test_meal2,
                                     user=user2,
                                     )
        response = self.client.get(reverse('meals details'))
        self.assertEqual(len(response.context['all_user_meals']), 1)

    def test_correct_user_pk(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('meals details'))
        self.assertEqual(response.context['user_pk'], user.pk)

    def test_taking_meals_by_user_and_date(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user,
                                    )
        meal2 = Meals.objects.create(**self.test_meal2,
                                     user=user,
                                     )
        response = self.client.get(reverse('meals details'))
        self.assertEqual(len(response.context['user_meals']), 2)


class TestDrinksDetailsView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
    test_user2 = {'username': 'testuser2',
                  'password': '1234567'}
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
    test_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }
    test_drink2 = {
        'drink': 'vodka',
        'weight': 100,
        'calories': 600,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('drinks details'))
        self.assertTemplateUsed('drinks_details.html')

    def test_correctly_taking_drinks_by_user(self):
        user = TheUser.objects.create_user(**self.test_user)
        user2 = TheUser.objects.create_user(**self.test_user2)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user,
                                      )
        drink2 = Drinks.objects.create(**self.test_drink2,
                                       user=user2,
                                       )
        response = self.client.get(reverse('drinks details'))
        self.assertEqual(len(response.context['all_user_drinks']), 1)

    def test_correct_user_pk(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('drinks details'))
        self.assertEqual(response.context['user_pk'], user.pk)

    def test_taking_drinks_by_user_and_date(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user,
                                      )
        drink2 = Drinks.objects.create(**self.test_drink2,
                                       user=user,
                                       )
        response = self.client.get(reverse('drinks details'))
        self.assertEqual(len(response.context['user_drinks']), 2)


class TestActivitiesDetailsView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
    test_user2 = {'username': 'testuser2',
                  'password': '1234567'}
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
    test_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 600,
    }
    test_activity2 = {
        'activity': 'deadlift',
        'time': 15,
        'calories': 300,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('activities details'))
        self.assertTemplateUsed('activities_details.html')

    def test_correctly_taking_activities_by_user(self):
        user = TheUser.objects.create_user(**self.test_user)
        user2 = TheUser.objects.create_user(**self.test_user2)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user,
                                             )
        activity2 = Activities.objects.create(**self.test_activity2,
                                              user=user2,
                                              )
        response = self.client.get(reverse('activities details'))
        self.assertEqual(len(response.context['all_user_activities']), 1)

    def test_correct_user_pk(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('activities details'))
        self.assertEqual(response.context['user_pk'], user.pk)

    def test_taking_activities_by_user_and_date(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user,
                                             )
        activity2 = Activities.objects.create(**self.test_activity2,
                                              user=user,
                                              )
        response = self.client.get(reverse('activities details'))
        self.assertEqual(len(response.context['user_activities']), 2)


class TestMealsEditView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('edit meal', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('edit_meals.html')

    def test_change_meal_info(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        response = self.client.post(reverse('edit meal', kwargs={'pk': profile.pk}), {'meal': 'beef',
                                                                                      'weight': 300,
                                                                                      'calories': 1500})
        meal.refresh_from_db()
        self.assertEqual(meal.meal, 'beef')
        self.assertEqual(meal.weight, 300)
        self.assertEqual(meal.calories, 1500)
        self.assertEqual(meal.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        response = self.client.post(reverse('edit meal', kwargs={'pk': profile.pk}), {'meal': 'beef',
                                                                                      'weight': 300,
                                                                                      'calories': 1500})
        meal.refresh_from_db()
        self.assertRedirects(response, reverse('meals details'))


class TestDrinksEditView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('edit drink', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('edit_drinks.html')

    def test_change_drink_info(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user)
        response = self.client.post(reverse('edit drink', kwargs={'pk': profile.pk}), {'drink': 'vodka',
                                                                                       'weight': 100,
                                                                                       'calories': 600})
        drink.refresh_from_db()
        self.assertEqual(drink.drink, 'vodka')
        self.assertEqual(drink.weight, 100)
        self.assertEqual(drink.calories, 600)
        self.assertEqual(drink.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user)
        response = self.client.post(reverse('edit drink', kwargs={'pk': profile.pk}), {'drink': 'tea',
                                                                                       'weight': 100,
                                                                                       'calories': 200})
        drink.refresh_from_db()
        self.assertRedirects(response, reverse('drinks details'))


class TestActivitiesEditView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 600,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        response = self.client.get(reverse('edit activity', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('edit_activity.html')

    def test_change_activity_info(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user)
        response = self.client.post(reverse('edit activity', kwargs={'pk': profile.pk}), {'activity': 'deadlift',
                                                                                          'time': 15,
                                                                                          'calories': 300})
        activity.refresh_from_db()
        self.assertEqual(activity.activity, 'deadlift')
        self.assertEqual(activity.time, 15)
        self.assertEqual(activity.calories, 300)
        self.assertEqual(activity.user, user)

    def test_success_url(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user)
        response = self.client.post(reverse('edit activity', kwargs={'pk': profile.pk}), {'activity': 'deadlift',
                                                                                          'time': 15,
                                                                                          'calories': 300})
        activity.refresh_from_db()
        self.assertRedirects(response, reverse('activities details'))


class TestDeleteMealView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        response = self.client.get('delete meal', kwargs={'pk': meal.pk})
        self.assertTemplateUsed('delete_meal.html')

    def test_for_deleting_user_and_profile_at_the_same_time(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        response = self.client.post('delete meal', kwargs={'pk': meal.pk})
        try:
            meal.refresh_from_db()
        except:
            self.assert_(True)

    def test_redirect_to_home_after_deleting_user_and_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        response = self.client.post(reverse('delete meal', kwargs={'pk': meal.pk}), {**self.test_meal,
                                                                                     'user': user})
        self.assertRedirects(response, '/calories/meals/details/')


class TestDeleteDrinkView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user)
        response = self.client.get('delete drink', kwargs={'pk': drink.pk})
        self.assertTemplateUsed('delete_drink.html')

    def test_for_deleting_user_and_profile_at_the_same_time(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user)
        response = self.client.post('delete drink', kwargs={'pk': drink.pk})
        try:
            drink.refresh_from_db()
        except:
            self.assert_(True)

    def test_redirect_to_home_after_deleting_user_and_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user)
        response = self.client.post(reverse('delete drink', kwargs={'pk': drink.pk}), {**self.test_drink,
                                                                                       'user': user})
        self.assertRedirects(response, '/calories/drinks/details/')


class TestDeleteActivityView(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 600,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user)
        response = self.client.get('delete activity', kwargs={'pk': activity.pk})
        self.assertTemplateUsed('delete_activity.html')

    def test_for_deleting_user_and_profile_at_the_same_time(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user)
        response = self.client.post('delete activity', kwargs={'pk': activity.pk})
        try:
            activity.refresh_from_db()
        except:
            self.assert_(True)

    def test_redirect_to_home_after_deleting_user_and_profile(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user)
        response = self.client.post(reverse('delete activity', kwargs={'pk': activity.pk}), {**self.test_activity,
                                                                                             'user': user})
        self.assertRedirects(response, '/calories/activities/details/')


class TestMyHistory(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }
    test_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }
    test_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 300,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user,
                                      )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user,
                                             )
        response = self.client.get('my history', kwargs={'pk': user.pk})
        self.assertTemplateUsed('my_history.html')

    def test_my_history_context(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user,
                                      )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user,
                                             )
        response = self.client.get(reverse('my history', kwargs={'pk': user.pk}))

        self.assertEqual(response.context['user_pk'], user.pk)
        self.assertEqual(response.context['dates'][0], meal.date_of_input)


class TestHistoryOfDay(TestCase):
    test_user = {'username': 'testuser',
                 'password': '123456'}
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
    test_meal = {
        'meal': 'samon',
        'weight': 500,
        'calories': 2000,
    }
    test_drink = {
        'drink': 'water',
        'weight': 500,
        'calories': 100,
    }
    test_activity = {
        'activity': 'running',
        'time': 30,
        'calories': 300,
    }

    def test_correct_template(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user,
                                      )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user,
                                             )
        response = self.client.get(reverse('history', kwargs={'day': meal.date_of_input.day,
                                                              'month': meal.date_of_input.month,
                                                              'year': meal.date_of_input.year,
                                                              'pk': user.pk}))
        self.assertTemplateUsed('history_of_day.html')

    def test_history_of_day_context_date(self):
        user = TheUser.objects.create_user(**self.test_user)
        self.client.login(**self.test_user)
        profile = Profile.objects.create(**self.test_profile,
                                         user=user,
                                         )
        meal = Meals.objects.create(**self.test_meal,
                                    user=user)
        drink = Drinks.objects.create(**self.test_drink,
                                      user=user,
                                      )
        activity = Activities.objects.create(**self.test_activity,
                                             user=user,
                                             )
        response = self.client.get(reverse('history', kwargs={'day': meal.date_of_input.day,
                                                              'month': meal.date_of_input.month,
                                                              'year': meal.date_of_input.year,
                                                              'pk': user.pk}))
        self.assertEqual(response.context['user_meals'][0], meal)
        self.assertEqual(response.context['user_drinks'][0], drink)
        self.assertEqual(response.context['user_activities'][0], activity)
        self.assertEqual(response.context['user_pk'], user.pk)
        self.assertEqual(response.context['consumed_cal'], sum([meal.calories, drink.calories]))
        self.assertEqual(response.context['burned_cal'], sum([activity.calories]))