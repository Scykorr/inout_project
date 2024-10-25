from django import forms
from .models import AddOn


class AddOnForm(forms.ModelForm):
    class Meta:
        model = AddOn
        fields = [
            'plan', 'users_count', 'help_desk', 'dms', 'risk_management', 'custom_branding',
            'gitlab_integration', 'b2b_crm', 'knowledge_base', 'asset_management', 'private_cloud',
            'billing_period', 'total_price'
        ]
        widgets = {
            'plan': forms.Select(attrs={'id': 'select_plan'}),
            'users_count': forms.NumberInput(attrs={'id': 'range4'}),
            'billing_period': forms.RadioSelect(attrs={'name': 'billing'}),
        }
