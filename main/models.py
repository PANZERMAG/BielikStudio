from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class TechnologiesModel(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Technologies'


class TypeOfProjModel(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Type of project'


class PortfolioItem(models.Model):
    title = models.CharField(max_length=100)

    description = CKEditor5Field('Text', config_name='extends')
    short_desc = models.CharField(max_length=100)

    task_short = models.CharField(max_length=200)
    solution_short = models.CharField(max_length=200)


    tech_stack = models.ManyToManyField(TechnologiesModel)
    tag = models.ForeignKey('TypeOfProjModel', null=True, on_delete=models.SET_NULL)

    logo_portfolio = models.FileField(upload_to='media')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Portfolio item'


class LeadModel(models.Model):
    name = models.CharField(max_length=60)
    company_name = models.CharField(max_length=60)
    email = models.EmailField()
    description = models.TextField()
