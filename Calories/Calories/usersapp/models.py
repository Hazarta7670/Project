from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.core.validators import MinLengthValidator, EmailValidator, MinValueValidator
from django.db import models

from Calories.usersapp.manager import TheManager
from Calories.usersapp.validators import image_max_size


class UserModel(AbstractBaseUser, PermissionsMixin):
    MAX_LEN_USER = 30
    MIN_LEN_USER = 3

    username = models.CharField(
        max_length=MAX_LEN_USER,
        validators=(MinLengthValidator(MIN_LEN_USER),
                    ),
        unique=True,
    )

    date_join = models.DateTimeField(
        auto_now_add=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = TheManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MIN_LEN = 2
    MIN_WEIGHT = 0
    MIN_HEIGHT = 0
    MIN_AGE = 0
    MALE = 'Male'
    FEMALE = 'Female'
    LITTLE_OR_NO_TRAINING = 'Little or No Training'
    LIGHT_EXERCISES_ONE_TWO_TIMES_A_WEEK = 'Light Exercises One-Two times a Week'
    MODERATELY_LOADED_EXERCISES_TWO_THREE_TIMES_A_WEEK = 'Moderately loaded Exercises Two-Three times a Week'
    INTENSIVE_EXERCISE_FOUR_FIVE_TIMES_A_WEEK = 'Intensive Exercise Four-Five times a Week'
    HEAVY_EXERCISE__PHYSICAL_WORK_OR_SPORT_SIX_SEVEN_DAYS_A_WEEK = \
        'Heavy Exercise, Physical Work or Sport Six-Seven days a Week'
    GENDER_CHOICES = [(x, x) for x in (MALE, FEMALE)]
    ACTIVITY_LEVEL_CHOICES = [(x, x) for x in (LITTLE_OR_NO_TRAINING, LIGHT_EXERCISES_ONE_TWO_TIMES_A_WEEK,
                                               MODERATELY_LOADED_EXERCISES_TWO_THREE_TIMES_A_WEEK,
                                               INTENSIVE_EXERCISE_FOUR_FIVE_TIMES_A_WEEK,
                                               HEAVY_EXERCISE__PHYSICAL_WORK_OR_SPORT_SIX_SEVEN_DAYS_A_WEEK)]

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LEN,
                                  validators=(MinLengthValidator(FIRST_NAME_MIN_LEN),
                                              ),
                                  )

    last_name = models.CharField(max_length=LAST_NAME_MAX_LEN,
                                 validators=(MinLengthValidator(LAST_NAME_MIN_LEN),
                                             ),
                                 )

    image = models.ImageField(validators=(image_max_size,
                                          ),
                              upload_to='images',
                              null=True,
                              blank=True,
                              )

    email = models.EmailField(validators=(EmailValidator,
                                          ),
                              unique=True,
                              )

    age = models.IntegerField(validators=(MinValueValidator(MIN_AGE),
                                          ),
                              default=MIN_AGE,
                              )

    weight = models.FloatField(validators=(MinValueValidator(MIN_WEIGHT),
                                           ),
                               default=MIN_WEIGHT,
                               )

    height = models.FloatField(validators=(MinValueValidator(MIN_HEIGHT),
                                           ),
                               default=MIN_HEIGHT,
                               )
    activity_level = models.CharField(max_length=max(len(x) for x, _ in ACTIVITY_LEVEL_CHOICES),
                                      choices=ACTIVITY_LEVEL_CHOICES,
                                      )

    sex = models.CharField(max_length=max(len(x) for x, _ in GENDER_CHOICES),
                           choices=GENDER_CHOICES,
                           )

    user = models.OneToOneField(UserModel,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
