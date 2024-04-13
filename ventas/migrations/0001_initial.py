# Generated by Django 4.1.1 on 2024-06-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provincia', models.CharField(choices=[('San José', 'San José'), ('Alajuela', 'Alajuela'), ('Cartago', 'Cartago'), ('Heredia', 'Heredia'), ('Guanacaste', 'Guanacaste'), ('Puntarenas', 'Puntarenas'), ('Limón', 'Limón')], max_length=20)),
                ('distrito', models.CharField(max_length=100)),
                ('cliente', models.CharField(max_length=100)),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField()),
                ('duracion', models.IntegerField()),
                ('color', models.CharField(choices=[('Azul', 'Azul'), ('Rojo', 'Rojo'), ('Verde', 'Verde'), ('Amarillo', 'Amarillo'), ('Naranja', 'Naranja'), ('Morado', 'Morado'), ('Rosa', 'Rosa'), ('Marrón', 'Marrón'), ('Negro', 'Negro'), ('Blanco', 'Blanco')], max_length=20)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('iva', models.BooleanField(default=False)),
                ('descripcion', models.TextField()),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.URLField()),
            ],
        ),
    ]