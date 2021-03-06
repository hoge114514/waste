# Generated by Django 2.1.2 on 2019-12-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191210_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='sample_7',
            new_name='deadline',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='sample_2',
            new_name='memo',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='sample_3',
            new_name='quontity',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='sample_9',
            new_name='vegetable',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_6',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.AddField(
            model_name='item',
            name='F_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='施設名'),
        ),
        migrations.AddField(
            model_name='item',
            name='I_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='入力者氏名'),
        ),
    ]
