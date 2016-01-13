# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_lists', '0003_habitlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='habit_list',
            field=models.ForeignKey(to='habit_lists.HabitList', default=None),
        ),
    ]
