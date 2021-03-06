# Generated by Django 2.1.3 on 2018-11-27 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipo_de_documento', models.CharField(max_length=50)),
                ('numero_de_documento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.IntegerField()),
                ('numero', models.CharField(max_length=6)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('tipo_de_documento', models.CharField(max_length=50)),
                ('numero_de_documento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='No title', max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('producto', models.ImageField(upload_to='producto/')),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('favorite', models.BooleanField(default=False)),
                ('descripcion', models.CharField(blank=True, max_length=200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='id_mesero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Mesero'),
        ),
    ]
