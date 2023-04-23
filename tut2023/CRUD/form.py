# from django import forms
# from .models import CRUD
#
# class CRUDForm(forms.ModelForm):
#  class Meta:
#   model = CRUD
#   fields = '__all__'
#   labels = {'image':'','firstname':'Doctor Name','lastname':'patient name'}


from django import forms
from .models import CRUD


class CRUDForm(forms.ModelForm):
 class Meta:
  model = CRUD
  fields = '__all__'
  labels = {'image': '', 'firstname': 'Doctor Name', 'lastname': 'Patient Name'}
  widgets = {
   'firstname': forms.TextInput(attrs={'class': 'form-control'}),
   'lastname': forms.TextInput(attrs={'class': 'form-control'}),
  }

 def __init__(self, *args, **kwargs):
  super().__init__(*args, **kwargs)
  self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
