from django.contrib import admin
from .models import Productdetails
from .models import CommercialOffer, Invoice, CompanyDetails, RegularPayment


@admin.register(Productdetails)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'paid_until', 'solution_type', 'package', 'user_count', 'subscription_until')


@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = ('legal_address', 'inn', 'email')


class CommercialOfferAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'amount', 'subject')
    search_fields = ('subject',)
    list_filter = ('created_date',)


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('status', 'subject', 'number', 'created_date')
    search_fields = ('subject', 'number')
    list_filter = ('status', 'created_date')


class RegularPaymentAdmin(admin.ModelAdmin):
    list_display = ('status', 'contact_id', 'product', 'next_payment', 'amount')
    search_fields = ('contact_id', 'product')
    list_filter = ('next_payment', 'status')


admin.site.register(CommercialOffer, CommercialOfferAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(RegularPayment, RegularPaymentAdmin)
