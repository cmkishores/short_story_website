# Generated by Django 2.2.5 on 2019-09-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('release_year', models.CharField(max_length=4)),
                ('genre', models.TextField(choices=[('CD', 'Comedy'), ('AC', 'Action'), ('DR', 'Drama'), ('HR', 'Horror'), ('KD', 'Kids'), ('MY', 'Mythology')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cover', models.ImageField(blank=True, upload_to='cover/')),
                ('story', models.TextField()),
            ],
            options={
                'verbose_name': 'Stories',
                'permissions': [('prime_member', 'Can read the stories')],
            },
        ),
    ]
