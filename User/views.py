from django.shortcuts import render, redirect
from Question.models import StudentQuestion
from .models import User

def home(request):
    userob = request.session['user']

    if userob['type'] == 'student':
        temp = "student/studenthome.html"   
    else:
        temp = "faculty/facultyhome.html"    

    return render(request, temp ,{
        'name' : userob['name'] 
    })

def askque(request):
    userid = request.session['user'].get('userid')
    user = User.objects.get(pk=userid)

    qlist = StudentQuestion.objects.filter(student=user, activeStatus = True)
    return render(request, 'student/askque.htm',{
        'list' : qlist
    })

def viewque(request):
    qlist = StudentQuestion.objects.filter(activeStatus=True)
    return render(request, 'faculty/viewque.htm',{
        'list': qlist
    })    

def logout(request):
    del request.session['user']
    return redirect("/login")

def profile(request):
    usertype = request.session['user'].get('type')
    return render(request, 'profile.htm',{
        'type': usertype
    })

def changepass(request):
    oldpass = request.POST.get('oldpwd')
    newpass = request.POST.get('newpwd')

    userid = request.session['user'].get('userid')
    user = User.objects.get(pk=userid)

    if user.user_password == oldpass:
        user.user_password = newpass
        user.save()

    return redirect('/user/logout')