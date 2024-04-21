# Generated by Django 5.0.4 on 2024-04-21 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=100)),
                ('icone', models.ImageField(blank=True, null=True, upload_to='icones')),
            ],
        ),
    ]
