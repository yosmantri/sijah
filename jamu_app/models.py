from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# class Penyakit(models.Model):
#     id_penyakit = models.AutoField(primary_key=True)
#     nama_penyakit = models.CharField(max_length=100)
#     update_oleh = models.CharField(max_length=50, default='admin')
#     update_pada = models.DateTimeField(default=datetime.now)
#     def __str__(self):
#         return self.nama_penyakit

# class Tanaman(models.Model):
#     id_tanaman = models.AutoField(primary_key=True)
#     nama_tanaman = models.CharField(max_length=20)
#     nama_latin = models.CharField(max_length=100, null=True)
#     update_oleh = models.CharField(max_length=50, default='admin')
#     update_pada = models.DateTimeField(default=datetime.now)
#     def __str__(self):
#         return self.nama_tanaman

# class Protein(models.Model):
#     id_protein = models.AutoField(primary_key=True)
#     kode_protein = models.CharField(max_length=20)
#     nama_protein = models.CharField(max_length=100)
#     id_penyakit = models.ForeignKey(Penyakit, on_delete=models.CASCADE)
#     update_oleh = models.CharField(max_length=50, default='admin')
#     update_pada = models.DateTimeField(default=datetime.now)
#     def __str__(self):
#         return self.nama_protein

# class Senyawa(models.Model):
#     id_senyawa = models.AutoField(primary_key=True)
#     kode_senyawa = models.CharField(max_length=20)
#     nama_senyawa = models.CharField(max_length=100)
#     rumus_molekul = models.CharField(max_length=50, null=True)
#     id_tanaman = models.ForeignKey(Tanaman, on_delete=models.CASCADE)
#     CID_pubchem = models.CharField(max_length=15, null=True)
#     update_oleh = models.CharField(max_length=50, default='admin')
#     update_pada = models.DateTimeField(default=datetime.now)
#     def __str__(self):
#         return self.nama_senyawa

### main tables
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

    def __str__(self):
        return self.compound_name


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

    def __str__(self):
        return self.disease_name_en


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

    def __str__(self):
        return self.latin_name


class JamuAppProtein(models.Model):
    protein_id = models.AutoField(primary_key=True)
    protein_code = models.CharField(max_length=20, blank=True, null=True)
    protein_name = models.CharField(max_length=100, blank=True, null=True)
    gene_name = models.CharField(max_length=50, blank=True, null=True)
    gi_number = models.CharField(max_length=15, blank=True, null=True)
    organism = models.CharField(max_length=100, blank=True, null=True)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_protein'

    def __str__(self):
        return self.gi_number


### transaction table
class JamuAppCompoundProtein(models.Model):
    compound = models.ForeignKey(JamuAppCompound, models.DO_NOTHING)
    protein = models.ForeignKey(JamuAppProtein, models.DO_NOTHING)
    added_by = models.CharField(max_length=50)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=50)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'jamu_app_compound_protein'


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

