from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Product, About, Slider, Media, Team
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    medias = Media.objects
    products = Product.objects
    teams = Team.objects
    about = About.objects.get(pk=1)
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
    return render(request, 'innotech/home.html', {'medias':medias, 'products':products, 'about':about, 'teams':teams, 'form': form})
