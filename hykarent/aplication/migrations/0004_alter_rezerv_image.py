# Generated by Django 5.2.1 on 2025-05-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0003_alter_rezerv_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezerv',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
