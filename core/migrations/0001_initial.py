# Generated by Django 3.1.3 on 2020-11-12 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('location', models.TextField()),
                ('about', models.CharField(max_length=500)),
                ('details', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField()),
                ('gender', models.CharField(choices=[['M', 'Male'], ['F', 'Female']], max_length=1)),
                ('symptoms', models.TextField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[['M', 'Male'], ['F', 'Female']], max_length=1)),
                ('specialization', models.CharField(max_length=300)),
                ('qualification', models.CharField(max_length=300)),
                ('language', models.CharField(max_length=300)),
                ('experience', models.IntegerField()),
                ('about', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='media/profile_pic')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('normal_charges', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.hospital')),
            ],
        ),
    ]
