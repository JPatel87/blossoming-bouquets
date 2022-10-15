# Generated by Django 3.2 on 2022-10-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('Bouquets', 'Bouquets'), ('Order', 'Order'), ('Delivery', 'Delivery'), ('Account', 'Account'), ('Other', 'Other')], default='Bouquets', max_length=20),
        ),
    ]
