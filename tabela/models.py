from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Source(models.Model):
    tipo = models.CharField(_("tipo"), unique=True, max_length=100)

    def __str__(self):
        return self.tipo

class Dataset (models.Model):
    serie = models.BigIntegerField(_("serie"), unique=True)
    nome = models.CharField(_("nome"), max_length=150)
    descricao = models.CharField(_("descrição"), max_length=255)
    fonte = models.CharField(_("fonte"), max_length=255)
    tipofonte = models.ForeignKey(Source, on_delete=models.CASCADE, default=1)

    def get_string_fields(self):
        field_names = [field.name for field in Dataset._meta.get_fields()]
        values = []
        for field_name in field_names[1:]:
            values.append('%s' % getattr(self, field_name))
        return values
