from django.db import models


class CustomUser(models.Model):
    email1 = models.EmailField(unique=True, blank=True,null=True)
    email2 = models.EmailField(unique=True, blank=True,null=True)
    email3 = models.EmailField(unique=True, blank=True,null=True)
    email4 = models.EmailField(unique=True, blank=True,null=True)
    participant1 = models.CharField(max_length=100,null=True)
    participant2 = models.CharField(max_length=100, blank=True,null=True)
    participant3 = models.CharField(max_length=100, blank=True,null=True)
    participant4 = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return self.participant1


# Create your models here.
class forms(models.Model):
    title = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    university_name = models.CharField(max_length=200)
    title_of_the_paper = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    whatsapp_number = models.CharField(max_length=100)
    name_of_the_Second_author = models.CharField(max_length=200)
    name_of_the_Third_author = models.CharField(max_length=200)
    name_of_the_fourth_author = models.CharField(max_length=200)
    name_of_the_fifth_author = models.CharField(max_length=200)
    q1 = models.IntegerField(default=5)
    q2 = models.IntegerField(default=5)
    q3 = models.IntegerField(default=5)
    q4 = models.IntegerField(default=5)
    q5 = models.IntegerField(default=5)
    q6 = models.IntegerField(default=5)
    feedback = models.TextField()

    def __str__(self):
        return self.name
