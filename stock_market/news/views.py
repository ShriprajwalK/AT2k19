from django.shortcuts import render
from django.utils import timezone
from .models import NewsPost

def news_list(request):
    posts = NewsPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/news_list.html', {'posts':posts})
