# Generated by Django 3.0.3 on 2020-04-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200425_2103'),
        ('exam', '0009_auto_20200425_1959'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clazz',
        ),
        migrations.AlterField(
            model_name='exam',
            name='clazzs',
            field=models.ManyToManyField(to='user.Clazz', verbose_name='参加考试的班级'),
        ),
    ]
