from django.db import models

class CategoryBanner(models.Model):
    title = models.CharField(max_length=15,verbose_name="Başlık")
    file = models.ImageField(upload_to = "category_banner")
    url = models.URLField(verbose_name="Link")
    isActive = models.BooleanField(default=True, verbose_name="Aktif/Pasif")

class SliderItem(models.Model):
    title = models.CharField(max_length=40,verbose_name="Başlık")
    image = models.ImageField(upload_to = "main_slider")
    paragraph = models.CharField(max_length=90,verbose_name="Metin")
    url = models.URLField(verbose_name="Link")
    isActive = models.BooleanField(default=True, verbose_name="Aktif/Pasif")


class SubLinks(models.Model):
    name = models.CharField(max_length=15,verbose_name="Yardımcı Link")
    url = models.URLField(verbose_name="Link")
    isActive = models.BooleanField(default=True, verbose_name="Aktif/Pasif")

class TopBarContent(models.Model):
    
    contentType = models.TextChoices('contentType', 'Görsel Metin')
    content = models.CharField(blank=True, choices=contentType.choices, max_length=10)
    text = models.CharField(max_length=80, verbose_name="Metin", blank=True)
    url = models.URLField(verbose_name="Link",default="link")
    image = models.ImageField(upload_to = "topbar")


class FooterSetting(models.Model):

    paragraph = models.TextField(max_length=125, verbose_name="Tanıtıcı Paragraf")

    group1_title = models.CharField(max_length=10,verbose_name="Link Grubu 1 Başlık")

    g1_link1_name = models.CharField(max_length=30,verbose_name="Group 1 Link-1 Ad")
    g1_link1 = models.URLField(verbose_name="Group 1 Link-1 Url")

    g1_link2_name = models.CharField(max_length=30,verbose_name="Group 1 Link-2 Ad")
    g1_link2 = models.URLField(verbose_name="Group 1 Link-2 Url")

    g1_link3_name = models.CharField(max_length=30,verbose_name="Group 1 Link-3 Ad")
    g1_link3 = models.URLField(verbose_name="Group 1 Link-3 Url")

    g1_link4_name = models.CharField(max_length=30,verbose_name="Group 1 Link-2 Ad")
    g1_link4 = models.URLField(verbose_name="Group 1 Link-4 Url")


    group2_title = models.CharField(max_length=10,verbose_name="Link Grubu 2 Başlık")

    g2_link1_name = models.CharField(max_length=30,verbose_name="Group 2 Link-1 Ad")
    g2_link1 = models.URLField(verbose_name="Group 2 Link-1 Url")

    g2_link2_name = models.CharField(max_length=30,verbose_name="Group 2 Link-2 Ad")
    g2_link2 = models.URLField(verbose_name="Group 2 Link-2 Url")

    g2_link3_name = models.CharField(max_length=30,verbose_name="Group 2 Link-3 Ad")
    g2_link3 = models.URLField(verbose_name="Group 2 Link-3 Url")

    g2_link4_name = models.CharField(max_length=30,verbose_name="Group 2 Link-4 Ad")
    g2_link4 = models.URLField(verbose_name="Group 2 Link-4 Url")

    adress = models.CharField(max_length=25, verbose_name="Adres")
    mail = models.EmailField(verbose_name="E-Mail")
    phone = models.CharField(max_length=16, verbose_name="Telefon")
    whatsapp = models.CharField(max_length=16, verbose_name="Whatsapp")
    edited_date = models.DateTimeField(auto_now=True, verbose_name="Düzenleme Tarihi")

    social_link1 = models.URLField(verbose_name="Sosyal Medya 1 Url")
    social_link1_icon = models.CharField(max_length=50,verbose_name= "Sosyal Medya İkon 1 ")
    
    social_link2 =models.URLField(verbose_name="Sosyal Medya 2 Url")
    social_link2_icon = models.CharField(max_length=50,verbose_name= "Sosyal Medya İkon 2 ")

    social_link3 = models.URLField(verbose_name="Sosyal Medya 3 Url")
    social_link3_icon = models.CharField(max_length=50,verbose_name= "Sosyal Medya İkon 3 ")

    social_link4 = models.URLField(verbose_name="Sosyal Medya 4 Url")
    social_link4_icon = models.CharField(max_length=50,verbose_name= "Sosyal Medya İkon 4")
    


