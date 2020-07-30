# Generated by Django 3.0.6 on 2020-06-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_ippool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ip',
        ),
        migrations.AddField(
            model_name='host',
            name='ExtranetDNS',
            field=models.CharField(default='218.3.5.153', max_length=20),
        ),
        migrations.AddField(
            model_name='host',
            name='ExtranetGateWay',
            field=models.CharField(default='192.168.1.1', max_length=20),
        ),
        migrations.AddField(
            model_name='host',
            name='ExtranetIp',
            field=models.GenericIPAddressField(db_index=True, default='192.168.1.248'),
        ),
        migrations.AddField(
            model_name='host',
            name='ExtranetNetMask',
            field=models.CharField(default='255.255.255.0', max_length=20),
        ),
        migrations.AddField(
            model_name='host',
            name='IntraneDNS',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='IntraneGateWay',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='IntranetIp',
            field=models.GenericIPAddressField(db_index=True, default='172.0.0.248'),
        ),
        migrations.AddField(
            model_name='host',
            name='IntranetNetMask',
            field=models.CharField(default='255.255.255.0', max_length=20),
        ),
        migrations.AddField(
            model_name='host',
            name='manufacturer',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='host',
            name='password',
            field=models.CharField(default='123123', max_length=32),
        ),
        migrations.AddField(
            model_name='host',
            name='username',
            field=models.CharField(default='administrator', max_length=32),
        ),
    ]
