# Generated by Django 4.1.3 on 2022-11-30 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(choices=[('bento_goncalves', 'Bento Gonçalves'), ('bonito', 'Bonito')], max_length=255)),
            ],
        ),
    ]