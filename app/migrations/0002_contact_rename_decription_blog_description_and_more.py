# Generated by Django 4.1.7 on 2023-03-05 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('is_solved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='decription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='is_puplished',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='Blog'),
        ),
    ]
