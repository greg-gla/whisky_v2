from django.urls import path, include
from django.contrib.auth.decorators import login_required

app_name = 'pages'

from pages.views import (
	about_view,
	delete_review,
	WhiskyList,
	WhiskyView,
	AddReviewView,
	EditReviewView,
	WarningView,
)

urlpatterns = [
	path('about/', about_view, name='about'),
	path('list/<int:pk>/', WhiskyList.as_view(), name='whisky-list'),
	path('whisky/<int:pk>/', WhiskyView.as_view(), name='view-whisky'),
	path('add_review/<int:pk>/', login_required(AddReviewView.as_view()), name='add-review'),
	path('edit_review/<int:pk>/', login_required(EditReviewView.as_view()), name='edit-review'),
	path('warning/<int:pk>/', login_required(WarningView.as_view()), name='warning'),
	path('delete_rating/<int:pk>/', login_required(delete_review), name='delete-review'),
]