# Generated by Django 4.0.2 on 2022-02-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xit', '0004_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('short_description', models.TextField()),
                ('image', models.ImageField(upload_to='award/')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner/')),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services/'),
        ),
    ]
