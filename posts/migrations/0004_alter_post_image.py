# Generated by Django 3.2.16 on 2022-11-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../m3efn2fnj5y2syaro1lk', upload_to='images/'),
        ),
    ]
