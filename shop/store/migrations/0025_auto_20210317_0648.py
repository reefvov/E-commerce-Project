# Generated by Django 3.1.7 on 2021-03-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_auto_20210317_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('รอชำระเงิน', 'รอชำระเงิน'), ('ชำระเงินแล้ว-รอตรวจสอบ', 'ชำระเงินแล้ว-รอตรวจสอบ'), ('กำลังจัดส่ง', 'กำลังจัดส่ง'), ('จัดส่งสินค้าแล้ว', 'จัดส่งสินค้าแล้ว')], max_length=255),
        ),
    ]
