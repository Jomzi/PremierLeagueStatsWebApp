# Generated by Django 3.0 on 2019-12-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('premlgueapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='id',
        ),
        migrations.AlterField(
            model_name='overview',
            name='team_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]