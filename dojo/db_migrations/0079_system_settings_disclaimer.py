# Generated by Django 2.2.17 on 2021-02-23 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0078_cvssv3_rename_verbose_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='system_settings',
            name='disclaimer',
            field=models.TextField(blank=True, default='', help_text='Include this custom disclaimer on all notifications and generated reports', max_length=3000, verbose_name='Custom Disclaimer'),
        ),
    ]