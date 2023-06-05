# Generated by Django 4.0.5 on 2023-06-02 07:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlepost',
            options={'ordering': ('-updated',)},
        ),
        migrations.AlterIndexTogether(
            name='articlepost',
            index_together=set(),
        ),
        migrations.AddField(
            model_name='articlepost',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='articlepost',
            index_together={('id', 'slug')},
        ),
        migrations.RemoveField(
            model_name='articlepost',
            name='slug1',
        ),
    ]
