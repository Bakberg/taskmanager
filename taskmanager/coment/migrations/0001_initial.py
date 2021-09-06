# Generated by Django 3.2.6 on 2021-09-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, verbose_name='Вопрос')),
                ('task', models.TextField(blank=True, verbose_name='ответь')),
                ('is_pblished', models.BooleanField(default=False, verbose_name='Публирован')),
            ],
            options={
                'verbose_name': 'Вопрос-ответь',
                'verbose_name_plural': 'Вопрос-ответь',
            },
        ),
    ]