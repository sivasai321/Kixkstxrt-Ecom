# Generated by Django 4.0.8 on 2022-11-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0035_alter_accounts_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercart',
            name='cancel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usercart',
            name='price_with_offer',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x000002376F3C3010>', max_length=200),
        ),
    ]
