from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Team(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.TextField()
    span_heading = models.TextField()
    description = models.TextField()
    twitter_link = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=30)
    instagram_link = models.CharField(max_length=30)
    linkedin_link = models.CharField(max_length=30)
    def __str__(self):
        return self.heading

# course
class Course(models.Model):
    image = models.ImageField(upload_to='images/')
    category = models.TextField()
    price=models.CharField(max_length=30)
    heading = models.TextField()
    description = models.TextField()
    trainer_profile=models.ImageField(upload_to='images/')
    trainer_name=models.TextField()
    rating=models.IntegerField()
    heart_rating_number=models.IntegerField()
    def __str__(self):
        return f'{self.heading}--{self.category}'
# features
class Feature(models.Model):
    color=models.CharField(max_length=30)
    heading=models.TextField()
    icon = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.heading}'
# counts
class Count(models.Model):
    value=models.IntegerField()
    name=models.TextField()
    def __str__(self):
        return f'{self.value}--{self.name}'

# icon box
class IconBox(models.Model):
    icon=models.CharField(max_length=30)
    heading=models.TextField()
    description=models.TextField()
    def __str__(self):
        return f'{self.heading}'

# class CustomUser(User):
#     phone_number=models.CharField(max_length=30)
#     profile_image=models.ImageField(upload_to='users/')
class AboutCount(models.Model):
    name=models.TextField()
    value=models.IntegerField()
    def __str__(self):
        return f'{self.name}--{self.value}'

class Testimonial(models.Model):
    profile=models.ImageField(upload_to='testimonials/')
    heading1=models.TextField()
    heading2=models.TextField()
    description=models.TextField()
    def __str__(self):
        return f'{self.heading1}--{self.heading2}'

class List(models.Model):
    icon=models.CharField(max_length=30)
    paragraph=models.TextField()
    def __str__(self):
        return f'{self.icon}'


class AboutTitle(models.Model):
    heading=models.TextField()
    description=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class Info(models.Model):
    bgImage=models.ImageField(upload_to='about/')
    heading=models.TextField()
    description=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class Hero(models.Model):
    heading1=models.TextField()
    heading2=models.TextField()
    description=models.TextField()
    btn=models.TextField()
    img=models.ImageField(upload_to='background/')
    def __str__(self):
        return f'{self.heading1}--{self.heading2}'

class Offer(models.Model):
    image=models.ImageField(upload_to='courses/')
    category=models.TextField()
    price=models.CharField(max_length=30)
    heading=models.TextField()
    description=models.TextField()
    trainer_profile=models.ImageField(upload_to='trainers/')
    trainer_name=models.TextField()
    rating=models.IntegerField()
    heart_rating_number=models.IntegerField()
    def __str__(self):
        return f'{self.heading}'

# class ContactForm(models.Model):
#     full_name=models.TextField()
#     email=models.CharField(max_length=30)
#     subject=models.CharField(max_length=30)
#     message=models.TextField()
#     def __str__(self):
#         return f'{self.full_name}'

class Trainer(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.TextField()
    span_heading = models.TextField()
    description = models.TextField()
    twitter_link = models.CharField(max_length=30)
    facebook_link = models.CharField(max_length=30)
    instagram_link = models.CharField(max_length=30)
    linkedin_link = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.heading}'

class PageTitle(models.Model):
    heading=models.TextField()
    description=models.TextField()
    link1=models.TextField()
    link2=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class Card(models.Model):
    image=models.ImageField(upload_to='events/')
    time=models.TextField()
    description=models.TextField()
    def __str__(self):
        return f'{self.time}'

class EventsTitle(models.Model):
    heading=models.TextField()
    description=models.TextField()
    link1=models.TextField()
    link2=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class Contact(models.Model):
    heading=models.TextField()
    description=models.TextField()
    link1=models.TextField()
    link2=models.TextField()

    def __str__(self):
        return f'{self.heading}'

class Item(models.Model):
    icon = models.CharField(max_length=30)
    heading = models.TextField()
    description = models.TextField()
    def __str__(self):
        return f'{self.heading}'

class Footer(models.Model):
    heading = models.TextField()
    link1 = models.TextField()
    link2 = models.TextField()
    link3 = models.TextField()
    link4 = models.TextField()
    link5 = models.TextField()
    def __str__(self):
        return f'{self.heading}'

class CopyRight(models.Model):
    copyright=models.TextField()
    sitename=models.TextField()
    span=models.TextField()
    credits=models.TextField()
    link=models.TextField()
    def __str__(self):
        return f'{self.copyright}'

class footerContact(models.Model):
    description1=models.TextField()
    description2=models.TextField()
    phone=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    twitter=models.CharField(max_length=30)
    facebook=models.CharField(max_length=30)
    Instagram = models.CharField(max_length=30)
    linkedIn = models.CharField(max_length=30)
    def __str__(self):
        return f'{self.description1}--{self.description2}'

class HomeCard(models.Model):
    heading = models.TextField()
    description = models.TextField()
    list1=models.TextField()
    list2=models.TextField()
    list3=models.TextField()
    btn1=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class WhyBox(models.Model):
    heading=models.TextField()
    description=models.TextField()
    span_heading=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class Pricing(models.Model):
    currency=models.CharField(max_length=3)
    amount=models.IntegerField()
    heading=models.TextField()
    month=models.CharField(max_length=15)
    list1=models.TextField()
    list2=models.TextField()
    list3=models.TextField()
    list4=models.TextField()
    list5=models.TextField()
    btn=models.TextField()
    def __str__(self):
        return f'{self.heading}'

class PricingTitle(models.Model):
    heading = models.TextField()
    description = models.TextField()
    link1 = models.TextField()
    link2 = models.TextField()
    def __str__(self):
        return f'{self.heading}'


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=14, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='users/', default='profile.png')

class ContactForm(models.Model):
    full_name = models.CharField(max_length=65)
    email = models.EmailField()
    subject = models.CharField(max_length=65)
    message = models.TextField()







