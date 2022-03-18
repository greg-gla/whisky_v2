from django.urls import path, include
from django.contrib.auth.decorators import login_required

app_name = 'accounts'

from accounts.views import (
	login_view,
	logout_view,
	RegisterView,
	UserProfileView,
	EditPasswordView,
)

urlpatterns = [
	path('login/', login_view, name='login'),
	path('logout/', logout_view, name='logout'),
	path('register/', RegisterView.as_view(), name='register'),
	path('profile/', login_required(UserProfileView.as_view()), name='profile'),
	path('change_password/', login_required(EditPasswordView.as_view()), name='change-password')
]