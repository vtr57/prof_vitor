# Generated by Django 5.0.7 on 2024-07-27 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_notasaula_caminho_html_notasaula_caminho_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notasaula',
            old_name='caminho_url',
            new_name='caminho_html',
        ),
    ]
