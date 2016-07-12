from django import forms

# from .models import Penyakit, Protein, Tanaman, Senyawa
from .models import JamuAppCompound, JamuAppDisease, JamuAppPlant, JamuAppProtein

# class InputForm(forms.Form):
# 	list_penyakit = forms.ModelChoiceField(queryset=Penyakit.objects.all())
# 	list_tanaman_1 = forms.ModelChoiceField(queryset=Tanaman.objects.all())
# 	list_tanaman_2 = forms.ModelChoiceField(queryset=Tanaman.objects.all())
# 	list_tanaman_3 = forms.ModelChoiceField(queryset=Tanaman.objects.all())
# 	list_tanaman_4 = forms.ModelChoiceField(queryset=Tanaman.objects.all())

# 	def get_data_senyawa(self, tanaman):
# 		# cleaned_data = self.cleaned_data
# 		list_senyawa = Senyawa.objects.filter(id_tanaman=tanaman).values()
# 		return list_senyawa
# 	def get_data_protein(self, penyakit):
# 		list_protein = Protein.objects.filter(id_penyakit=penyakit).values()
# 		return list_protein

class SearchForm(forms.Form):
	list_disease = forms.ModelChoiceField(queryset=JamuAppDisease.objects.all())
	list_plant_1 = forms.ModelChoiceField(queryset=JamuAppPlant.objects.all().order_by('latin_name').values())
	list_plant_2 = forms.ModelChoiceField(queryset=JamuAppPlant.objects.all().order_by('latin_name').values())
	list_plant_3 = forms.ModelChoiceField(queryset=JamuAppPlant.objects.all().order_by('latin_name').values())
	list_plant_4 = forms.ModelChoiceField(queryset=JamuAppPlant.objects.all().order_by('latin_name').values())

class SearchFormAjax(forms.Form):
	listDisease = forms.ModelChoiceField(queryset=JamuAppDisease.objects.all())
	listProtein = forms.ModelChoiceField(queryset=JamuAppProtein.objects.filter(organism='Homo sapiens').order_by('protein_name').values())
	listCompound = forms.ModelChoiceField(queryset=JamuAppCompound.objects.all().order_by('compound_name').values())
	listPlant = forms.ModelChoiceField(queryset=JamuAppPlant.objects.all().order_by('latin_name').values())
