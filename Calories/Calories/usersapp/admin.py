from django.contrib import admin

from Calories.contentapp.models import Meals, Drinks, Activities
from Calories.usersapp.models import Profile, UserModel


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    pass


@admin.register(Drinks)
class DrinksAdmin(admin.ModelAdmin):
    pass


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    pass

