from django.shortcuts import render, redirect
from .models import Restaurant
from django.conf import settings
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    """
    Home page that fetches the restaurant details
    and display the details.
    """
    restaurant = Restaurant.objects.first()
    return render(request, "homepage.html", {"restaurant": restaurant})


def contact(request):
    """
    Handle the contact form submission and send email notifications.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # extract form data
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            # email subject & body
            subject = f"New contact form mesage from {name}"
            body = f"""
            You have recevied a new mesage from Tasty Bites:
            Name: {name},
            Email: {email},
            Message: {message}
            """

            # send email
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def homepage(request):
    query = request.GET.get('q')
    restaurant = Restaurant.objects.first()
    if query:
        menu_items = MenuItem.objects.filter(name_icontains=query)
    else:
        menu_items = MenuItem.objects.all()
    return render(request, 'homepage.html', {'menu_items': menu_items, 'query': query, 'restaurant': restaurant})