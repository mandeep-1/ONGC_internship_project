# Generated by Django 3.0.7 on 2020-07-07 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_ongc', '0004_auto_20200701_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='bletter',
            field=models.FileField(default='', upload_to='media/Bonafied_Letter'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='lmarksheet',
            field=models.FileField(default='', upload_to='media/Latest_Marksheet'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='marksheet12',
            field=models.FileField(default='', upload_to='media/Marksheet_12'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='photograph',
            field=models.ImageField(default='', upload_to='media/Photograph'),
        ),
    ]
