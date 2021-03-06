from django.contrib import admin
from .models import *


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_number', 'name', 'city', 'cell_phone')
    list_filter = ('cust_number', 'name', 'city')
    search_fields = ('cust_number', 'name')
    ordering = ['cust_number']


class InvestmentList(admin.ModelAdmin):
    list_display = ('customer', 'category', 'description', 'recent_value')
    list_filter = ('customer', 'category')
    search_fields = ('customer', 'category')
    ordering = ['customer']


class StockList(admin.ModelAdmin):
    list_display = ('customer', 'symbol', 'name', 'shares', 'purchase_price')
    list_filter = ('customer', 'symbol', 'name')
    search_fields = ('customer', 'symbol', 'name')
    ordering = ['customer']


class FundList(admin.ModelAdmin):
    list_display = ('customer', 'fund_type', 'fund_amount', 'start_date', 'end_date')
    list_filter = ('customer', 'fund_type')
    search_fields = ('customer', 'fund_type')
    ordering = ['customer']


admin.site.register(Customer, CustomerList)
admin.site.register(Investment, InvestmentList)
admin.site.register(Stock, StockList)
admin.site.register(Fund, FundList)
