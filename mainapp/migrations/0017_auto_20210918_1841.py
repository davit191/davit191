# Generated by Django 3.1.4 on 2021-09-18 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20210918_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_contact',
            name='gmail',
            field=models.CharField(default=1, max_length=12, verbose_name='ոսահամար'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data_contact',
            name='mail',
            field=models.CharField(default=2, max_length=12, verbose_name='հեռաամար'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data_contact',
            name='name',
            field=models.CharField(choices=[('@mail', '@mail'), ('num', 'num'), ('gmail', 'gmail')], max_length=20, verbose_name=''),
        ),
    ]
