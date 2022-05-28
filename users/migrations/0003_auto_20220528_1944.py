# Generated by Django 2.2.16 on 2022-05-28 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20220528_1944'),
        ('organizations', '0004_auto_20220528_1944'),
        ('users', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Направления',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar_url',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='users/avatars/profile.png', upload_to=users.models.User.user_avatar_path, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='UserDirection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Direction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserDirection',
                'verbose_name_plural': 'UserDirection',
            },
        ),
        migrations.CreateModel(
            name='ReviewUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Отзыв')),
                ('rating', models.FloatField(verbose_name='Рейтинг')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_user', to='events.Event', verbose_name='Мероприятие')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_user', to='organizations.Organization', verbose_name='Организация')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_user', to=settings.AUTH_USER_MODEL, verbose_name='Волонтер')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256, verbose_name='Сертификат URL')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Сертификаты',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='direction',
            field=models.ManyToManyField(related_name='users_direction', through='users.UserDirection', to='users.Direction', verbose_name='Направления'),
        ),
    ]
