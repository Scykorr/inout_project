# Generated by Django 5.0.1 on 2024-10-24 20:41

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay_gateway', '0002_fordelete_alter_user_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addon',
            old_name='price',
            new_name='price_per_user',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='price',
            new_name='price_per_user',
        ),
        migrations.AddField(
            model_name='addon',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_count', models.PositiveIntegerField(default=5)),
                ('addons', models.ManyToManyField(to='pay_gateway.addon')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay_gateway.plan')),
            ],
        ),
    ]
