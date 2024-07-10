from django.contrib import admin
from .models import (
    News,
    Application,
    # Deal,
    Document,
    Image,
    Vazirlik,
    Employee,
    InteraktivXizmat,
    Logo,
    Product,
    ProductInfo,
)
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.utils.safestring import mark_safe


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "full_name_en",
        "full_name_ru",
        "full_name_uz",
        "phone_number",
        "address_en",
        "address_ru",
        "address_uz",
        "position_en",
        "position_ru",
        "position_uz",
        "email",
        "photo",
    )
    search_fields = (
        "full_name_en",
        "full_name_ru",
        "full_name_uz",
        "position_en",
        "position_ru",
        "position_uz",
        "email",
    )


class VazirlikAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


class TenderlarAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


from ckeditor.widgets import CKEditorWidget
from .models import (
    ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar,
    DavlatTashkilotlari,
    Tenderlar,
    MurojaatlarniKoribchiqishTartibi,
    MurojaatlarStatistikasi,
    IshonchTelefoniReglamenti,
    LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlar,
    YoshlarSiyosati,
    YoshlarMarkaziYangiliklari,
    YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlar,
    UmumiyMalumotlar,
    GenderTenglikAsosiyInsonHuquqlaridanBiri,
    YurtimizdaGenderTenglikniTaminlashStrategiyasi,
    MeyoriyHujjatlar,
    MeyorVazirlikdaGenderSiyosatiiyHujjatlar,
    VazirlikdaGenderSiyosati,
    SaytHaritasi,
    HarakatlarStrategiyasi,
    QonunchilikBazasi,
    BoshIshJoylari,
    OchiqMalumotlar,
    KopKelganSavollargaJavoblar,
)


class CKEditorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }


admin.site.register(SaytHaritasi, CKEditorAdmin)
admin.site.register(News, CKEditorAdmin)
admin.site.register(HarakatlarStrategiyasi, CKEditorAdmin)
admin.site.register(QonunchilikBazasi, CKEditorAdmin)
admin.site.register(BoshIshJoylari, CKEditorAdmin)
admin.site.register(OchiqMalumotlar, CKEditorAdmin)
admin.site.register(KopKelganSavollargaJavoblar, CKEditorAdmin)
admin.site.register(
    ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar, CKEditorAdmin
)
admin.site.register(DavlatTashkilotlari, CKEditorAdmin)
admin.site.register(Tenderlar, TenderlarAdmin)
admin.site.register(MurojaatlarniKoribchiqishTartibi, CKEditorAdmin)
admin.site.register(MurojaatlarStatistikasi, CKEditorAdmin)
admin.site.register(IshonchTelefoniReglamenti, CKEditorAdmin)
admin.site.register(LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlar, CKEditorAdmin)
admin.site.register(YoshlarSiyosati, CKEditorAdmin)
admin.site.register(YoshlarMarkaziYangiliklari, CKEditorAdmin)
admin.site.register(YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlar, CKEditorAdmin)
admin.site.register(UmumiyMalumotlar, CKEditorAdmin)
admin.site.register(GenderTenglikAsosiyInsonHuquqlaridanBiri, CKEditorAdmin)
admin.site.register(YurtimizdaGenderTenglikniTaminlashStrategiyasi, CKEditorAdmin)
admin.site.register(MeyoriyHujjatlar, CKEditorAdmin)
admin.site.register(MeyorVazirlikdaGenderSiyosatiiyHujjatlar, CKEditorAdmin)
admin.site.register(VazirlikdaGenderSiyosati, CKEditorAdmin)
admin.site.register(Employee, CKEditorAdmin)
admin.site.register(Logo, CKEditorAdmin)
admin.site.register(Document, CKEditorAdmin)
admin.site.register(Product, CKEditorAdmin)
admin.site.register(ProductInfo, CKEditorAdmin)
admin.site.register(Vazirlik, VazirlikAdmin)


class LogoAdmin(admin.ModelAdmin):
    list_display = ("link", "text_en", "text_ru", "text_uz")


class DocumentAdmin(admin.ModelAdmin):
    list_display = ["id", "title_en", "title_ru", "title_uz"]
    search_fields = ["title_en", "title_ru", "title_uz"]


# class DealAdmin(admin.ModelAdmin):
#     list_display = ('title_en', 'title_ru', 'title_uz', 'status', 'price', 'publish_date', 'expiration_date')
#     search_fields = ('title_en', 'title_ru', 'title_uz', 'status')
#     list_filter = ('status', 'publish_date', 'expiration_date')


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_ru", "title_uz", "pub_date")
    search_fields = ("title_en", "title_ru", "title_uz")


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name_en",
        "name_ru",
        "name_uz",
        "description_en",
        "description_ru",
        "description_uz",
        "image_preview",
    ]
    readonly_fields = ["image_preview"]

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                '<img src="{url}" width="100" />'.format(url=obj.image.url)
            )
        else:
            return "No Image"

    image_preview.short_description = "Image Preview"


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = [
        "title_en",
        "title_ru",
        "title_uz",
        "text_en",
        "text_ru",
        "text_uz",
        "product",
    ]


@admin.register(InteraktivXizmat)
class InteraktivXizmatAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_ru", "title_uz", "url", "views")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone_number")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title_en", "title_ru", "title_uz", "image")


# admin.site.register(Employee, EmployeeAdmin)
# admin.site.register(Logo, LogoAdmin)
# admin.site.register(Document, DocumentAdmin)
# admin.site.register(Product, ProductAdmin)
# admin.site.register(ProductInfo, ProductInfoAdmin)
# admin.site.register(News, NewsAdmin)
