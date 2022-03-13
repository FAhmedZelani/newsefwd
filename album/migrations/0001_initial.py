# Generated by Django 4.0.2 on 2022-02-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('short_description', models.TextField()),
                ('image', models.ImageField(upload_to='carousel/')),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]