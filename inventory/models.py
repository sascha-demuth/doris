""" 
Modelsfile of Django

Project : D.O.R.I.S

stands for Decentral Operable Ressource Information System 
or
Dezentral Operables Ressourcen Informations-System

Author : Sascha Michael Demuth
Email  : sascha.demuth@web.de

"""


from django.conf import settings
from django.db import models
from django.utils import timezone

"""

class : singleArticle

In this class I define the object for the articles. Every articleinstance will have it's own description in the ArticleDetails-Table.

"""

class SingleArticle(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    barcodeID = models.IntegerField()
    articleClass = models.IntegerField()
    childOf = models.IntegerField()
    statusInt = models.IntegerField()
    creationDate = models.DateTimeField(default=timezone.now)

class Category(models.Model):
    catName = models.CharField(max_length=200)

class ArticleDetails(models.Model):
    artName = models.CharField(max_length=200)
    catFK = models.IntegerField()
    referenceFK = models.IntegerField()

class ArticleComments(models.Model):
    commentType = models.IntegerField()
    modelReferenceFK = models.IntegerField()
    articleReferenceFK = models.IntegerField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creationDate = models.DateTimeField(default=timezone.now)
    isActive = models.BooleanField(default=True)
    commentContent = models.TextField()
    commentDescription = models.TextField()
