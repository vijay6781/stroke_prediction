from django.http import HttpResponse
from django.shortcuts import render

from app.models import Record
from .forms import RecordForm

# Create your views here.
def home(request):
    return HttpResponse("sadf")


def check(request):
    if request.method =='POST':
        fm=RecordForm(request.POST)
        if fm.is_valid():
            gender=fm.cleaned_data['gender']
            age=fm.cleaned_data['age']
            hypertension=fm.cleaned_data['hypertension']
            heart_disease=fm.cleaned_data['heart_disease']
            ever_married=fm.cleaned_data['ever_married']
            work_type=fm.cleaned_data['work_type']
            residence_type=fm.cleaned_data['residence_type']
            avg_glucose_level=fm.cleaned_data['avg_glucose_level']
            bmi=fm.cleaned_data['bmi']
            smoking_status=fm.cleaned_data['smoking_status']
            local=Record(
                gender=gender,
                age=age,
                hypertension=hypertension,
                heart_disease=heart_disease,
                ever_married=ever_married,
                work_type=work_type,
                residence_type=residence_type,
                avg_glucose_level=avg_glucose_level,
                bmi=bmi,
                smoking_status=smoking_status,
                )
            local.save()
            temp=[item for item in Record.objects.all()]
            # dtstroke=temp[-1].dtstroke
            # knnstroke=temp[-1].knnstroke
            # lrstroke=temp[-1].lrstroke
            svmstroke=temp[-1].svmstroke
            gnbstroke=temp[-1].gnbstroke
            rfstroke=temp[-1].rfstroke
            # rfstroke=temp[-1].rfstroke
            overallresult=temp[-1].overallresult
            return render(request,'result.html',{'svmstroke':svmstroke,'gnbstroke':gnbstroke,'rfstroke':rfstroke,'overallresult':overallresult})
    else:
        fm=RecordForm()        
    return render(request,'check.html',{'form':fm})
        
