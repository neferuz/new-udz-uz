from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from home.views import (
    ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalarViewSet,
    DavlatTashkilotlariViewSet,
    MurojaatlarniKoribchiqishTartibiViewSet,
    MurojaatlarStatistikasiViewSet,
    IshonchTelefoniReglamentiViewSet,
    LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlarViewSet,
    YoshlarSiyosatiViewSet,
    YoshlarMarkaziYangiliklariViewSet,
    YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlarViewSet,
    UmumiyMalumotlarViewSet,
    GenderTenglikAsosiyInsonHuquqlaridanBiriViewSet,
    YurtimizdaGenderTenglikniTaminlashStrategiyasiViewSet,
    MeyoriyHujjatlarViewSet,
    MeyorVazirlikdaGenderSiyosatiiyHujjatlarViewSet,
    VazirlikdaGenderSiyosatiViewSet,
    TenderlarViewSet,
    SaytHaritasiViewSet,
    HarakatlarStrategiyasiViewSet,
    QonunchilikBazasiViewSet,
    BoshIshJoylariViewSet,
    OchiqMalumotlarViewSet,
    KopKelganSavollargaJavoblarViewSet,
)

router = DefaultRouter()
router.register(r"sayt-haritasi", SaytHaritasiViewSet)
router.register(r"harakatlar-strategiyasi", HarakatlarStrategiyasiViewSet)
router.register(r"qonunchilik-bazasi", QonunchilikBazasiViewSet)
router.register(r"bosh-ish-joylari", BoshIshJoylariViewSet)
router.register(r"ochiq-malumotlar", OchiqMalumotlarViewSet)
router.register(r"kop-kelgan-savollarga-javoblar", KopKelganSavollargaJavoblarViewSet)
router.register(
    r"elektron_hukumat", ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalarViewSet
)
router.register(r"tenderlarkonkurslar", TenderlarViewSet)
router.register(r"davlat_tashkilotlari", DavlatTashkilotlariViewSet)
router.register(
    r"murojaatlarni_koribchiqish_tartibi", MurojaatlarniKoribchiqishTartibiViewSet
)
router.register(r"murojaatlar_statistikasi", MurojaatlarStatistikasiViewSet)
router.register(r"ishonch_telefoni_reglamenti", IshonchTelefoniReglamentiViewSet)
router.register(
    r"logistika_samaradorligi",
    LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlarViewSet,
)
router.register(r"yoshlar_siyosati", YoshlarSiyosatiViewSet)
router.register(r"yoshlar_markazi_yangiliklari", YoshlarMarkaziYangiliklariViewSet)
router.register(
    r"yoshlar_siyosatiga_oid_hujjatlar",
    YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlarViewSet,
)
router.register(r"umumiy_malumotlar", UmumiyMalumotlarViewSet)
router.register(r"gender_tenglik", GenderTenglikAsosiyInsonHuquqlaridanBiriViewSet)
router.register(
    r"gender_tenglik_strategiyasi",
    YurtimizdaGenderTenglikniTaminlashStrategiyasiViewSet,
)
router.register(r"meyoriy_hujjatlar", MeyoriyHujjatlarViewSet)
router.register(
    r"gender_siyosati_hujjatlar", MeyorVazirlikdaGenderSiyosatiiyHujjatlarViewSet
)
router.register(r"vazirlikda_gender_siyosati", VazirlikdaGenderSiyosatiViewSet)

router.register(r"products", views.ProductViewSet)
router.register(r"product-info", views.ProductInfoViewSet)
router.register(r"persons", views.PersonViewSet)
router.register(r"news", views.NewsViewSet)
router.register(r"deals", views.DealViewSet)
# router.register(r'slider-images', views.SliderImageViewSet)
# router.register(r'second-slider-images', views.SecondSliderImageViewSet)
router.register(r"documents", views.DocumentViewSet)
router.register(r"images", views.ImageViewSet)
router.register(r"logos", views.LogoViewSet)
router.register(r"employees", views.EmployeeViewSet)
router.register(r"vazirlik", views.VazirlikViewSet)
router.register(r"interaktiv", views.InteraktivXizmatViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "interaktiv-xizmatlar/",
        views.InteraktivXizmatListCreateAPIView.as_view(),
        name="interaktiv-xizmat-list",
    ),
    path(
        "interaktiv-xizmatlar/<int:pk>/",
        views.InteraktivXizmatRetrieveUpdateDestroyAPIView.as_view(),
        name="interaktiv-xizmat-detail",
    ),
    path("link-redirect/<int:pk>/", views.link_redirect_view, name="link-redirect"),
    path("deals/<int:pk>/", views.DealDetailView.as_view(), name="deal-detail"),
    path(
        "news/<int:pk>/", views.NewsDetailView.as_view(), name="news-detail"
    ),  # Заменен NewsDetailView на views.NewsDetailView.as_view()
    path(
        "interaktiv/<int:pk>/increment_views/",
        views.InteraktivXizmatViewSet.as_view({"post": "increment_views"}),
        name="interaktiv-increment-views",
    ),
    path(
        "applications/",
        views.ApplicationListCreate.as_view(),
        name="create-application",
    ),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
