# Generated by Django 3.2.7 on 2022-06-03 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tabela', '0002_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='tipofonte',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tabela.source'),
        ),
    ]
