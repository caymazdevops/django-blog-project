from django.db import models

class Kategori(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Spor(models.Model):
    title = models.CharField(max_length=255)  # Başlık alanı (Maksimum 255 karakter)
    content = models.TextField()  # İçerik alanı
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)  # Görsel alanı (opsiyonel)
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi (otomatik olarak eklenir)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)  # Kategori ekleme

    def __str__(self):
        return self.title  # Modelin başlık alanını döndüren bir temsil
    
class Logolar(models.Model):
    team = models.CharField(max_length=100, default='Unknown Team')
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)  # Görsel alanı (opsiyonel)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)  # Kategori ekleme
   

    def __str__(self):
        return self.team  # Modelin başlık alanını döndüren bir temsil