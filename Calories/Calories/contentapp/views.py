from datetime import datetime

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView

from Calories.contentapp.forms import MealForm, DeleteMealForm, DrinkForm, DeleteDrinkForm, ActivityForm, \
    DeleteActivityForm
from Calories.contentapp.models import Meals, Drinks, Activities


class MealView(CreateView):
    form_class = MealForm
    template_name = 'add_meal.html'
    success_url = reverse_lazy('meals details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MealsDetailsView(TemplateView):
    model = Meals
    template_name = 'meals_details.html'
    context_object_name = 'meals'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.now().date()
        all_user_meals = list(Meals.objects.filter(user_id=self.request.user.pk))
        user_meals = list(Meals.objects.filter(date_of_input__year=datetime.now().year,
                                               date_of_input__month=datetime.now().month,
                                               date_of_input__day=datetime.now().day,
                                               user_id=self.request.user.pk))
        user_primary_key = self.request.user.pk
        context.update({'user_meals': user_meals, 'date': date, 'all_user_meals': all_user_meals,
                        'user_pk': user_primary_key})
        return context


class MealsEditView(UpdateView):
    model = Meals
    fields = ['meal', 'weight', 'calories', 'image']
    template_name = 'edit_meals.html'
    context_object_name = 'meal'

    def get_success_url(self):
        return reverse('meals details')


def delete_meal_view(request, pk):
    meal = Meals.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteMealForm(instance=meal)
        return render(request, 'delete_meal.html', {'form': form, 'meal': meal})
    else:
        form = DeleteMealForm(request.POST, instance=meal)
        form.save()
        return redirect('meals details')


class DrinkView(CreateView):
    form_class = DrinkForm
    template_name = 'add_drink.html'
    success_url = reverse_lazy('drinks details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DrinksDetailsView(TemplateView):
    model = Drinks
    template_name = 'drinks_details.html'
    context_object_name = 'drinks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.now().date()
        all_user_drinks = list(Drinks.objects.filter(user_id=self.request.user.pk))
        user_drinks = list(Drinks.objects.filter(date_of_input__year=datetime.now().year,
                                                 date_of_input__month=datetime.now().month,
                                                 date_of_input__day=datetime.now().day,
                                                 user_id=self.request.user.pk))
        user_primary_key = self.request.user.pk
        context.update({'user_drinks': user_drinks, 'date': date, 'all_user_drinks': all_user_drinks,
                        'user_pk': user_primary_key})
        return context


class DrinksEditView(UpdateView):
    model = Drinks
    fields = ['drink', 'weight', 'calories', 'image']
    template_name = 'edit_drinks.html'
    context_object_name = 'drink'

    def get_success_url(self):
        return reverse('drinks details')


def delete_drink_view(request, pk):
    drink = Drinks.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteDrinkForm(instance=drink)
        return render(request, 'delete_drink.html', {'form': form, 'drink': drink})
    else:
        form = DeleteDrinkForm(request.POST, instance=drink)
        form.save()
        return redirect('drinks details')


class ActivityView(CreateView):
    form_class = ActivityForm
    template_name = 'add_activity.html'
    success_url = reverse_lazy('activities details')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ActivitiesDetailsView(TemplateView):
    model = Activities
    template_name = 'activities_details.html'
    context_object_name = 'activities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.now().date()
        all_user_activities = list(Activities.objects.filter(user_id=self.request.user.pk))
        user_activities = list(Activities.objects.filter(date_of_input__year=datetime.now().year,
                                                         date_of_input__month=datetime.now().month,
                                                         date_of_input__day=datetime.now().day,
                                                         user_id=self.request.user.pk))
        user_primary_key = self.request.user.pk
        context.update({'user_activities': user_activities, 'date': date, 'all_user_activities': all_user_activities,
                        'user_pk': user_primary_key})
        return context


class ActivitiesEditView(UpdateView):
    model = Activities
    fields = ['activity', 'time', 'calories', 'image']
    template_name = 'edit_activity.html'
    context_object_name = 'activity'

    def get_success_url(self):
        return reverse('activities details')


def delete_activity_view(request, pk):
    activity = Activities.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteActivityForm(instance=activity)
        return render(request, 'delete_activity.html', {'form': form, 'activity': activity})
    else:
        form = DeleteActivityForm(request.POST, instance=activity)
        form.save()
        return redirect('activities details')


class MyHistory(DetailView):
    template_name = 'my_history.html'

    def get_queryset(self):
        user = get_user_model().objects.filter(pk=self.request.user.pk)
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_meals = sorted(list(Meals.objects.filter(user_id=self.request.user.pk).distinct('date_of_input')),
                            key=lambda x: x.date_of_input)
        user_drinks = sorted(list(Drinks.objects.filter(user_id=self.request.user.pk).distinct('date_of_input')),
                             key=lambda x: x.date_of_input)
        user_activities = sorted(list(Activities.objects.filter(user_id=self.request.user.pk).distinct('date_of_input')),
                                 key=lambda x: x.date_of_input)
        dates = []
        user_pk = self.request.user.pk
        for meal in user_meals:
            if meal.date_of_input not in dates:
                dates.append(meal.date_of_input)
        for drink in user_drinks:
            if drink.date_of_input not in dates:
                dates.append(drink.date_of_input)
        for activity in user_activities:
            if activity.date_of_input not in dates:
                dates.append(activity.date_of_input)
        dates = sorted(dates, key=lambda x: x)
        context.update({'dates': dates, 'user_pk': user_pk})
        return context


class HistoryOfTheDay(TemplateView):
    template_name = 'history_of_day.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_meals = list(Meals.objects.filter(date_of_input__year=context['year'],
                                               date_of_input__month=context['month'],
                                               date_of_input__day=context['day'],
                                               user_id=self.request.user.pk))
        user_drinks = list(Drinks.objects.filter(date_of_input__year=context['year'],
                                                 date_of_input__month=context['month'],
                                                 date_of_input__day=context['day'],
                                                 user_id=self.request.user.pk))
        user_activities = list(Activities.objects.filter(date_of_input__year=context['year'],
                                                         date_of_input__month=context['month'],
                                                         date_of_input__day=context['day'],
                                                         user_id=self.request.user.pk))
        consumed_cal = sum([meal.calories for meal in user_meals]) + sum([drink.calories for drink in user_drinks])
        burned_cal = sum([activity.calories for activity in user_activities])
        user_pk = self.request.user.pk
        context.update({'user_meals': user_meals, 'user_drinks': user_drinks,
                                                  'user_activities': user_activities, 'user_pk': user_pk,
                                                  'consumed_cal': consumed_cal, 'burned_cal': burned_cal})
        return context
