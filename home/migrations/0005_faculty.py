# Generated by Django 4.0.4 on 2022-07-21 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_curriculum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_no', models.CharField(max_length=10)),
                ('f_code', models.CharField(max_length=10)),
                ('f_fullname', models.CharField(max_length=100)),
                ('f_username', models.CharField(max_length=100)),
                ('f_password', models.CharField(max_length=100)),
            ],
        ),
    ]