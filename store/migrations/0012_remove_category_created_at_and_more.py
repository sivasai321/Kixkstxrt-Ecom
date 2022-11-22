# Generated by Django 4.0.8 on 2022-10-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_accounts_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
        migrations.RemoveField(
            model_name='category',
            name='trending',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='product',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x7f21d34ce710>', max_length=200),
        ),
    ]
