from django import forms
from myapp.models import Player
class PlayerModel2Form(forms.ModelForm):
  class Meta:
    model = Player
    fields = '__all__'