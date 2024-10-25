# Generated by Django 5.0.1 on 2024-10-24 20:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_gateway', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForDelete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_plan', to='pay_gateway.plan'),
        ),
    ]
