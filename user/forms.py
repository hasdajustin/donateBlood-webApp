from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BLOOD_GROUP_CHOICES, AREA_CHOICES

class CustomRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=18, max_value=100)
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)
    area = forms.ChoiceField(choices=AREA_CHOICES)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'age', 'blood_group', 'area', 'phone']


from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'age', 'blood_group', 'area', 'phone']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
