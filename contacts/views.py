from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http import HttpRequest
from django.db.models import Q

from contacts.forms import ContactForm
from contacts.models import Contact
# Create your views here.
@login_required
def index(request):
    contacts = request.user.contacts.all().order_by('-created_at')
    context = {
        'contacts': contacts,
        'form': ContactForm()
    }
    return render(request, 'contacts.html', context)

@login_required
def search_contacts(request):
    query = request.GET.get('search', '')

    # import time
    # time.sleep(2)
    
    contacts = request.user.contacts.filter(
        Q(name__icontains=query) | Q(email__icontains=query)
    )

    return render(
        request, 
        'partials/contact-list.html',
        {'contacts': contacts}
    )

@login_required
@require_http_methods(['POST'])
def create_contact(request: HttpRequest):
    form = ContactForm(
        request.POST, 
        initial={'user': request.user}
    )
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()

        context = {'contact': contact}
        response = render(
            request, 
            'partials/contact-row.html', 
            context
        )
        response['HX-Trigger'] = 'success'
        return response
    else:
        response = render(
            request, 
            'partials/add-contact-modal.html', 
            {'form': form}
        )
        response['HX-Retarget'] = '#contact_modal' # Retarget the modal
        response['HX-Reswap'] = 'outerHTML' # Replace the modal content with the form
        response['HX-Trigger-After-Settle'] = 'fail' # Show an alert if the form is not valid
        return response

# @login_required
# @require_http_methods(['DELETE'])
# def delete_contact(request: HttpRequest, contact_id: int):
#     query = Q(id=contact_id, user=request.user)
#     contact = Contact.objects.get(query)
#     if contact:
#         contact.delete()
#         return HttpResponse(status=204)
#     else:
#         return HttpResponse(status=404)
