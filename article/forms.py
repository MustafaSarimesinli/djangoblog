from django import forms    
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article # model ile Article class ile bağlantı kurma 
        fields = ["title","content","article_image"] # models içindeki title ve content alanından input oluştur. diğerlerine dokanma