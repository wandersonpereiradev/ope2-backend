# Generated by Django 3.2.6 on 2021-09-07 17:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('funcao', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=255)),
                ('senha', models.IntegerField()),
                ('is_admin', models.CharField(max_length=255)),
            ],
        ),
    ]
