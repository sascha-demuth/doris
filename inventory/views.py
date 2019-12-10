from django.shortcuts import render
from django.utils import timezone
from .models import SingleArticle, Category, ArticleDetails, ArticleComments


# Create your views here.
def cat_list(request):
    categorys = Category.objects.all()
    return render(request, 'inventory/cat_list.html', {'categorys': categorys})

