from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
# admin içersindeki tobloya atıf yapmak için yani göstermek için model.ForeignKey üzeriden çekiyoruz.
# auth.User'ı ForeignKey olarak belirliyoruz. O user'a ait olan article'ların silinmesi gerekiyor.
# bunun için on_delete parametresi yazılır. Eğer o User silinirse buradaki usera ait tüm veriler silinecek.
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
# verbose_name; admin panalinde article da yazılan inglizce kelimeleri istediğimizle değiştirebiliyoruz.
    def __str__(self):
        return self.title
# daha önce NOP gördüğümüz bu method ile makaleleri isimleri görmek yerine başlıklarını ya da istersek yazarını gösterebiliriz.

    class Meta:
        ordering = ['-create_date']


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="isim")
    comment_content = models.CharField(max_length=200,verbose_name="yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']