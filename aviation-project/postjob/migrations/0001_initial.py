# Generated by Django 3.0.6 on 2020-06-18 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Jobform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('postdate', models.DateField()),
                ('posttime', models.TimeField()),
                ('deadlinedate', models.DateField()),
                ('deadlinetime', models.TimeField()),
                ('jobtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postjob.Jobtype')),
            ],
        ),
    ]
