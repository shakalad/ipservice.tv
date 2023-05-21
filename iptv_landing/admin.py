from django.contrib import admin
from .models import *


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'application_status', 'name_surname', 'phone_number', 'call_status', 'declined_reason',
                    'town', 'competitor', 'other_comment', 'updated_at',)
    list_display_links = ('name_surname', 'phone_number', 'application_status', 'call_status', 'declined_reason',
                          'town', 'competitor', 'created_at')
    list_filter = ('application_status', 'call_status', 'created_at', 'competitor')
    search_fields = ('name_surname', 'phone_number', 'other_comment', 'created_at')


class PaymentInstance(admin.TabularInline):
    model = Payments
    readonly_fields = ('payment_time',)
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('application', 'phone_number', 'email', 'status', 'first_payment_date', 'payed_until', 'comment')
    list_display_links = ('phone_number', 'status', 'email', 'application', 'first_payment_date', 'payed_until', 'comment')
    search_fields = ('application__name_surname', 'phone_number', 'email', 'payed_until', 'comment')
    list_filter = ('status', )
    inlines = [PaymentInstance]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'payment_time')
    list_display_links = ('client', 'amount')
    search_fields = ('client__application__name_surname', 'amount', 'payment_time')
    list_filter = ('payment_time',)
    readonly_fields = ('payment_time', )


# KZ SETTINGS ======================================================================================
class ApplicationKZAdmin(admin.ModelAdmin):
    list_display = (
    'created_at', 'application_status', 'name_surname', 'phone_number', 'call_status', 'declined_reason',
    'town', 'competitor', 'other_comment', 'updated_at',)
    list_display_links = ('name_surname', 'phone_number', 'application_status', 'call_status', 'declined_reason',
                          'town', 'competitor', 'created_at')
    list_filter = ('application_status', 'call_status', 'created_at', 'competitor')
    search_fields = ('name_surname', 'phone_number', 'other_comment', 'created_at')


class PaymentKZInstance(admin.TabularInline):
    model = PaymentsKZ
    readonly_fields = ('payment_time',)
    extra = 1


class ClientKZAdmin(admin.ModelAdmin):
    model = ClientKZ
    list_display = ('application', 'phone_number', 'email', 'status', 'first_payment_date', 'payed_until', 'comment')
    list_display_links = ('phone_number', 'status', 'email', 'application', 'first_payment_date', 'payed_until', 'comment')
    search_fields = ('application__name_surname', 'phone_number', 'email', 'payed_until', 'comment')
    list_filter = ('status', )
    inlines = [PaymentKZInstance]


class PaymentKZAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'payment_time')
    list_display_links = ('client', 'amount')
    search_fields = ('client__application__name_surname', 'amount', 'payment_time')
    list_filter = ('payment_time',)
    readonly_fields = ('payment_time', )


# GEO settings
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Payments, PaymentAdmin)
# KZ settings
admin.site.register(ApplicationKZ, ApplicationKZAdmin)
admin.site.register(ClientKZ, ClientKZAdmin)
admin.site.register(PaymentsKZ, PaymentKZAdmin)


