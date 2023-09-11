from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'My Wardrobe',
        'name': 'Kilau Nisrina Akhyaari',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
