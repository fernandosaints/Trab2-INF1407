# Generated by Django 3.2.9 on 2021-11-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='creator',
            field=models.CharField(default=1, editable=False, max_length=30, verbose_name='Creator'),
            preserve_default=False,
        ),
    ]
