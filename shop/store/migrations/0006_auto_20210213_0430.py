# Generated by Django 3.1.5 on 2021-02-12 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210213_0405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'หมวดหมู่', 'verbose_name_plural': 'ข้อมูลประเภทสินค้า'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
