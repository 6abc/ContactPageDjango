# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully ✅')
            return redirect('index')
        else:
            messages.error(request, 'Message not sent (form validation error) ❌')
    else:
        # Move this inside the else block
        form = ContactForm()
    
    contacts = Contact.objects.all()
    return render(request, 'app/index.html', {'form': form, 'contacts': contacts})