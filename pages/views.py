from django.shortcuts import render

# Create your views here.
def home(request):
	name = "Welcome"
	return render(request, "home.html", {"name": name})

def about(request):
	from pages.namer import namer
	return render(request, "about.html", {"my_stuff": namer})

def contact(request):
	from pages.models import badella
	return render(request, "contact.html", {"badella": badella})

def contact_lg(request):
	return render(request, "contact_lokeshg.html", {})

def contact_lb(request):
	return render(request, "contact_lokeshb.html", {})

def contact_n(request):
	return render(request, "contact_nithin.html", {})

