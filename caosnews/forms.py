
from django.forms import ModelForm
from .models import caosnews

class caosnewsForm(ModelForm):
    class Meta:
     model = caosnews
     fields = "__all__"