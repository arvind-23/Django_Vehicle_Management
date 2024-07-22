from django import forms
from .models import Feedback
from .models import VehicleInventory
from .models import TestDrive

class VehicleForm(forms.ModelForm):
    class Meta:
        model=VehicleInventory
        fields='__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

class TestDriveForm(forms.ModelForm):
    class Meta:
        model=TestDrive
        fields='__all__'