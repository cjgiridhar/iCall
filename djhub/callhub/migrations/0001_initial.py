# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('phone_number', models.CharField(default=b'', max_length=b'50', blank=True)),
                ('title', models.CharField(default=b'', max_length=b'50', blank=True)),
                ('company', models.CharField(default=b'', max_length=b'50', blank=True)),
                ('status', models.CharField(default=b'UNKNOWN', max_length=10, choices=[(b'UNKNOWN', 'Unknown'), (b'INVITED', 'Invitation Sent (only email known)'), (b'IDENTIFIED', 'Identified (email and name known)'), (b'VERIFIED', 'Verified e-mail address'), (b'USER', 'Signed Up')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
