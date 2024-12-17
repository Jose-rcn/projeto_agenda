from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import get_object_or_404


def index(request):
    Contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts': Contacts,
        'site_title': 'Contatos - Agenda'
    }
    return render(request, 'contact/index.html', context=context)


def single_contact(request, contact_id):
    contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True
    )
    context = {
        'contact': contact,
        'site_title': contact.first_name
    }
    return render(request, 'contact/single_contact.html', context=context)
