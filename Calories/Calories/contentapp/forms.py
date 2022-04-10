from django import forms

from Calories.contentapp.models import Meals, Drinks, Activities


class MealForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ['meal', 'weight', 'calories', 'image']
        widgets = {
            'meal': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter your Meal'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter the Weight of your Meal in Grams'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter the Calories of the Meal'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add a Picture of the Meal'}),

        }


class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drinks
        fields = ['drink', 'weight', 'calories', 'image']
        widgets = {
            'drink': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter your Drink'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter the Weight of your Drink in Grams'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter the Calories of the Drink'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add a Picture of the Drink'}),

        }


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['activity', 'time', 'calories', 'image']
        widgets = {
            'activity': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter your Activity'}),
            'time': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter the Duration of your Activity in Minutes'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter the Calories Burned in your Activity'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add a Picture of the Activity'}),

        }


class DeleteMealForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Meals
        fields = ['meal', 'weight', 'calories', 'image']
        widgets = {
            'meal': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter your Meal'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter the Weight of your Meal in Grams'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter the Calories of the Meal'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add a Picture of the Meal'}),
        }


class DeleteDrinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Drinks
        fields = ['drink', 'weight', 'calories', 'image']
        widgets = {
            'drink': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter your Drink'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter the Weight of your Drink in Grams'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter the Calories of the Drink'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add a Picture of the Drink'}),

        }


class DeleteActivityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Activities
        fields = ['activity', 'time', 'calories', 'image']
        widgets = {
            'activity': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Enter your Activity'}),
            'time': forms.NumberInput(attrs={'class': 'form-control',
                                             'placeholder': 'Enter the Duration of your Activity in Minutes'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Enter the Calories Burned in your Activity'}),
            'image': forms.FileInput(attrs={'placeholder': 'Add a Picture of the Activity'}),

        }