from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from Calories.usersapp.validators import image_max_size

TheUser = get_user_model()


class Meals(models.Model):
    MAX_LEN = 255
    MIN_WEIGHT = 0
    MIN_LEN = 3

    meal = models.CharField(max_length=MAX_LEN,
                            validators=(MinLengthValidator(MIN_LEN),
                                        ),
                            )

    weight = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                           ),
                               default=MIN_WEIGHT)

    calories = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                             ),
                                 default=MIN_WEIGHT,
                                 )

    image = models.ImageField(validators=(image_max_size,
                                          ),
                              null=True,
                              blank=True,
                              )

    date_of_input = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(TheUser,
                             on_delete=models.CASCADE,
                             )


class Drinks(models.Model):
    MAX_LEN = 255
    MIN_WEIGHT = 0
    MIN_LEN = 3

    drink = models.CharField(max_length=MAX_LEN,
                             validators=(MinLengthValidator(MIN_LEN),
                                         ),
                             )

    weight = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                           ),
                               default=MIN_WEIGHT)

    calories = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                             ),
                                 default=MIN_WEIGHT,
                                 )

    image = models.ImageField(validators=(image_max_size,
                                          ),
                              null=True,
                              blank=True,
                              )

    date_of_input = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(TheUser,
                             on_delete=models.CASCADE,
                             )


class Activities(models.Model):
    MAX_LEN = 255
    MIN_WEIGHT = 0
    MIN_LEN = 3

    activity = models.CharField(max_length=MAX_LEN,
                                validators=(MinLengthValidator(MIN_LEN),
                                            ),
                                )

    time = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                         ),
                             default=MIN_WEIGHT,
                             )

    calories = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                             ),
                                 default=MIN_WEIGHT,
                                 )

    image = models.ImageField(validators=(image_max_size,
                                          ),
                              null=True,
                              blank=True,
                              )
    date_of_input = models.DateField(
        auto_now_add=True,
    )

    user = models.ForeignKey(TheUser,
                             on_delete=models.CASCADE,
                             )

