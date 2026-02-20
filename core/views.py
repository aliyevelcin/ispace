from urllib import request
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
from django.http import Http404
from core.forms import EmailForm
def home(request):
    news = News.objects.all()
    sliders = Slider.objects.all()
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.order_by('-id')[:4]
    accessories = Accessories.objects.all()
    tv_homes = Tv_Home.objects.all()
    airpodss = Airpods.objects.all()
    watches = Watch.objects.all()
    stores = Store.objects.all()
    sort = request.GET.get('sort')
    subtype = request.GET.get('subtype')
    if subtype == 'macbook':
        macs = Mac.objects.filter(subtype='Macbook')

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    form = EmailForm()

    new_products = [
        ('macs', Mac.objects.first()),
        ('ipads', Ipad.objects.first()),
        ('iphones', Iphone.objects.first()),
        ('watches', Watch.objects.first()),
        ('airpodss', Airpods.objects.first()),
        ('tv_homes', Tv_Home.objects.first()),
        ('accessoriess', Accessories.objects.first()),
    ]


    context = {
         "stores": stores,
        'iphones': iphones,
        'sliders': sliders,
        'macs': macs,
        'news': news,
        'new_products': new_products,
        'ipads': ipads,
        'accessories': accessories,
        'tv_homes': tv_homes,
        'airpodss': airpodss,
        'watches': watches,
        'form': form,
    }
    return render(request, 'index.html', context)

def mac(request):
    header_mac = Mac.objects.order_by('-id')
    sort = request.GET.get('sort')
    subtype = request.GET.get('subtype') #copy
    macs = Mac.objects.order_by('-id')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if subtype == 'macpro':  # copy #
            macs = Mac.objects.filter(marka='MacBook Pro') #copy
    if subtype == 'macair':
            macs = Mac.objects.filter(marka='MacBook Air')

    if subtype == 'appm5':
            macs = Mac.objects.filter(chip='Apple M5')

    if subtype == 'appm4pr':
            macs = Mac.objects.filter(chip='Apple M4 Pro')

    if subtype == '1TB':
            macs = Mac.objects.filter(ssd='1 TB')
           
    if subtype == '512GB':
            macs = Mac.objects.filter(ssd='512 GB')
    if subtype == '256GB':
            macs = Mac.objects.filter(ssd='256 GB')
             
    if subtype == '8GB':
            macs = Mac.objects.filter(ram='8 GB')
             
    if subtype == '32GB':
            macs = Mac.objects.filter(ram='32 GB')
             
    if subtype == '24GB':
            macs = Mac.objects.filter(ram='24 GB')

    if subtype == '16GB':
            macs = Mac.objects.filter(ram='16 GB')


    if subtype == 'Space Black':
            macs = Mac.objects.filter(color='Space Black')         
    if subtype == 'Silver':
            macs = Mac.objects.filter(color='Silver')         
    if subtype == 'Space Black':
            macs = Mac.objects.filter(color='Space Black')         
    if subtype == '14.2':
            macs = Mac.objects.filter(size='14.2')         
    if subtype == '16.2':
            macs = Mac.objects.filter(size='16.2') 
    if subtype == '15':
            macs = Mac.objects.filter(size='15')        
    if subtype == '13':
            macs = Mac.objects.filter(size='13') 
    if min_price:
        macs = macs.filter(price__gte=min_price)
    if max_price:
        macs = macs.filter(price__lte=max_price)      
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpods = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    
    product_types = Product_type.objects.all()
    
    count = len(macs)
    context = {
         'header_mac': header_mac,
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones,
        'watches': watches,
        'airpods': airpods,
        'tv_homes': tv_homes,
        'accessories': accessories,
        'product_types': product_types,
        'count': count,
        'sort': sort,
    }
    return render(request, 'mac.html', context)

def ipad(request):
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpods = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    count = len(ipads)
    product_types = Product_type.objects.all()

    context = {
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones,
        'watches': watches,
        'airpods': airpods,
        'tv_homes': tv_homes,
        'accessories': accessories,
        'product_types': product_types,
        'count': count,
    }
    return render(request, 'ipad.html', context)

def iphone(request):
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpods = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    count = len(iphones)
    product_types = Product_type.objects.all()

    context = {
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones,
        'watches': watches,
        'airpods': airpods,
        'tv_homes': tv_homes,
        'accessories': accessories,
        'product_types': product_types,
        'count': count,
    }
    return render(request, 'iphone.html', context)

def watch(request):
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpods = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    count = len(watches)
    product_types = Product_type.objects.all()

    context = {
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones,
        'watches': watches,
        'airpods': airpods,
        'tv_homes': tv_homes,
        'accessories': accessories,
        'product_types': product_types,
        'count': count,
    }
    return render(request, 'watch.html', context)

def airpods(request):
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpodss = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    count = len(airpodss)
    product_types = Product_type.objects.all()

    context = {
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones,
        'watches': watches,
        'airpodss': airpodss,
        'tv_homes': tv_homes,
        'accessories': accessories,
        'product_types': product_types,
        'count': count,
    }
    return render(request, 'airpods.html', context)

def tv_home(request):
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpodss = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    count = len(tv_homes)
    product_types = Product_type.objects.all()

    context = {
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones,
        'watches': watches,
        'airpodss': airpodss,
        'tv_homes': tv_homes,
        'accessories': accessories,
        'product_types': product_types,
        'count': count,
    }
    return render(request, 'tv_home.html', context)

def accessories(request):
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.order_by('-id')[:4]
  
    tv_homes = Tv_Home.objects.all()
    airpodss = Airpods.objects.all()
    watches = Watch.objects.all()
    accessories = Accessories.objects.all()
    context = {
        'macs': macs,
        'ipads': ipads,
        'iphones': iphones, 
        'watches': watches,
        'airpodss': airpodss,
        'tv_homes': tv_homes,
         

        'accessoriess': accessories,
    }
    return render(request, 'accessories.html', context)

def trade_in(request):
    sliders = Slider.objects.all()
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    accessoriess = Accessories.objects.all()
    new_products = [
        ('macs', Mac.objects.first()),
        ('ipads', Ipad.objects.first()),
        ('iphones', Iphone.objects.first()),
        ('watches', Watch.objects.first()),
        ('airpodss', Airpods.objects.first()),
        ('tv_homes', Tv_Home.objects.first()),
        ('accessoriess', Accessories.objects.first()),
    ]
    context = {
        'sliders': sliders,
        'macs': macs,
        'new_products': new_products,
        'ipads': ipads,
        'accessoriess': accessoriess,
    }
    return render(request, 'trade_in.html', context)

def list(request):
    search = request.GET.get('search')
    print(search)

    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.all()
    watches = Watch.objects.all()
    airpodss = Airpods.objects.all()
    tv_homes = Tv_Home.objects.all()
    accessories = Accessories.objects.all()
    all = []
    for mac in macs:
        all.append(mac)
    for ipad in ipads:
        all.append(ipad)
    for iphone in iphones:
        all.append(iphone)
    for watch in watches:
        all.append(watch)
    for airpods in airpodss:
        all.append(airpods)
    for tv_home in tv_homes:
        all.append(tv_home)
    for accessory in accessories:
        all.append(accessory)

    if search:
        macs = Mac.objects.filter(name__icontains=search)
        ipads = Ipad.objects.filter(name__icontains=search)
        iphones = Iphone.objects.filter(name__icontains=search)
        watches = Watch.objects.filter(name__icontains=search)
        airpodss = Airpods.objects.filter(name__icontains=search)
        tv_homes = Tv_Home.objects.filter(name__icontains=search)
        accessories = Accessories.objects.filter(name__icontains=search)

        all = []
        for mac in macs:
            all.append(mac)
        for ipad in ipads:
            all.append(ipad)
        for iphone in iphones:
            all.append(iphone)
        for watch in watches:
            all.append(watch)
        for airpods in airpodss:
            all.append(airpods)
        for tv_home in tv_homes:
            all.append(tv_home)
        for accessory in accessories:
            all.append(accessory)
    count = len(all)
    context = {
        'all': all,
        'count': count
    }
    return render(request, 'list.html', context)
def pay(request, model, id):
    news = News.objects.all()
    sliders = Slider.objects.all()
    macs = Mac.objects.all()
    ipads = Ipad.objects.all()
    iphones = Iphone.objects.order_by('-id')[:4]
    accessories = Accessories.objects.all()
    tv_homes = Tv_Home.objects.all()
    airpodss = Airpods.objects.all()
    watches = Watch.objects.all()
    stores = Store.objects.all()
    giftcards = Giftcards.objects.all()
    
    new_products = [
        ('macs', Mac.objects.first()),
        ('ipads', Ipad.objects.first()),
        ('iphones', Iphone.objects.first()),
        ('watches', Watch.objects.first()),
        ('airpods', Airpods.objects.first()),
        ('tv_homes', Tv_Home.objects.first()),
        ('accessories', Accessories.objects.first()),
        ('giftcards', Giftcards.objects.first()),
    ]

    model_map = {
        'macs': Mac,
        'ipads': Ipad,
        'iphones': Iphone,
        'watches': Watch,
        'airpods': Airpods,
        'tv_homes': Tv_Home,
        'accessories': Accessories,
        'giftcards': Giftcards,
    }

    product_model = model_map.get(model)

    if product_model is None:
        raise Http404("Belə model yoxdur")

    product = get_object_or_404(product_model, id=id)

    context = {
        'new_products': new_products,
        'product': product,
        "stores": stores,
        'iphones': iphones,
        'sliders': sliders,
        'macs': macs,
        'news': news,
        'new_products': new_products,
        'ipads': ipads,
        'accessories': accessories,
        'tv_homes': tv_homes,
        'airpodss': airpodss,
        'watches': watches,
        'giftcards': giftcards,
    
    }
    return render(request, 'pay.html', context)

def offers(request):
    offers = Offer.objects.all()
    context = {
        'offers': offers,
    }
    return render(request, 'offers.html', context)

def services(request):
    return render(request, 'services.html')

def financing(request):
    return render(request, 'financing.html')

def warranty(request):
    return render(request, 'warranty.html')

def giftcards(request):
    giftcardss = Giftcards.objects.all()
    context = {
        'giftcardss': giftcardss,
    }
    return render(request, 'giftcards.html', context)

def stores(request):
    stores = Store.objects.all()
    context = {
        'stores': stores,
    }
    return render(request, 'stores.html', context)

def brands(request):
    brands = Brand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, 'brands.html', context)
