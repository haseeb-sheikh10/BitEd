# Generated by Django 4.1.7 on 2023-04-04 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('folder', '0006_alter_tile_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='questions',
            field=models.ManyToManyField(blank=True, to='questions.question'),
        ),
    ]