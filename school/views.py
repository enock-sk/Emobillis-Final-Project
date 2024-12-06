from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .form import ContactForm, RegistrationForm
from .models import (
    Team, Course, Feature, Count, IconBox, AboutCount, Testimonial, List,
    AboutTitle, Info, Hero, Offer, Trainer, PageTitle, Card, EventsTitle,
    Contact, Item, Footer, CopyRight, footerContact, HomeCard, WhyBox,
    Pricing, PricingTitle, CustomUser
)
from .utils import send_registration_email


@login_required(login_url='login')
def index(request):
    team = Team.objects.all()
    course = Course.objects.all()
    feature = Feature.objects.all()
    count = Count.objects.all()
    IconBoxes = IconBox.objects.all()
    heros = Hero.objects.first()
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()
    homecard = HomeCard.objects.first()
    whybox = WhyBox.objects.first()

    context = {
        'teams': team,
        'courses': course,
        'features': feature,
        'counts': count,
        'IconBoxes': IconBoxes,
        'hero': heros,
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
        'homecard': homecard,
        'whybox': whybox,
    }
    return render(request, 'index.html', context)


def about(request):
    about = AboutCount.objects.all()
    testimonial = Testimonial.objects.all()
    list = List.objects.all()
    aboutTitle = AboutTitle.objects.first()
    info = Info.objects.first()
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()

    context = {
        'aboutCount': about,
        'testimonials': testimonial,
        'lists': list,
        'aboutTitles': aboutTitle,
        'infos': info,
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
    }
    return render(request, 'about.html', context)


def contact(request):
    contact = Contact.objects.first()
    item = Item.objects.first()
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()

    context = {
        'contact': contact,
        'items': item,
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
    }
    return render(request, 'contact.html', context)


def courses(request):
    offers = Offer.objects.all()
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()

    context = {
        'offers': offers,
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
    }
    return render(request, 'courses.html', context)


def coursedetails(request):
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()

    context = {
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
    }
    return render(request, 'course-details.html', context)


def events(request):
    card = Card.objects.all()
    footer = Footer.objects.all()
    eventsTitle = EventsTitle.objects.first()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()

    context = {
        'cards': card,
        'eventsTitle': eventsTitle,
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
    }
    return render(request, 'events.html', context)


def pricing(request):
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()
    pricing = Pricing.objects.all()
    pricingtitle = PricingTitle.objects.first()

    context = {
        'footer': footer,
        'copyright': copyright,
        'pricings': pricing,
        'pricingtitle': pricingtitle,
        'footerC': footerC,
    }
    return render(request, 'pricing.html', context)


def trainers(request):
    trainer = Trainer.objects.all()
    pageTitle = PageTitle.objects.first()
    footer = Footer.objects.all()
    copyright = CopyRight.objects.first()
    footerC = footerContact.objects.first()

    context = {
        'trainers': trainer,
        'pageTitles': pageTitle,
        'footer': footer,
        'copyright': copyright,
        'footerC': footerC,
    }
    return render(request, 'trainers.html', context)


def user_registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            send_registration_email(user)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Registration successfully.')
            login(request, user)
            return redirect('/')
    return render(request, 'registration_form.html', {'form': form})


def login_user(request):
    if request.method != 'POST':
        return render(request, 'login.html')
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = CustomUser.objects.get(username=username)
        user.set_password(password)
    except CustomUser.DoesNotExist:
        messages.error(request, 'Username does not exist!')
        return render(request, 'login.html')
    user = authenticate(request, username=username, password=password)
    if user is None:
        messages.error(request, 'Incorrect password')
        return render(request, 'login.html')
    elif user.is_active:
        login(request, user)
        messages.success(request, 'Logged in successfully')
    else:
        messages.error(request, 'Please activate your account')
        return render(request, 'login.html')
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('login')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save()
            name = contact_form.full_name
            email = contact_form.email
            subject = contact_form.subject
            message = contact_form.message

            owner_email = 'ekiplangat64@gmail.com'
            email_subject = f"EnoLearn Users Inquiries: {subject}"
            email_message = (
                f"You have received a new message from your EnoLearn contact form.\n\n"
                f"Name: {name}\n"
                f"Email: {email}\n\n"
                f"Message:\n{message}"
            )

            try:
                send_mail(
                    subject=email_subject,
                    message=email_message,
                    from_email=email,
                    recipient_list=[owner_email],
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, "An error occurred while sending your message. Please try again.")

            return redirect('contact-us')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)
