# Generated by Django 2.1.5 on 2019-03-25 12:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_answer_is_attempted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('description', models.TextField(blank=True, help_text='a description of the quiz', verbose_name='Description')),
                ('url', models.SlugField(help_text='a user friendly url', max_length=60, verbose_name='user friendly url')),
                ('random_order', models.BooleanField(default=False, help_text='Display the questions in a random order or as they are set?', verbose_name='Random Order')),
                ('answers_at_end', models.BooleanField(default=False, help_text='Correct answer is NOT shown after question. Answers displayed at the end.', verbose_name='Answers at end')),
                ('exam_paper', models.BooleanField(default=False, help_text='If yes, the result of each attempt by a user will be stored. Necessary for marking.', verbose_name='Exam Paper')),
                ('single_attempt', models.BooleanField(default=False, help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.', verbose_name='Single Attempt')),
                ('draft', models.BooleanField(blank=True, default=False, help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.', verbose_name='Draft')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['category'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='ques_image',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ques_link',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ques_text',
        ),
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.CharField(default=django.utils.timezone.now, help_text='Enter the question text that you want displayed', max_length=1000, verbose_name='Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, help_text='Explanation to be shown after the question has been answered.', max_length=2000, verbose_name='Explanation'),
        ),
        migrations.AddField(
            model_name='question',
            name='figure',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Figure'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Category', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(blank=True, to='quiz.Quiz', verbose_name='Quiz'),
        ),
    ]