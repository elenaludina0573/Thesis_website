# Generated by Django 5.0.7 on 2024-07-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя доктора')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество доктора')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия доктора')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('specialization', models.CharField(max_length=255, verbose_name='Специализация')),
                ('qualification', models.CharField(max_length=255, verbose_name='Квалификация')),
                ('experience', models.PositiveIntegerField(verbose_name='Опыт работы в летах')),
            ],
            options={
                'verbose_name': 'доктор',
                'verbose_name_plural': 'доктора',
            },
        ),
    ]
