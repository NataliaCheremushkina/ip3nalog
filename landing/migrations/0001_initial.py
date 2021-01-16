# Generated by Django 3.1.5 on 2021-01-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sorting', models.PositiveIntegerField(default=999)),
                ('block_title', models.CharField(max_length=250)),
                ('title', models.CharField(blank=True, max_length=250)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='uploads/')),
                ('status', models.CharField(choices=[('visible', 'Visible'), ('invisible', 'Invisible')], default='invisible', max_length=10)),
                ('menu_status', models.CharField(choices=[('visible', 'Visible'), ('invisible', 'Invisible')], default='invisible', max_length=10)),
            ],
        ),
    ]
