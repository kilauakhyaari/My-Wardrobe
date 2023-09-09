from django.shortcuts import render

def show_main(request):
    context = {
        'app': 'My Wardrobe',
        'name': 'Pak Bepe',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
