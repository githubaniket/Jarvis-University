# Generated by Django 2.1.7 on 2021-04-26 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='ansDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 23, 36, 13, 542981)),
        ),
        migrations.AlterField(
            model_name='studentquestion',
            name='quesDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 26, 23, 36, 13, 542981)),
        ),
    ]
