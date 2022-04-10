from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from Calories.contentapp.models import Meals, Drinks, Activities
from Calories.usersapp.forms import ProfileForm, UserForm
from Calories.usersapp.models import Profile


class HomePage(TemplateView):
    template_name = 'home_page.html'


class ProfileView(CreateView):
    form_class = ProfileForm
    template_name = 'create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile details', kwargs={'pk': self.request.user.pk})


class RegistrateUser(CreateView):
    form_class = UserForm
    template_name = 'create_user.html'
    success_url = reverse_lazy('login page')


class Login(LoginView):
    template_name = 'login_page.html'

    def get_success_url(self):
        return reverse('home page')


class Logout(LogoutView):
    pass


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user_id=self.request.user.pk)

        if profile.sex == 'Male':
            basal_metabolism = (profile.weight * 10) + (6.25 * profile.height) - (5 * profile.age) + 5
        else:
            basal_metabolism = (profile.weight * 10) + (6.25 * profile.height) - (5 * profile.age) - 161
        if profile.activity_level == 'Little or No Training':
            basal_metabolism = basal_metabolism * 1.2
        elif profile.activity_level == 'Light Exercises One-Two times a Week':
            basal_metabolism = basal_metabolism * 1.375
        elif profile.activity_level == 'Moderately loaded Exercises Two-Three times a Week':
            basal_metabolism = basal_metabolism * 1.55
        elif profile.activity_level == 'Intensive Exercise Four-Five times a Week':
            basal_metabolism = basal_metabolism * 1.725
        elif profile.activity_level == 'Heavy Exercise, Physical Work or Sport Six-Seven days a Week':
            basal_metabolism = basal_metabolism * 1.9
        bmi = profile.weight / ((profile.height/100) * (profile.height/100))
        if bmi < 18.5:
            normal = 'Underweight'
        elif 18.5 <= bmi < 25:
            normal = 'Healthy Weight'
        elif 25 <= bmi < 30:
            normal = 'Overweight'
        elif 30 <= bmi <= 35:
            normal = 'Obesity'
        else:
            normal = 'Severe obesity I, II and III degree'

        daily_meals = list(Meals.objects.filter(date_of_input__year=datetime.now().year,
                                                date_of_input__month=datetime.now().month,
                                                date_of_input__day=datetime.now().day,
                                                user_id=self.request.user.pk))
        cal_of_meals = sum([c.calories for c in daily_meals])
        daily_drinks = list(Drinks.objects.filter(date_of_input__year=datetime.now().year,
                                                  date_of_input__month=datetime.now().month,
                                                  date_of_input__day=datetime.now().day,
                                                  user_id=self.request.user.pk))
        cal_of_drinks = sum([d.calories for d in daily_drinks])
        daily_activities = list(Activities.objects.filter(date_of_input__year=datetime.now().year,
                                                          date_of_input__month=datetime.now().month,
                                                          date_of_input__day=datetime.now().day,
                                                          user_id=self.request.user.pk))
        cal_burned = sum([a.calories for a in daily_activities])
        context.update({'basal_metabolism': basal_metabolism, 'bmi': bmi, 'normal': normal,
                        'daily_cal': (cal_of_meals + cal_of_drinks), 'burned': cal_burned})
        return context


class UpdateProfileView(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'email', 'age', 'weight', 'height', 'activity_level', 'sex', 'image']
    template_name = 'profile_edit.html'
    context_object_name = 'profile'

    def get_success_url(self):
        return reverse('profile details', kwargs={'pk': self.object.pk})


class DeleteProfileView(DeleteView):
    model = get_user_model()
    template_name = 'delete_account.html'
    success_url = reverse_lazy('home page')
