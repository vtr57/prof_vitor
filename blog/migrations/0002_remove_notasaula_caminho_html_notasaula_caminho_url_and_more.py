# Generated by Django 5.0.7 on 2024-07-27 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notasaula',
            name='caminho_html',
        ),
        migrations.AddField(
            model_name='notasaula',
            name='caminho_url',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notasaula',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='notasaula',
            name='titulo',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
