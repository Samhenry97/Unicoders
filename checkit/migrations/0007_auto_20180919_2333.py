# Generated by Django 2.1.1 on 2018-09-19 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkit', '0006_auto_20180919_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='checkit.Company'),
        ),
        migrations.AddField(
            model_name='company',
            name='desc',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
