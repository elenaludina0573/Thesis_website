# Generated by Django 4.2.13 on 2024-08-11 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_alter_client_options_alter_record_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnostics',
            options={'permissions': [('can_view_diagnostics', 'Может просматривать диагностики')], 'verbose_name': 'диагностика', 'verbose_name_plural': 'диагностики'},
        ),
    ]
