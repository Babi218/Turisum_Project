# Generated by Django 4.2.18 on 2025-03-26 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_contact_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='DOB',
        ),
    ]
