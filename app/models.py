from django.db import models
import joblib
import os
import numpy as np
from sklearn.tree import DecisionTreeClassifier


# Create your models here.

class Record(models.Model):
    gender=models.IntegerField()
    age=models.IntegerField()
    hypertension=models.IntegerField()
    heart_disease=models.IntegerField()
    ever_married=models.IntegerField()
    work_type=models.IntegerField()
    residence_type=models.IntegerField()
    avg_glucose_level=models.IntegerField()
    bmi=models.IntegerField()
    smoking_status=models.IntegerField()
    
    svmstroke=models.IntegerField(blank=True,null=True)
    rfstroke=models.FloatField(blank=True,null=True)
    gnbstroke=models.IntegerField(blank=True,null=True)
    
    overallresult=models.FloatField(blank=True, null=True, default=0)
    def save(self, *args, **kwargs):
        
        ml_model_svm=joblib.load(r"C:\Users\Yeeroj\Desktop\MajorJoblibFiles\svm.joblib")
        ml_model_gnb=joblib.load(r"C:\Users\Yeeroj\Desktop\MajorJoblibFiles\gnb.joblib")
        ml_model_rf=joblib.load(r"C:\Users\Yeeroj\Desktop\MajorJoblibFiles\rf.joblib")
        
        mfccs=[self.gender,self.age,self.hypertension,self.heart_disease,self.ever_married,self.work_type,self.residence_type,self.avg_glucose_level,self.bmi,self.smoking_status]
        
        self.svmstroke = ml_model_svm.predict([mfccs])
        self.gnbstroke = ml_model_gnb.predict([mfccs])
        self.rfstroke = ml_model_rf.predict([mfccs])
        
        self.overallresult=(((0.9363*self.rfstroke)+(0.8620*self.gnbstroke)+(0.9393*self.svmstroke))/3)*100
        return super().save(*args, *kwargs)
    


      

    
    

