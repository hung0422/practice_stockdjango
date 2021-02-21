from django import forms
from .models import PredictionRecord, PredictionCategory

# 建立新資料會用到
class RecordForm(forms.ModelForm):
    class Meta:
        model = PredictionRecord
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = PredictionCategory
        fields = '__all__'