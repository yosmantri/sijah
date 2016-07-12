# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class JamuAppCompound(models.Model):
    compound_id = models.AutoField(primary_key=True)
    knapsack_code = models.CharField(max_length=20, blank=True, null=True)
    cas_id = models.CharField(max_length=15, blank=True, null=True)
    compound_name = models.CharField(max_length=100, blank=True, null=True)
    molecular_formula = models.CharField(max_length=50, blank=True, null=True)
    molecular_weight = models.DecimalField(max_digits=12, decimal_places=8, blank=True, null=True)
    pubchem_cid = models.CharField(max_length=15, blank=True, null=True)
    smiles = models.CharField(max_length=100, blank=True, null=True)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_compound'


class JamuAppCompoundProtein(models.Model):
    compound = models.ForeignKey(JamuAppCompound, models.DO_NOTHING)
    protein = models.ForeignKey('JamuAppProtein', models.DO_NOTHING)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_compound_protein'


class JamuAppDisease(models.Model):
    disease_id = models.AutoField(primary_key=True)
    disease_name_en = models.CharField(max_length=100, blank=True, null=True)
    disease_name_id = models.CharField(max_length=100, blank=True, null=True)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_disease'


class JamuAppPlant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    plant_name_en = models.CharField(max_length=30, blank=True, null=True)
    plant_name_id = models.CharField(max_length=30, blank=True, null=True)
    latin_name = models.CharField(max_length=100, blank=True, null=True)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_plant'


class JamuAppPlantCompound(models.Model):
    plant = models.ForeignKey(JamuAppPlant, models.DO_NOTHING)
    compound = models.ForeignKey(JamuAppCompound, models.DO_NOTHING)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_plant_compound'


class JamuAppProtein(models.Model):
    protein_id = models.AutoField(primary_key=True)
    protein_code = models.CharField(max_length=20, blank=True, null=True)
    protein_name = models.CharField(max_length=100, blank=True, null=True)
    gi_number = models.CharField(max_length=15, blank=True, null=True)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_protein'
