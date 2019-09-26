from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic import TemplateView



class OrdersView(TemplateView):
	template_name = 'orders.html'

	
