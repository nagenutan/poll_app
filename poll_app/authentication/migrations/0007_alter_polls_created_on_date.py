# Generated by Django 4.1.1 on 2022-09-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_polls_remove_usersdetails_opt1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='created_on_date',
            field=models.DateTimeField(auto_now_add=True, max_length=30),
        ),
    ]
