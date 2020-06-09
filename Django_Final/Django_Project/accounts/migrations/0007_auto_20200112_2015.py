# Generated by Django 3.0.2 on 2020-01-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200112_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size_inches',
            field=models.CharField(choices=[(' ', '  '), ('7 inches ', '7 inches '), ('9 inches ', '9 inches ')], max_length=10, null=True),
        ),
    ]
