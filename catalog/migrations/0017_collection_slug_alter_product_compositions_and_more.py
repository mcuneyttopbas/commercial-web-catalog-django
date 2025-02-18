# Generated by Django 4.0.2 on 2022-03-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_collection_is_active_collection_is_contract_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='compositions',
            field=models.ManyToManyField(to='catalog.Composition'),
        ),
        migrations.AlterField(
            model_name='product',
            name='usages',
            field=models.ManyToManyField(to='catalog.Usage'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(),
        ),
    ]
