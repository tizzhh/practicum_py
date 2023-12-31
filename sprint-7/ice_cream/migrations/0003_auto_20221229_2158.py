# Generated by Django 3.2.16 on 2022-12-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ice_cream', '0002_auto_20221229_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='output_order',
            field=models.PositiveSmallIntegerField(
                default=100, verbose_name='Порядок отображения'
            ),
        ),
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=5
            ),
            preserve_default=False,
        ),
    ]
