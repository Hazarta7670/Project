from unittest import TestCase

from django.core.exceptions import ValidationError

from Calories.usersapp.validators import image_max_size


class BiggerFakeSize:
    size = 5242890


class SmallerFakeSize:
    size = 5242870


class BiggerFakeFile(BiggerFakeSize):
    file = BiggerFakeSize


class SmallerFakeFile(SmallerFakeSize):
    file = SmallerFakeSize


class TestValidator(TestCase):
    def test_bigger_image_size(self):
        file = BiggerFakeFile
        with self.assertRaises(ValidationError) as context:
            image_max_size(file)
        self.assertIsNotNone(context.exception)

    def test_small_image_size(self):
        file = SmallerFakeFile
        image_max_size(file)
        self.assertTrue(True)
