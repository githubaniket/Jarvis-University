from django.shortcuts import render, redirect
from User.models import Branch, User

def home(request):
    return render(request, 'index.html')

def register(request):
    branches = Branch.objects.all()
    print(branches)
    return render(request, 'register.html',{
        'branches':branches
    })

def saveuser(request):
    ob= User()
    ob.user_name = request.POST.get('uname')
    ob.user_email = request.POST.get('email')
    ob.user_password = request.POST.get('pwd')
    ob.user_type = request.POST.get('type')
    branch_slug = request.POST.get('branch')
    branch = Branch.objects.filter(branch_slug=branch_slug)
    ob.user_branch = branch[0]
    ob.save()
    return redirect("/register")
        

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')        
    else:
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")

        records = User.objects.filter(user_email=email,user_password=pwd)
        count = len(records)
        if count == 0:
            return redirect("/login") 
        else:
            userob = records[0]
            request.session['user'] = {
                'userid': userob.id,
                'name' : userob.user_name,
                'email' : userob.user_email,
                'type' : userob.user_type,
                'branch' : userob.user_branch.branch_slug
            }
            return redirect("/user/home")       