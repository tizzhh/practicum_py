# Generated by Django 4.2.7 on 2023-11-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ice_cream", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "verbose_name": "категорию",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterModelOptions(
            name="wrapper",
            options={
                "verbose_name": "обёртку",
                "verbose_name_plural": "Обёртки",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                max_length=64, unique=True, verbose_name="Слаг"
            ),
        ),
        migrations.AlterField(
            model_name="topping",
            name="slug",
            field=models.SlugField(
                max_length=64, unique=True, verbose_name="Слаг"
            ),
        ),
        migrations.AlterField(
            model_name="wrapper",
            name="title",
            field=models.CharField(
                help_text="Уникальное название обёртки, не более 256 символов",
                max_length=256,
                verbose_name="Название",
            ),
        ),
    ]
