# Generated by Django 4.1.7 on 2023-03-11 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126)),
                ('publish_date', models.DateTimeField(auto_now=True, verbose_name='Publish date')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126)),
                ('appointment_date', models.DateTimeField(verbose_name='Appointment date')),
                ('dismissal_date', models.DateTimeField(verbose_name='Dismissal date')),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=126)),
                ('type', models.CharField(max_length=126)),
                ('url', models.URLField(unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126)),
                ('description', models.TextField(blank=True)),
                ('publish_date', models.DateTimeField(auto_now=True, verbose_name='Publish date')),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=126)),
                ('code', models.CharField(max_length=126, unique=True)),
                ('root_code', models.CharField(max_length=126)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=126, verbose_name='First name')),
                ('last_name', models.CharField(max_length=126, verbose_name='Last name')),
                ('username', models.CharField(max_length=126, unique=True)),
                ('national_code', models.IntegerField(unique=True)),
                ('evidence', models.TextField()),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TagLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.main')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.tag')),
            ],
        ),
        migrations.CreateModel(
            name='PositionLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.position')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.user')),
            ],
        ),
        migrations.CreateModel(
            name='MediaLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(default=(0, 0, 0), verbose_name='Start time')),
                ('end_time', models.TimeField(default=(0, 0, 0), verbose_name='End time')),
                ('description', models.TextField(blank=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.main')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.repository')),
            ],
        ),
        migrations.AddField(
            model_name='main',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.tree'),
        ),
        migrations.AddField(
            model_name='main',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.user'),
        ),
        migrations.CreateModel(
            name='DocumentLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_part', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.main')),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experience.repository')),
            ],
        ),
    ]
