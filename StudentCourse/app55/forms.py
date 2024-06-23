from app55.models import students
from django import forms


class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['name1','college1','course1']