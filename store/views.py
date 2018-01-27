from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'store/index.html')


def product(request):
    if 'brie' in request.POST:
        title = "Brie"
        context = {'title': title}
        return render(request, 'store/product.html', context)

    elif 'conjured' in request.POST:
        title = "conjured"
        context = {'title': title}
        return render(request, 'store/product.html', context)

    elif 'backstage_passes' in request.POST:
        title = "backstage_passes"
        context = {'title': title}
        return render(request, 'store/product.html', context)

    elif 'sulfuras' in request.POST:
        title = "sulfuras"
        context = {'title': title}
        return render(request, 'store/product.html', context)
