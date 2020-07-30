# Generated by Django 3.0.6 on 2020-06-08 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20200603_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='ippool',
            name='owner',
            field=models.CharField(db_index=True, default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
    ]
