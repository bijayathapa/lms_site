# Generated by Django 3.2.7 on 2021-09-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210914_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
