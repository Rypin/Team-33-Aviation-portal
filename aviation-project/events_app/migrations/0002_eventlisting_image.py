# Generated by Django 3.0.6 on 2020-06-18 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventlisting',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='company_logos'),
        ),
    ]
