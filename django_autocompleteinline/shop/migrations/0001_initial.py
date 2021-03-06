# Generated by Django 2.0.1 on 2018-01-25 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nom')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prix')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nom')),
            ],
            options={
                'verbose_name': 'Magasin',
                'verbose_name_plural': 'Magasins',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Prix spécifique à ce magasin')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product', verbose_name='Produit')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop', verbose_name='Magasin')),
            ],
            options={
                'verbose_name': 'Produit du Magasin',
                'verbose_name_plural': 'Produits du Magasin',
            },
        ),
        migrations.AlterUniqueTogether(
            name='shopproduct',
            unique_together={('product', 'shop')},
        ),
    ]
