# Generated by Django 3.0.6 on 2021-03-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210323_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
