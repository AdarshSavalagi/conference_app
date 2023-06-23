from django.shortcuts import render, redirect
from .models import *
import os
import zipfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from supporting import send_mail
from django.db import IntegrityError
import openpyxl

IMAGE_INPUT_PATH = 'E:/Production/Conference/conference/supporting/cert_template.jpg'
IMAGE_OUTPUT_PATH1 = 'E:/Production/Conference/conference/media/modififed_template1.jpg'
IMAGE_OUTPUT_PATH2 = 'E:/Production/Conference/conference/media/modififed_template2.jpg'
IMAGE_OUTPUT_PATH3 = 'E:/Production/Conference/conference/media/modififed_template3.jpg'
IMAGE_OUTPUT_PATH4 = 'E:/Production/Conference/conference/media/modififed_template4.jpg'


@login_required(login_url="/signin/")
def index(request):
    if request.method == 'POST':
        Form = forms(
            title=request.POST['salutation'],
            name=request.POST['fullname'],
            university_name=request.POST['university'],
            title_of_the_paper=request.POST['papertitle'],
            email=request.POST['email'],
            contact=request.POST['phone'],
            whatsapp_number=request.POST['Whatsapp'],
            q1=request.POST.get('q1', 5),
            q2=request.POST.get('q2', 5),
            q3=request.POST.get('q3', 5),
            q4=request.POST.get('q4', 5),
            q5=request.POST.get('q5', 5),
            q6=request.POST.get('q6', 5),
            feedback=request.POST['message'],
            name_of_the_Second_author=request.POST['name2'],
            name_of_the_Third_author=request.POST['name3'],
            name_of_the_fourth_author=request.POST['name4'],
            name_of_the_fifth_author=request.POST['name5'],
        )
        Form.save()
        return render(request, 'success.html')
    else:
        return render(request, 'index.html')


def signin2(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            CustomUser.objects.get(email1=username)
            try:
                USER = User.objects.create_user(username, username, '11111111')
            except:
                USER = User.objects.get(username=username)
            obj = authenticate(username=username, password='11111111')
            print(obj)
            if obj is not None:
                login(request, obj)
                return redirect(index)
            else:
                return redirect(index)
        except:
            return render(request, 'signin.html', {"message": 'invalid user'})
    else:
        return render(request, 'signin.html')


def signin(request):
    if request.method == 'POST':
        if CustomUser.objects.filter(email1=request.POST['username']).exists() or CustomUser.objects.filter(
                email2=request.POST['username']).exists() or CustomUser.objects.filter(
            email3=request.POST['username']).exists() or CustomUser.objects.filter(
            email4=request.POST['username']).exists():
            try:
                USER = User.objects.create_user(request.POST['username'], request.POST['username'], '11111111')
            except IntegrityError as e:
                USER = User.objects.get(username=request.POST['username'])
            obj = authenticate(username=request.POST['username'], password='11111111')
            if obj is not None:
                login(request, obj)
                return redirect(index)
            else:
                return redirect(index)
        else:
            return render(request, 'signin.html', {"message": 'invalid user'})
    else:
        return render(request, 'signin.html')


@login_required(login_url="/signin/")
def issueCertificate(request):
    if CustomUser.objects.filter(email1=request.user.username).exists():
        obj = CustomUser.objects.get(email1=request.user.username)
    elif CustomUser.objects.filter(email2=request.user.username).exists():
        obj = CustomUser.objects.get(email2=request.user.username)
    elif CustomUser.objects.filter(email3=request.user.username).exists():
        obj = CustomUser.objects.get(email3=request.user.username)
    elif CustomUser.objects.filter(email4=request.user.username).exists():
        obj = CustomUser.objects.get(email4=request.user.username)
    else:
        return HttpResponse("Invalid Request")
    photo_paths = []
    if obj.participant1 != '' and obj.participant1 is not None:
        send_mail.create(IMAGE_INPUT_PATH, str(obj.participant1), IMAGE_OUTPUT_PATH1)
        photo_paths.append(IMAGE_OUTPUT_PATH1)
    if obj.participant2 != '' and obj.participant2 is not None:
        send_mail.create(IMAGE_INPUT_PATH, str(obj.participant2), IMAGE_OUTPUT_PATH2)
        photo_paths.append(IMAGE_OUTPUT_PATH2)
    if obj.participant3 != '' and obj.participant3 is not None:
        send_mail.create(IMAGE_INPUT_PATH, str(obj.participant3), IMAGE_OUTPUT_PATH3)
        photo_paths.append(IMAGE_OUTPUT_PATH3)
    if obj.participant4 != '' and obj.participant4 is not None:
        send_mail.create(IMAGE_INPUT_PATH, str(obj.participant4), IMAGE_OUTPUT_PATH4)
        photo_paths.append(IMAGE_OUTPUT_PATH4)
    zip_file_path = 'E:/Production/Conference/conference/media/modififed_template.zip'
    with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
        for path in photo_paths:
            photo_name = os.path.basename(path)
            zip_file.write(path, photo_name)
    with open(zip_file_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="photos.zip"'

    os.remove(zip_file_path)

    return response


def get_rows():
    file_path = 'E:\Production\internationalconference\supporting\Book1.xlsx'
    workbook = openpyxl.load_workbook(file_path)
    sheet_name = 'Sheet1'
    sheet = workbook[sheet_name]
    rows = []
    i = 0
    for row in sheet.iter_rows(values_only=True):
        rows.append(row)
        try:
            obj = CustomUser(participant1=row[0])
            if row[1]:
                obj.participant2 = row[1]
            if row[2]:
                obj.participant3 = row[2]
            if row[3]:
                obj.participant4 = row[3]
            if row[4]:
                obj.email1 = row[4]
            if row[5]:
                obj.email2 = row[5]
            if row[6]:
                obj.email3 = row[6]
            if row[7]:
                obj.email4 = row[7]
            obj.save()
            i += 1
            print(f"Object added {row[0]}")
        except Exception as e:
            print(f"object not added {row[0]} : {e}")
    print(f"{i} students added")
