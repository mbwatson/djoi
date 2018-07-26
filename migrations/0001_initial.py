# Generated by Django 2.0.7 on 2018-07-26 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
            ],
            options={
                'verbose_name': 'Employee Alias',
                'verbose_name_plural': 'Employee Aliases',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doi', models.CharField(max_length=63, unique=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('citation', models.TextField(blank=True, default='Not available')),
                ('author', models.ManyToManyField(blank=True, to='djoi.Author')),
            ],
        ),
        migrations.AddField(
            model_name='alias',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djoi.Employee'),
        ),
    ]
