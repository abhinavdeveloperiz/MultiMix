from django import forms
from app import models

class Contact(forms.ModelForm):
    class Meta:
        model=models.Contact

        fields=["name","phone","subject","message"]

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Name"}),
            "phone":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Number"}),
            "subject":forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter Subject"}),
            "message":forms.Textarea(attrs={"class":"form-control", "rows":3 ,"placeholder":"Enter Here......"})
        }