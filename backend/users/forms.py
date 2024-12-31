from django import forms
from .models import User, Company, Candidate

class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(
        choices=[('COMPANY', 'Company'), ('CANDIDATE', 'Candidate')],
        widget=forms.RadioSelect
    )

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name', 'industry', 'location', 'company_size', 'open_positions']

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['establishment_name', 'skills', 'experience', 'preferred_locations']
