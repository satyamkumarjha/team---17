# Generated by Django 3.0.6 on 2020-10-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=300)),
                ('course_id', models.IntegerField()),
                ('course_info', models.TextField()),
                ('cover_image_url', models.SlugField()),
                ('videos_location', models.SlugField()),
                ('instructor_name', models.CharField(max_length=300)),
                ('instructor_qualification', models.CharField(max_length=300)),
                ('reviewer_name', models.CharField(max_length=300)),
                ('review_para', models.TextField()),
                ('review_rating', models.IntegerField()),
            ],
        ),
    ]
