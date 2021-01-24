from django.contrib import admin

from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): # models içindeki Article ile dekorator içindeki Article bağlamak için Meta adında bir class oluşturuyoruz. Django önerisi
    
    list_display = ["title","author","create_date"] # panalde hangi bilgilerinin gösterilmesini istiyorsak bunları list_display ile ekliyoruz.
    
    list_display_links = ["title","create_date"] # list_display_link de üzerilerine tıklayarak edit sayfasına gideceğimiz kısma link özelliği eklemeye yarıyor.
    
    search_fields = ["title"] # başlığa göre panelde arama işlemi yapar.
    
    list_filter = ["create_date"] # hangi sürelerde makale oluşturuldu(örn: 7 gün içinde, son 1 ayda vb.) göstermeye yarıyor
    class Meta:
        model = Article # bağlantı işlemi