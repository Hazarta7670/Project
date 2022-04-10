from django.urls import path

from Calories.contentapp.views import MealView, MealsDetailsView, MealsEditView, delete_meal_view, DrinkView, \
    DrinksDetailsView, DrinksEditView, delete_drink_view, ActivityView, ActivitiesDetailsView, ActivitiesEditView, \
    delete_activity_view, my_history, history_of_day

urlpatterns = [
    path('meals/add/', MealView.as_view(), name='add meal'),
    path('meals/details/', MealsDetailsView.as_view(), name='meals details'),
    path('meals/edit/meal/<int:pk>/', MealsEditView.as_view(), name='edit meal'),
    path('meals/delete/meal/<int:pk>/', delete_meal_view, name='delete meal'),

    path('drinks/add/', DrinkView.as_view(), name='add drink'),
    path('drinks/details/', DrinksDetailsView.as_view(), name='drinks details'),
    path('drinks/edit/drink/<int:pk>/', DrinksEditView.as_view(), name='edit drink'),
    path('drinks/delete/drink/<int:pk>/', delete_drink_view, name='delete drink'),

    path('activities/add/', ActivityView.as_view(), name='add activity'),
    path('activities/details/', ActivitiesDetailsView.as_view(), name='activities details'),
    path('activities/edit/activity/<int:pk>/', ActivitiesEditView.as_view(), name='edit activity'),
    path('activities/delete/activity/<int:pk>/', delete_activity_view, name='delete activity'),

    path('my_history/<int:pk>', my_history, name='my history'),
    path('history/<int:day>/<int:month>/<int:year>/<int:pk>/', history_of_day, name='history'),
]
