# Generated by Django 3.0.7 on 2020-07-07 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_ongc', '0005_auto_20200707_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='bletter',
            field=models.FileField(default='', upload_to='Bonafied_Letter'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='lmarksheet',
            field=models.FileField(default='', upload_to='Latest_Marksheet'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='marksheet12',
            field=models.FileField(default='', upload_to='Marksheet_12'),
        ),
        migrations.AlterField(
            model_name='regform',
            name='photograph',
            field=models.ImageField(default='', upload_to='Photograph'),
        ),
    ]
