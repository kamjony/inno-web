from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Product, About, Slider, Media
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    products = Product.objects
    about = About.objects.get(pk=1)
    slider1 = Slider.objects.get(pk=1)
    slider2 = Slider.objects.get(pk=2)
    slider3 = Slider.objects.get(pk=3)
    medias = Media.objects
    return render(request, 'innotech/home.html', {'products':products, 'about':about, 'slider1':slider1, 'slider2':slider2, 'slider3':slider3, 'medias':medias})

def productlist(request):
    productlist = Product.objects
    return render(request, 'innotech/products.html', {'productlist':productlist})

def product_detail(request, product_id):
    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'innotech/product_detail.html', {'product':product_detail})

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "innotech/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def about(request):
    medias1 = Media.objects
    return render(request, 'innotech/about.html', {'medias1':medias1})
