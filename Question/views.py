from django.shortcuts import render, redirect
from django.http import HttpResponse
from User.models import User
from .models import StudentQuestion, Answers

def saveQus(request):
    userid = request.session['user'].get('userid')
    user = User.objects.get(pk=userid)

    qob = StudentQuestion()
    qob.ques = request.POST.get('question')
    qob.student = user

    qob.save()
    
    return redirect('/user/ask')

def saveAns(request):
    userid = request.session['user'].get('userid')
    user = User.objects.get(pk=userid)

    question = StudentQuestion.objects.get(pk=request.GET.get('qid'))

    ob = Answers()
    ob.ans = request.GET.get('ans')
    ob.faculty = user
    ob.question = question
    ob.student = user

    ob.save()
    
    return HttpResponse("Done !")

def viewAns(request):
    qid = request.GET.get('qid')
    ques = StudentQuestion.objects.get(pk=request.GET.get('qid'))
    answers = Answers.objects.filter(question=ques)
    return render(request, "student/answers.htm",{
        'answers': answers
    })
