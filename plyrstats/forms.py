from django import forms
from plyrstats.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
