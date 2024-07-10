from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Tenderlar(models.Model):
    STATUS_CHOICES = (
        ("Закупки", "Закупки"),
        ("Продажи", "Продажи"),
        ("Результаты торгов", "Результаты торгов"),
        ("Предприятия с негативным опытом", "Предприятия с негативным опытом"),
        ("Архив", "Архив"),
    )

    title_en = models.TextField(_("Заголовок (English)"), default="Default Text")
    title_ru = models.TextField(_("Заголовок (Russian)"), default="Default Text")
    title_uz = models.TextField(_("Заголовок (Uzbek)"), default="Default Text")
    text_en = models.TextField(_("Текст (English)"), default="Default Text")
    text_ru = models.TextField(_("Текст (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Текст (Uzbek)"), default="Default Text")
    start_date = models.DateField(_("Начало даты"), blank=True, null=True)
    end_date = models.DateField(_("Конец тендера"), blank=True, null=True)
    views = models.PositiveIntegerField(_("Просмотры"), default=0)
    status = models.CharField(
        _("Статус"), max_length=50, choices=STATUS_CHOICES, default="Закупки"
    )

    class Meta:
        verbose_name = _("Тендеры и конкурсы")
        verbose_name_plural = _("Тендеры и конкурсы")

    def __str__(self):
        return self.title_uz


class ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Elektron Hukumat Doirasida Amalga Oshirilayotgan Loyihalar")
        verbose_name_plural = _(
            "Elektron Hukumat Doirasida Amalga Oshirilayotgan Loyihalar"
        )

    def __str__(self):
        return self.text_uz


class DavlatTashkilotlari(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Davlat Tashkilotlari")
        verbose_name_plural = _("Davlat Tashkilotlari")

    def __str__(self):
        return self.text_uz


class DavlatRamzlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Davlat Ramzlar")
        verbose_name_plural = _("Davlat Ramzlar")

    def __str__(self):
        return self.text_uz


class SaytHaritasi(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Sayt Haritasi")
        verbose_name_plural = _("Sayt Haritasi")

    def __str__(self):
        return self.text_uz


class HarakatlarStrategiyasi(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Harakatlar Strategiyasi")
        verbose_name_plural = _("Harakatlar Strategiyasi")

    def __str__(self):
        return self.text_uz


class QonunchilikBazasi(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Qonunchilik Bazasi")
        verbose_name_plural = _("Qonunchilik Bazasi")

    def __str__(self):
        return self.text_uz


class BoshIshJoylari(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Bosh Ish Joylari")
        verbose_name_plural = _("Bosh Ish Joylari")

    def __str__(self):
        return self.text_uz


class OchiqMalumotlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Ochiq Malumotlar")
        verbose_name_plural = _("Ochiq Malumotlar")

    def __str__(self):
        return self.text_uz


class KopKelganSavollargaJavoblar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Kop Kelgan Savollarga Javoblar")
        verbose_name_plural = _("Kop Kelgan Savollarga Javoblar")

    def __str__(self):
        return self.text_uz


class MurojaatlarniKoribchiqishTartibi(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Murojaatlarni Koribchiqish Tartibi")
        verbose_name_plural = _("Murojaatlarni Koribchiqish Tartibi")

    def __str__(self):
        return self.text_uz


class MurojaatlarStatistikasi(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Murojaatlar Statistikasi")
        verbose_name_plural = _("Murojaatlar Statistikasi")

    def __str__(self):
        return self.text_uz


class IshonchTelefoniReglamenti(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Ishonch Telefoni Reglamenti")
        verbose_name_plural = _("Ishonch Telefoni Reglamenti")

    def __str__(self):
        return self.text_uz


class LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Logistika Samaradorligi Indeksi Boyicha Ochiq Malumotlar")
        verbose_name_plural = _(
            "Logistika Samaradorligi Indeksi Boyicha Ochiq Malumotlar"
        )

    def __str__(self):
        return self.text_uz


class YoshlarSiyosati(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Yoshlar Siyosati")
        verbose_name_plural = _("Yoshlar Siyosati")

    def __str__(self):
        return self.text_uz


class YoshlarMarkaziYangiliklari(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Yoshlar Markazi Yangiliklari")
        verbose_name_plural = _("Yoshlar Markazi Yangiliklari")

    def __str__(self):
        return self.text_uz


class YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Yoshlar Siyosatiga Oid Meyoriy Huquqiy Hujjatlar")
        verbose_name_plural = _("Yoshlar Siyosatiga Oid Meyoriy Huquqiy Hujjatlar")

    def __str__(self):
        return self.text_uz


class UmumiyMalumotlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Umumiy Malumotlar")
        verbose_name_plural = _("Umumiy Malumotlar")

    def __str__(self):
        return self.text_uz


class GenderTenglikAsosiyInsonHuquqlaridanBiri(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Gender Tenglik Asosiy Inson Huquqlaridan Biri")
        verbose_name_plural = _("Gender Tenglik Asosiy Inson Huquqlaridan Biri")

    def __str__(self):
        return self.text_uz


class YurtimizdaGenderTenglikniTaminlashStrategiyasi(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Yurtimizda Gender Tenglikni Taminlash Strategiyasi")
        verbose_name_plural = _("Yurtimizda Gender Tenglikni Taminlash Strategiyasi")

    def __str__(self):
        return self.text_uz


class MeyoriyHujjatlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Meyoriy Hujjatlar")
        verbose_name_plural = _("Meyoriy Hujjatlar")

    def __str__(self):
        return self.text_uz


class MeyorVazirlikdaGenderSiyosatiiyHujjatlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Meyor Vazirlikda Gender Siyosatiiy Hujjatlar")
        verbose_name_plural = _("Meyor Vazirlikda Gender Siyosatiiy Hujjatlar")

    def __str__(self):
        return self.text_uz


class VazirlikdaGenderSiyosati(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Vazirlikda Gender Siyosati")
        verbose_name_plural = _("Vazirlikda Gender Siyosati")

    def __str__(self):
        return self.text_uz


class Korsatkichlar(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Korsatkichlar")
        verbose_name_plural = _("Korsatkichlar")

    def __str__(self):
        return self.text_uz


class GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqish(models.Model):
    text_en = models.TextField(_("Text (English)"), default="Default Text")
    text_ru = models.TextField(_("Text (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Text (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Gender Tenglikka Oid Meyoriy Hujjatlarni Ishlab Chiqish")
        verbose_name_plural = _(
            "Gender Tenglikka Oid Meyoriy Hujjatlarni Ishlab Chiqish"
        )

    def __str__(self):
        return self.text_uz


class Document(models.Model):
    title_en = models.CharField(
        _("Title (English)"), max_length=255, default="Default Title (English)"
    )
    title_ru = models.CharField(
        _("Title (Russian)"), max_length=255, default="Default Title (Russian)"
    )
    title_uz = models.CharField(
        _("Title (Uzbek)"), max_length=255, default="Default Title (Uzbek)"
    )
    pdf_file = models.FileField(upload_to="documents/")

    class Meta:
        verbose_name = _("PDF")
        verbose_name_plural = _("PDF")

    def __str__(self):
        return self.title_en


class Application(models.Model):
    first_name = models.CharField(
        _("Ismi"), max_length=100, default="Default First Name"
    )
    last_name = models.CharField(
        _("Sharifi"), max_length=100, default="Default Last Name"
    )
    phone_number = models.CharField(
        _("Telefon raqami"), max_length=20, default="Default Phone Number"
    )

    class Meta:
        verbose_name = _("Boglanish")
        verbose_name_plural = _("Boglanish")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "22"
        verbose_name_plural = "22"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class InteraktivXizmat(models.Model):
    title_en = models.CharField(
        _("Xizmat nomi (English)"), max_length=100, default="Default Name"
    )
    title_ru = models.CharField(
        _("Xizmat nomi (Russian)"), max_length=100, default="Default Name"
    )
    title_uz = models.CharField(
        _("Xizmat nomi (Uzbek)"), max_length=100, default="Default Name"
    )
    url = models.URLField(_("URL"))
    views = models.IntegerField(_("Views"), default=0)

    def __str__(self):
        return self.title_en


class Product(models.Model):
    name_en = models.CharField(
        _("Product Name (English)"), max_length=100, default="Default Name"
    )
    name_ru = models.CharField(
        _("Product Name (Russian)"), max_length=100, default="Default Name"
    )
    name_uz = models.CharField(
        _("Product Name (Uzbek)"), max_length=100, default="Default Name"
    )
    description_en = models.TextField(
        _("Product Description (English)"), default="Default Description"
    )
    description_ru = models.TextField(
        _("Product Description (Russian)"), default="Default Description"
    )
    description_uz = models.TextField(
        _("Product Description (Uzbek)"), default="Default Description"
    )
    image = models.ImageField(_("Image"), upload_to="products/", blank=True, null=True)

    product_number = models.CharField(
        _("Product Number"), max_length=100, blank=True, null=True
    )
    brand = models.CharField(_("Brand"), max_length=100, blank=True, null=True)
    quantity = models.IntegerField(_("Quantity"), default=0)
    price_per_unit = models.DecimalField(
        _("Price per Unit"), max_digits=10, decimal_places=2, default=0
    )
    group_deal = models.BooleanField(_("Group Deal"), default=False)
    trade_type = models.CharField(_("Trade Type"), max_length=50, blank=True, null=True)
    warranty_type = models.CharField(
        _("Warranty Type"), max_length=50, blank=True, null=True
    )
    manufacturer = models.CharField(
        _("Manufacturer"), max_length=100, blank=True, null=True
    )
    manufacturer_country = models.CharField(
        _("Manufacturer Country"), max_length=100, blank=True, null=True
    )
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)

    class Meta:
        verbose_name = _("Product/Tender")
        verbose_name_plural = _("Products/Tenders")

    def __str__(self):
        return self.name_en


class News(models.Model):
    title_en = models.CharField(
        _("Engili nomi (English)"), max_length=200, default="Default Title"
    )
    title_ru = models.CharField(
        _("Engili nomi (Russian)"), max_length=200, default="Default Title"
    )
    title_uz = models.CharField(
        _("Engili nomi (Uzbek)"), max_length=200, default="Default Title"
    )
    image = models.ImageField(_("Image"), upload_to="news_images/")
    text_en = models.TextField(
        _("Engili haqida malumot (English)"), default="Default Text"
    )
    text_ru = models.TextField(
        _("Engili haqida malumot (Russian)"), default="Default Text"
    )
    text_uz = models.TextField(
        _("Engili haqida malumot (Uzbek)"), default="Default Text"
    )
    link = models.URLField(
        _("Link"),
        max_length=200,
        default="https://www.gazeta.uz/oz/2024/04/13/yunusabad/",
    )
    pub_date = models.DateTimeField(_("Publication Date"), auto_now_add=True)
    views = models.PositiveIntegerField(_("Views"), default=0)

    class Meta:
        verbose_name = _("Yangiliklar")
        verbose_name_plural = _("Yangiliklar")

    def __str__(self):
        return self.title_en


class Deal(models.Model):
    title_en = models.CharField(
        _("Title (English)"), max_length=100, default="Default Title"
    )
    title_ru = models.CharField(
        _("Title (Russian)"), max_length=100, default="Default Title"
    )
    title_uz = models.CharField(
        _("Title (Uzbek)"), max_length=100, default="Default Title"
    )
    description_en = models.TextField(
        _("Description (English)"), default="Default Description"
    )
    description_ru = models.TextField(
        _("Description (Russian)"), default="Default Description"
    )
    description_uz = models.TextField(
        _("Description (Uzbek)"), default="Default Description"
    )
    site = models.URLField(_("Site"))
    img = models.ImageField(
        _("Image"), upload_to="tender/", default="tender/default.jpg"
    )
    gmail = models.EmailField(_("Email"))
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    status = models.CharField(_("Status"), max_length=50, default="New")
    publish_date = models.DateField(_("Publish Date"), default=timezone.now)
    expiration_date = models.DateField(_("Expiration Date"), default=timezone.now)
    views = models.PositiveIntegerField(_("Views"), default=0)

    class Meta:
        verbose_name = _("Deal")
        verbose_name_plural = _("Deals")


class Vazirlik(models.Model):
    title_en = models.CharField(
        _("sarlavha (English)"), max_length=100, default="Default Title"
    )
    title_ru = models.CharField(
        _("sarlavha (Russian)"), max_length=100, default="Default Title"
    )
    title_uz = models.CharField(
        _("sarlavha (Uzbek)"), max_length=100, default="Default Title"
    )
    text_en = models.TextField(_("Batafsil malumot (English)"), default="Default Text")
    text_ru = models.TextField(_("Batafsil malumot (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Batafsil malumot (Uzbek)"), default="Default Text")

    def __str__(self):
        return self.title_en


class Employee(models.Model):
    full_name_en = models.CharField(
        _("Ismi Sharifi Familiyasi (English)"),
        max_length=100,
        default="Default Full Name",
    )
    full_name_ru = models.CharField(
        _("Ismi Sharifi Familiyasi (Russian)"),
        max_length=100,
        default="Default Full Name",
    )
    full_name_uz = models.CharField(
        _("Ismi Sharifi Familiyasi (Uzbek)"),
        max_length=100,
        default="Default Full Name",
    )
    phone_number = models.CharField(_("Telefon raqami"), max_length=15)
    address_en = models.CharField(
        _("Address (English)"), max_length=200, default="Default Address"
    )
    address_ru = models.CharField(
        _("Address (Russian)"), max_length=200, default="Default Address"
    )
    address_uz = models.CharField(
        _("Address (Uzbek)"), max_length=200, default="Default Address"
    )
    position_en = models.CharField(
        _("Lavozmi (English)"), max_length=100, default="Default Position"
    )
    position_ru = models.CharField(
        _("Lavozmi (Russian)"), max_length=100, default="Default Position"
    )
    position_uz = models.CharField(
        _("Lavozmi (Uzbek)"), max_length=100, default="Default Position"
    )
    email = models.EmailField(_("Email"))
    comment_en = models.TextField(
        _("Comment (English)"), blank=True, null=True, default="Default Comment"
    )
    comment_ru = models.TextField(
        _("Comment (Russian)"), blank=True, null=True, default="Default Comment"
    )
    comment_uz = models.TextField(
        _("Comment (Uzbek)"), blank=True, null=True, default="Default Comment"
    )
    photo = models.ImageField(_("Photo"), upload_to="photos/", blank=True, null=True)

    class Meta:
        verbose_name = _("Boshlliqlar")
        verbose_name_plural = _("Boshlliqlar")

    def __str__(self):
        return self.full_name_en


class Logo(models.Model):
    link = models.URLField(_("Link"), max_length=200)
    image = models.ImageField(_("Logotip"), upload_to="images/")
    text_en = models.TextField(_("Nomi (English)"), default="Default Text")
    text_ru = models.TextField(_("Nomi (Russian)"), default="Default Text")
    text_uz = models.TextField(_("Nomi (Uzbek)"), default="Default Text")

    class Meta:
        verbose_name = _("Boshqa sayt linklari")
        verbose_name_plural = _("Boshqa sayt linklari")

    def __str__(self):
        return self.text_en


class Image(models.Model):
    title_en = models.CharField(
        _("Title (English)"), max_length=100, default="Default Title"
    )
    title_ru = models.CharField(
        _("Title (Russian)"), max_length=100, default="Default Title"
    )
    title_uz = models.CharField(
        _("Title (Uzbek)"), max_length=100, default="Default Title"
    )
    image = models.ImageField(_("Image"), upload_to="images/")

    class Meta:
        verbose_name = _("Galereya")
        verbose_name_plural = _("Galereya")

    def __str__(self):
        return self.title_en


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, related_name="info", on_delete=models.CASCADE)
    title_en = models.CharField(_("sarlavha (English)"), max_length=100)
    title_ru = models.CharField(_("sarlavha (Russian)"), max_length=100)
    title_uz = models.CharField(_("sarlavha (Uzbek)"), max_length=100)
    text_en = models.TextField(_("Qo'shimcha ma'lumot (English)"))
    text_ru = models.TextField(_("Qo'shimcha ma'lumot (Russian)"))
    text_uz = models.TextField(_("Qo'shimcha ma'lumot (Uzbek)"))

    class Meta:
        verbose_name = "Tender/Mahsulot qisqa malumot"
        verbose_name_plural = "Tender/Mahsulot qisqa malumot"

    def __str__(self):
        # Change 'name' to 'name_en', 'name_ru', or 'name_uz' as needed
        return f"{self.product.name_en} - {self.title_en}"
