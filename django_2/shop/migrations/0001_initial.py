# Generated by Django 4.2.2 on 2023-06-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('prodect_desc', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
