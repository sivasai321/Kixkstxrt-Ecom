# Generated by Django 4.1.2 on 2022-10-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_accounts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x7f0e7f62a3b0>', max_length=200),
        ),
    ]
