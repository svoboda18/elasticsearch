# Generated by Django 5.0 on 2023-12-31 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
