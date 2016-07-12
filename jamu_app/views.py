from django.shortcuts import HttpResponseRedirect, render
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from .models import Penyakit, Tanaman
from .models import JamuAppCompound, JamuAppPlant, JamuAppProtein, JamuAppCompoundProtein, JamuAppPlantCompound

# from .forms import InputForm
from .forms import SearchForm, SearchFormAjax

def index(request):
	return render(request, 'jamu_app/index.html')


# def input(request):
# 	# list_penyakit = Penyakit.objects.order_by('nama_penyakit')
# 	# list_tanaman = Tanaman.objects.order_by('nama_tanaman')
# 	# context = {'list_penyakit': list_penyakit, 'list_tanaman': list_tanaman}
# 	# return render(request, 'jamu_app/input.html', context)

# 	if request.method == "POST":
# 		form = InputForm(request.POST)
# 		if form.is_valid():
# 			penyakit = form.cleaned_data['list_penyakit']
# 			tanaman = []
# 			tanaman.append(form.cleaned_data['list_tanaman_1'])
# 			tanaman.append(form.cleaned_data['list_tanaman_2'])
# 			tanaman.append(form.cleaned_data['list_tanaman_3'])
# 			tanaman.append(form.cleaned_data['list_tanaman_4'])
# 			list_tanaman = list(set(tanaman))
# 			# return render(request, 'jamu_app/showdebug.html', {'showdebug': tanamans})
# 			list_senyawa_sb = form.get_data_senyawa('1')
# 			list_senyawa_pr = form.get_data_senyawa('2')
# 			list_senyawa_bw = form.get_data_senyawa('3')
# 			list_senyawa_jh = form.get_data_senyawa('4')
# 			list_protein = form.get_data_protein(penyakit)

# 			# return render(request, 'jamu_app/showdebug.html', {'showdebug': tanamans})


def search(request):
	if 'list_disease' in request.GET and 'list_plant_1' in request.GET and 'list_plant_2' in request.GET and 'list_plant_3' in request.GET and 'list_plant_4' in request.GET:
		# insert action to do if the data is completed here
		form = request.GET
		plant = []
		list_plant_compound = []
		list_compound = []
		list_compound_protein = []
		list_protein = []
		plant.append(form['list_plant_1'])
		plant.append(form['list_plant_2'])
		plant.append(form['list_plant_3'])
		plant.append(form['list_plant_4'])
		plant = list(set(plant))
		list_plant = JamuAppPlant.objects.filter(plant_id__in=set(plant))
		for pl in list_plant:
			plant_comp = JamuAppPlantCompound.objects.filter(plant_id=pl).select_related()
			comps = plant_comp.values_list('compound_id', flat=True)
			lst_comp = JamuAppCompound.objects.filter(compound_id__in=set(comps))
			list_compound.append(lst_comp)
			list_plant_compound.append(plant_comp)
		for pl in list_compound:
			for comp in pl:
				comp_prot = JamuAppCompoundProtein.objects.filter(compound_id=comp).select_related()[:1]
				prots = comp_prot.values_list('protein_id', flat=True)
				lst_prot = JamuAppProtein.objects.filter(protein_id__in=set(prots))
				list_protein.append(lst_prot)
				list_compound_protein.append(comp_prot)
		# return render(request, 'jamu_app/showdebug.html', {'showdebug': list_compound_protein})
		return render(request, 'jamu_app/search_result.html', {'list_plant': list_plant, 'list_compound': list_compound, 'list_protein': list_protein, 'list_plant_compound': list_plant_compound, 'list_compound_protein': list_compound_protein})
	elif 'list_disease' in request.GET or 'list_plant_1' in request.GET or 'list_plant_2' in request.GET or 'list_plant_3' in request.GET or 'list_plant_4' in request.GET:
		form = SearchForm(request.GET)
	else:
		form = SearchForm()
	# return render(request, 'jamu_app/showdebug.html', {'showdebug': request.GET})
	return render(request, 'jamu_app/search.html', {'form': form})

# def get_list(request):
# 	# if request.method == "POST":
# 	# 	form = InputForm(request.POST)
# 	# 	if form.is_valid():
# 	penyakit = form.cleaned_data['list_penyakit']
# 	tanaman = form.cleaned_data['list_tanaman']
# 	list_senyawa = form.get_data_senyawa(tanaman)
# 	list_protein = form.get_data_protein(penyakit)

# 	paginator_senyawa = Paginator(list_senyawa, 10)
# 	page = request.GET.get('page')
# 	try:
# 		lstsenyawa = paginator_senyawa.page(page)
# 	except PageNotAnInteger:
# 		lstsenyawa = paginator_senyawa.page(1)
# 	except EmptyPage:
# 		lstsenyawa = paginator_senyawa.page(paginator_senyawa.num_pages)

# 	return render(request, 'jamu_app/get_list.html', {'list_senyawa': list_senyawa, 'list_protein': list_protein, 'lstsenyawa': lstsenyawa, 'penyakit': penyakit, 'tanaman': tanaman})

def search_ajax(request):
	form = SearchFormAjax()
	return render(request, 'jamu_app/search_ajax.html', {'form': form})