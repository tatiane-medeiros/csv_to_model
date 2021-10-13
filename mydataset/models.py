from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Dataset (models.Model):
    myid = models.IntegerField(_("myid"))
    serie = models.BigIntegerField(_("serie"))
    nome = models.CharField(_("nome"), max_length=150)
    descricao = models.CharField(_("descrição"), max_length=255)
    fonte = models.CharField(_("fonte"), max_length=255)