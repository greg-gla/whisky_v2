from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .forms import AccountAuthenticationForm, RegistrationForm, UserUpdateForm
from django.core.exceptions import ValidationError
from accounts.models import User
from django.views.generic import View, TemplateView, UpdateView
from django.contrib.auth import views as auth_views

# Create your views here.
def login_view(request, *args, **kwargs):
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect('home')
	
	form = AccountAuthenticationForm()
	destination = get_next_if_exists(request)

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				request.session['user_id'] = user.id
				request.session['username'] = user.username
				
				login(request, user)
				if destination:
					return redirect(destination)
				else:
					return redirect('home')

	context['login_form'] = form
	return render(request, 'accounts/login.html', context)	

def logout_view(request):
	logout(request)
	return redirect('home')

class RegisterView(View):
	def get(self, request):
		if request.user.is_authenticated:
			return redirect('home')

		context = {}	
		form = RegistrationForm()
		context['registration_form'] = form

		return render(request, 'accounts/register.html', context)	

	def post(self, request):
		context = {}
		form = RegistrationForm(request.POST)

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			request.session['user_id'] = account.id
			request.session['username'] = account.username

			return redirect('home')
		else:
			context['registration_form'] = form

			return render(request, 'accounts/register.html', context)

class UserProfileView(TemplateView):
	template_name = 'accounts/profile.html'

	def post(self, request):
		context = {}
		form = UserUpdateForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
		else:
			context['form'] = form	

		return render(request, 'accounts/profile.html', context)

class EditPasswordView(auth_views.PasswordChangeView):
	template_name = 'accounts/change_password.html'	

	def get_success_url(self):
		return reverse('home')

def get_next_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect