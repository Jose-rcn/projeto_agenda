from contact.models import Contact
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q


def index(request):
    Contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')[:10]

    context = {
        'contacts': Contacts,
        'site_title': 'Contatos - Agenda'
    }
    return render(request, 'contact/index.html', context=context)


def search(request,):
    search_value = request.GET.get('q', '').strip()

    if search_value == "":
        return redirect('contact:index')

    print(search_value)
    Contacts = Contact.objects \
        .filter(Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(phone__icontains=search_value) |
                Q(email__icontains=search_value) |
                Q(id__icontains=search_value)
                , show=True)\
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
