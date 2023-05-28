from django import forms

from .models import TechnologiesModel, TypeOfProjModel, LeadModel


class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search',
                                   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Search"}),
                                   required=False)
    type_of_proj = forms.ModelChoiceField(label='Type of project', queryset=TypeOfProjModel.objects.all(),
                                          widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
                                          required=False)
    tech_stack = forms.ModelChoiceField(label='Tech stack', queryset=TechnologiesModel.objects.all(),
                                        widget=forms.Select(attrs={'class': 'btn btn-secondary dropdown-toggle'}),
                                        required=False)


class LeadForm(forms.Form):

    name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Name:'}))
    company_name = forms.CharField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Company:'}))
    email = forms.EmailField(max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Email:'}))

    description = forms.Field(widget=forms.TextInput(attrs={'placeholder': 'Email:'}))

