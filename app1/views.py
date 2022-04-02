from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Cores,Question,Choose,CorrectAns



def index(request):
    all_exam=Cores.objects.all
    return render(request,'home.html',{'all_exam':all_exam})

def qution(request, id):
    qutions=Cores.objects.get(pk=id)
    eachqution=qutions.question_set.all()
    eachqution1=get_object_or_404(eachqution, pk=10)
    return render (request,'qution.html',{'all_qutions':eachqution1})

def result(request,id1,id2):
    next=id2
    if request.method == 'POST':
        next=next+1
        cours=Cores.objects.get(pk=id1)
        eachqution=cours.question_set.get(pk=next)
    return render (request,'qution.html',{'all_qutions':eachqution})