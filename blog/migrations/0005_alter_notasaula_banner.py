# Generated by Django 5.0.7 on 2024-07-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_notasaula_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notasaula',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='img/post/'),
        ),
    ]
