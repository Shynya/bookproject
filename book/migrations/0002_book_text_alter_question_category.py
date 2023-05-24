# Generated by Django 4.1.5 on 2023-04-09 14:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='text',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('JAVA', 'JAVA'), ('Linux', 'Linux'), ('Python', 'Python'), ('Python(Django)', 'Python(Django)'), ('Python(Machine Learning)', 'Python(機械学習)'), ('Javascript', 'Javascript'), ('Javascript(Vue.js)', 'Javascript(vue.js)'), ('PHP', 'PHP'), ('Access VBA', 'Access VBA'), ('Excel VBA', 'Excel VBA'), ('statistics', '統計学'), ('trivia', '雑学'), ('other', 'その他')], max_length=100),
        ),
    ]