# Generated by Django 4.2 on 2023-05-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherView', '0002_alter_chemicals_name_alter_equipment_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='steps',
            name='step',
            field=models.TextField(blank=True, null=True),
        ),
    ]
