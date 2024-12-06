# Generated by Django 5.1.2 on 2024-12-06 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_duration_mins_event_duration_hrs'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecurringEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.event')),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
            ],
            bases=('accounts.event',),
        ),
        migrations.AlterField(
            model_name='account',
            name='sleep_end',
            field=models.IntegerField(default=8),
        ),
    ]