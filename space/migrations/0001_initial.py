# Generated by Django 4.2.6 on 2023-11-17 10:31

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(blank=True, choices=[('Lightweight – up to 5 tons of payload', 'Light'), ('Medium - from 5 to 20 tons', 'Medium'), ('Heavy – from 20 to 100 tons', 'Heavy'), ('Super heavy – over 100 tons', 'Super heavy')], max_length=50, null=True)),
                ('fuel_condition', models.CharField(blank=True, choices=[('Solid rocket engine', 'SRE'), ('Liquid rocket engine', 'Liquid rocket engine'), ('Hybrid', 'Hybrid')], max_length=50, null=True)),
                ('stages', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='rockets')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
