from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin,PermissionRequiredMixin
from django.db.models.query_utils import Q

from django.urls import reverse_lazy
import stripe

from .models import Story
from django.conf import settings
stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class StoryListView(LoginRequiredMixin, ListView):
	model = Story
	template_name = 'index.html'
	context_object_name = 'storylist'
	login_url='login'

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


class StoryDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
	model = Story
	template_name = 'story.html'
	permission_required = 'stories.prime_member'

class AddStoryView(LoginRequiredMixin,CreateView):
	model = Story
	template_name = 'addstory.html'
	fields = ['name','author','release_year','genre','cover','story',]
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class EditStoryView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Story
	template_name = 'editstory.html'
	fields = ['name','author','release_year','genre','cover','story',]
	
	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user

class DeleteStoryView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Story
	template_name = 'deletestory.html'
	success_url = reverse_lazy('home')

	def test_func(self):
		obj = self.get_object()
		return obj.owner == self.request.user


class SearchStoryView(LoginRequiredMixin,ListView):
	model = Story
	template_name = 'search.html'
	context_object_name = 'searchstorylist'

	def get_queryset(self):
		query = self.request.GET['name']
		return Story.objects.filter(name__contains=query)

