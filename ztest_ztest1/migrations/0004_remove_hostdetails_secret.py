# Generated by Django 3.2.7 on 2021-09-11 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ztest_ztest1', '0003_hostdetails_vendorname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostdetails',
            name='secret',
        ),
    ]