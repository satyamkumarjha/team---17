# Generated by Django 3.0.6 on 2021-03-31 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherdata',
            name='teacher_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]