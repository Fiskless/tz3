# Generated by Django 3.0.7 on 2021-04-23 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('human', '0001_initial'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='human',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match', to='human.Human'),
        ),
    ]
