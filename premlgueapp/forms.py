from django import forms
from premlgueapp.models import Overview

class OverviewForm(forms.ModelForm):
    class Meta:
        model = Overview
        fields = "__all__"
