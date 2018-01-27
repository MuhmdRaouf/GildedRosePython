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
        sellin = "conjured"
        context = {
            'title': title,
            'title2': title,
        }
        return render(request, 'store/product.html', context)

    elif 'backstage_passes' in request.POST:
        title = "backstage_passes"
        context = {'title': title}
        return render(request, 'store/product.html', context)

    elif 'sulfuras' in request.POST:
        title = "sulfuras"
        context = {'title': title}
        return render(request, 'store/product.html', context)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1
                    item.sell_in -= 1

            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in in range(6, 11):
                    if item.quality < 50:
                        item.quality = item.quality + 2
                elif item.sell_in in range(0, 6):
                    if item.quality < 50:
                        item.quality = item.quality + 3
                else:
                    item.quality = 0

                item.sell_in -= 1



            elif item.name == "Conjured":
                if item.quality < 50:
                    item.quality -= 2
                    item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
