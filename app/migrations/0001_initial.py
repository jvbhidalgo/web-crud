# Generated by Django 3.0.5 on 2020-04-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(blank=True, max_length=1000)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
