# Generated by Django 3.0.7 on 2021-04-22 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('MAN', 'Man'), ('WOMAN', 'Woman')], max_length=5)),
            ],
            options={
                'verbose_name': 'пара',
                'verbose_name_plural': 'пары',
            },
        ),
    ]
