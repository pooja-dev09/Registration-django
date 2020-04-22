from django.shortcuts import render
from django.http import HttpResponse
from .models import loginform


def index(request):
    if request.method=='POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        dateofbirth = request.POST.get('birthday')
        gender =  request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        education = request.POST.get('subject')
        d = loginform(FirstName= firstname,LastName=lastname,DateOfBirth=dateofbirth,Gender=gender,Email=email,Phone=phone,Education=education)
        d.save()
    return render(request, 'index.html')

def login(request):
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    datavalid = loginform.objects.filter(Email=email,Phone=phone)
    if datavalid:
        return viewprofile(request)
    else:
        return render(request, 'login.html')

def viewprofile(request):
    data = loginform.objects.all()
    data_new = []
    for i in data:
        email_data= i.Email
        phone_data=i.Phone
        gender_data=i.Gender
        education_data=i.Education
        id = i.id
        data = {'email_data':email_data,'phone_data':phone_data,'gender_data':gender_data,'education_data':education_data,'id':id}
        data_new.append(data)
    return  render(request, 'profile.html',{'result':data_new })

def editprofile(request,id):
    dataid = loginform.objects.filter(id=id)
    new =[]
    for i in dataid:
        first_name = i.FirstName
        last_Name = i.LastName
        date_of_birth = i.DateOfBirth
        gender = i.Gender
        email = i.Email
        phone = i.Phone
        education = i.Education
        data = {'id':id,'first_name':first_name,'last_Name':last_Name,'date_of_birth':date_of_birth,'gender':gender,'email':email,'phone':phone,'education':education}
        new.append(data)
    return render(request, 'edit.html',{'result':new})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        dateofbirth = request.POST.get('birthday')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        education = request.POST.get('education')
        loginform.objects.filter(id=id).update(FirstName=firstname,LastName=lastname,DateOfBirth=dateofbirth,Gender=gender,Email=email,Phone=phone,Education=education)

    return  viewprofile(request)

def delete(request,id):
    loginform.objects.filter(id=id).delete()
    return viewprofile(request)




