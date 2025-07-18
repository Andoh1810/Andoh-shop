# Generated by Django 4.2 on 2025-04-23 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catégorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagesCategories')),
                ('feminin', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('prix', models.IntegerField()),
                ('quantite_stock', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='imagesArticles')),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='site_app.catégorie')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='site_app.type')),
            ],
        ),
    ]
