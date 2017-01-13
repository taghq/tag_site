# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='signup_form.BaseModel', primary_key=True)),
                ('title', models.CharField(max_length=100, db_index=True)),
                ('experts', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('signup_form.basemodel',),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='signup_form.BaseModel', primary_key=True)),
                ('name', models.CharField(max_length=100, db_index=True)),
                ('email', models.EmailField(max_length=100, db_index=True)),
                ('interests', models.ManyToManyField(related_name='interests', blank=True, to='signup_form.Interest')),
            ],
            bases=('signup_form.basemodel',),
        ),
    ]
