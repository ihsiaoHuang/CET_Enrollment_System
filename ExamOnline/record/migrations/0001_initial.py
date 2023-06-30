# Generated by Django 3.0.3 on 2020-04-24 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
        ('user', '0001_initial'),
        ('exam', '0007_delete_recode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='你的作答')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='练习')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Program', verbose_name='编程题')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '编程题答题记录',
                'verbose_name_plural': '编程题答题记录',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='JudgeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='你的作答')),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Judge', verbose_name='判断题')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='练习')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '判断题答题记录',
                'verbose_name_plural': '判断题答题记录',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='FillRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='你的作答')),
                ('fill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Fill', verbose_name='填空题')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='练习')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '填空题答题记录',
                'verbose_name_plural': '填空题答题记录',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ChoiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='你的作答')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Choice', verbose_name='选择题')),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Practice', verbose_name='练习')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Student', verbose_name='学生')),
            ],
            options={
                'verbose_name': '选择题答题记录',
                'verbose_name_plural': '选择题答题记录',
                'ordering': ['id'],
            },
        ),
    ]
