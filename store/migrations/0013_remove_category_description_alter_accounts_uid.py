# Generated by Django 4.0.8 on 2022-10-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_remove_category_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x7f7e11f0a710>', max_length=200),
        ),
    ]
