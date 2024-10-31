from django import forms
from .models import AddOn, UserProfile


class AddOnForm(forms.ModelForm):
    class Meta:
        model = AddOn
        fields = [
            'plan', 'user_amount', 'help_desk', 'dms', 'risk_management', 'custom_branding',
            'gitlab_integration', 'b2b_crm', 'knowledge_base', 'asset_management', 'private_cloud',
            'billing'
        ]
        widgets = {
            'plan': forms.Select(attrs={'id': 'select_plan'}),
            'user_amount': forms.NumberInput(attrs={'id': 'range4'}),
            'billing': forms.RadioSelect(attrs={'name': 'billing'}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'email', 'organization_name', 'phone_number', 'country', 'city',
            'legal_address', 'inn', 'domain_name',
            'payment_method'
        ]
        widgets = {
            'email': forms.EmailInput(),
            'organization_name': forms.TextInput(),
            'phone_number': forms.TextInput(),
            'country': forms.TextInput(),
            'city': forms.TextInput(),
            'legal_address': forms.TextInput(),
            'inn': forms.TextInput(),
            'domain_name': forms.TextInput(),
            'payment_method': forms.RadioSelect(),
            'users_count': forms.NumberInput(),
        }
