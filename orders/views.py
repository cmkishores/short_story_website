from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic import TemplateView
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class OrdersView(TemplateView):
	template_name = 'orders.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['stripe_key'] = settings.STRIPE_TEST_PUBLIC_KEY
		return context


def charge(request):


	# takes the permission we set in the model and access using codename
	permission = Permission.objects.get(codename='prime_member')
	
	#get the current user credentials

	u= request.user

	#change the permission of user after payment

	u.user_permissions.add(permission)

	if request.method == 'POST':
		charge = stripe.Charge.create(
			amount = 1000,
			currency='usd',
			description='Purchase all stories',
			source=request.POST['stripeToken']
			)
		return render(request, 'paymentdone.html')

