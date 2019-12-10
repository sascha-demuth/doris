from django.contrib import admin
from .models import SingleArticle, Category, ArticleDetails, ArticleComments

admin.site.register(SingleArticle)
admin.site.register(Category)
admin.site.register(ArticleDetails)
admin.site.register(ArticleComments)
# Register your models here.
