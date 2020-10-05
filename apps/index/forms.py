from django import forms
from .models import SchoolLevel, School
from apps.forms import FormMixin


class SchoolLevelForm(forms.ModelForm, FormMixin):
    class Meta:
        model = SchoolLevel
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        exists = SchoolLevel.objects.filter(name=name).exists()
        if exists:
            raise forms.ValidationError('此科研等级已经存在！')
        else:
            return name


class SchoolForm(forms.ModelForm, FormMixin):
    school_level = forms.IntegerField()
    school_category = forms.IntegerField()

    class Meta:
        model = School
        exclude = ['school_level', 'school_category', 'reg_time']


class AddMessageForm(forms.Form, FormMixin):
    content = forms.CharField(max_length=100)
