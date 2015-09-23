# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email_from',
            field=models.EmailField(blank=True, verbose_name='From address', max_length=254, help_text='The address the email will be sent from'),
        ),
        migrations.AlterField(
            model_name='form',
            name='sites',
            field=models.ManyToManyField(related_name='forms_form_forms', default=[1], to='sites.Site', editable=False),
        ),
    ]
