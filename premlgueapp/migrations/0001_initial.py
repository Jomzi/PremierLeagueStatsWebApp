# Generated by Django 3.0 on 2019-12-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=100)),
                ('matches_played', models.IntegerField()),
                ('wins', models.IntegerField()),
                ('draws', models.IntegerField()),
                ('losses', models.IntegerField()),
                ('league_position', models.IntegerField()),
                ('goals_scored', models.IntegerField()),
                ('goals_conceded', models.IntegerField()),
                ('goal_difference', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
            options={
                'db_table': 'overview',
            },
        ),
    ]
