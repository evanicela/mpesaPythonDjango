# Generated by Django 4.1.7 on 2023-03-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoename', models.CharField(db_column='shoename', max_length=100)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('price', models.CharField(db_column='price', max_length=100)),
                ('imageurl', models.CharField(db_column='imageurl', max_length=1000)),
            ],
            options={
                'verbose_name': 'Shoe',
                'verbose_name_plural': 'Shoes',
                'db_table': 'shoe',
            },
        ),
    ]