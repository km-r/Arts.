# Generated by Django 3.1.4 on 2021-01-06 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0004_auto_20210106_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='Events',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arts.events'),
        ),
    ]