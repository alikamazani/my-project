from django import forms
from steps_count.models import Top_List

class Top_List_Form(forms.ModelForm):
    class Meta:
        model=Top_List