# Generated by Django 4.1.3 on 2022-11-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FCDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finalCost', models.DecimalField(decimal_places=2, default=0, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='FHCDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('tempWorkerHiringCost', models.DecimalField(decimal_places=2, max_digits=19)),
                ('tempWorkerFiringCost', models.DecimalField(decimal_places=2, max_digits=19)),
                ('tempWorkerHired', models.IntegerField()),
                ('tempWorkerFired', models.IntegerField()),
                ('hiringCost', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
                ('firingCost', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IHCDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('holdingCostPerUnit', models.DecimalField(decimal_places=2, max_digits=19)),
                ('unitsOfEndingInventory', models.IntegerField()),
                ('inventoryHoldingCost', models.DecimalField(decimal_places=2, max_digits=19, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RDDatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField()),
                ('demand', models.IntegerField()),
                ('productionPermanentWorker', models.IntegerField()),
                ('numPermanentWorker', models.IntegerField()),
                ('remainingDemand', models.IntegerField(null=True)),
            ],
        ),
    ]
