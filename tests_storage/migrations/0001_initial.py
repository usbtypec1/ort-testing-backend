# Generated by Django 4.0.4 on 2022-05-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('section', models.PositiveSmallIntegerField(choices=[(0, 'Analogies'), (1, 'Sentences completion'), (2, 'Math part 1'), (3, 'Math part 2'), (4, 'Reading'), (5, 'Grammar')])),
                ('correct_answer', models.TextField()),
                ('wrong_answer_1', models.TextField()),
                ('wrong_answer_2', models.TextField()),
                ('wrong_answer_3', models.TextField()),
                ('wrong_answer_4', models.TextField(blank=True, null=True)),
                ('tests', models.ManyToManyField(to='tests_storage.test')),
            ],
        ),
    ]
