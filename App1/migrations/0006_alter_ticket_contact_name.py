# Generated by Django 4.0.4 on 2022-05-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_alter_login_email_alter_login_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Contact_Name',
            field=models.CharField(max_length=100),
        ),
    ]
