from django.shortcuts import render

# Create your views here.

def index(request):
    pokemon = ["Rayquaza", "Groudon", "Kyogre", "Mewtwo", "Mew"]
    return render(request, "index.html", {"pokemon": pokemon})
    
    
def pokemon_details(request, pokemon):
    return render(request, "details.html", {"pokemon": pokemon})