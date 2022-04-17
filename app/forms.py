from django import forms
from .models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'gender',
            'age',
            'hypertension',
            'heart_disease',
            'ever_married',
            'work_type',
            'residence_type',
            'avg_glucose_level',
            'bmi',
            'smoking_status',
            
            
            
            ]
        
