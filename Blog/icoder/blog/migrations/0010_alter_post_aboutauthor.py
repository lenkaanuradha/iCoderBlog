# Generated by Django 4.2.6 on 2023-10-26 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_aboutauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='aboutauthor',
            field=models.CharField(max_length=500),
        ),
    ]
