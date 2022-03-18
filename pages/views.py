from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from pages.models import Distillery, Whisky, Rating
from django.shortcuts import get_object_or_404

# Create your views here.

class IndexView(TemplateView):
	template_name = 'pages/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['distilleries'] = Distillery.objects.all()

		return context

class WhiskyList(ListView):
	template_name = 'pages/whisky_list.html'
	paginate_by = 10

	def get_queryset(self, *args, **kwargs):
		instance = 	get_object_or_404(Distillery, pk=self.kwargs.get('pk'))
		queryset = Whisky.objects.filter(distillery=instance.pk)	
		
		if 'rating' in self.request.GET:
			rating = int(self.request.GET.get('rating'))

			whiskies = []	
			for q in queryset:
				avg = calculate_rating(Rating.objects.filter(whisky_id=q.pk))
				if avg >= rating:
					whiskies.append(q.pk)

			queryset = queryset.filter(pk__in=whiskies)		

		return queryset.order_by('-pk')

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		instance = get_object_or_404(Distillery, pk=self.kwargs.get('pk'))

		if 'rating' in self.request.GET:
				rating = int(self.request.GET.get('rating'))
				context['filter_rate'] = rating

		context['distillery'] = instance

		return context

def about_view(request):
	return render(request, 'pages/about.html')

class WhiskyView(TemplateView):
	template_name = 'pages/whisky.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		instance = get_object_or_404(Whisky, pk=self.kwargs.get('pk'))
		context['whisky'] = instance
		context['ratings'] = Rating.objects.filter(whisky_id=instance.pk).order_by('-pk')
		context['average_rate'] = calculate_rating(context['ratings'])

		return context

class AddReviewView(CreateView):
	model = Rating
	fields = ['numeric_rating', 'verbal_rating', 'whisky_id', 'user_id']

	def get(self, request, **kwargs):
		context = {}
		instance = get_object_or_404(Whisky, pk=self.kwargs.get('pk'))
		context['whisky_id'] = instance.pk

		try:
			_ = Rating.objects.filter(whisky_id=instance.pk).get(user_id=self.request.user.id)
		except Rating.DoesNotExist:
			return render(request, 'pages/add_review.html', context)

		context['user_review']	= Rating.objects.filter(whisky_id=instance.pk).get(user_id=self.request.user.id)
		return render(request, 'pages/info.html', context)	

	def get_success_url(self):
		return reverse('pages:view-whisky', kwargs={'pk': self.kwargs['pk']})

class EditReviewView(UpdateView):
	model = Rating
	template_name = 'pages/edit_review.html'
	fields = ['numeric_rating', 'verbal_rating', 'whisky_id', 'user_id']

	def post(self, request, **kwargs):
		instance = get_object_or_404(Rating, pk=self.kwargs.get('pk'))
		if instance.user_id.id != self.request.user.id:
			return redirect('home')
	
		return super().post(request, **kwargs)

	def get_success_url(self):
		instance = get_object_or_404(Rating, pk=self.kwargs.get('pk'))
		return reverse('pages:view-whisky', kwargs={'pk': instance.whisky_id.pk})

class WarningView(TemplateView):
	template_name = 'pages/warning.html'		

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		instance = get_object_or_404(Rating, pk=self.kwargs.get('pk'))
		context['rating'] = instance

		return context	

def delete_review(request, *args, **kwargs):
	instance = get_object_or_404(Rating, pk=kwargs.get('pk'))
	primary_key = instance.whisky_id.pk

	if instance.user_id.pk != request.user.id:
		return redirect('home')

	Rating.objects.filter(pk=instance.pk).delete()

	return redirect('pages:view-whisky', primary_key)	

class SearchView(ListView):
	template_name = 'pages/results_list.html'
	paginate_by = 10

	def get_queryset(self):
		if 'q' in self.request.GET:
			query = self.request.GET.get('q')

			return Whisky.objects.filter(name__startswith=query)
		else:
			return redirect('home')	

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		if 'q' in self.request.GET:
			query = self.request.GET.get('q')
			context['query'] = query	

		return context

def calculate_rating(ratings):
	if len(ratings) == 0:
		return -1

	acc = 0
	for rating in ratings:
		acc += rating.numeric_rating

	return round(acc / len(ratings), 1)

