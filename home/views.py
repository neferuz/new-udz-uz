from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import (
    Person,
    News,
    Product,
    ProductInfo,
    Application,
    Document,
    Deal,
    Image,
    Logo,
    Employee,
    Vazirlik,
    InteraktivXizmat,
)
from .serializers import (
    PersonSerializer,
    NewsSerializer,
    ProductSerializer,
    ProductInfoSerializer,
    ApplicationSerializer,
    DocumentSerializer,
    DealSerializer,
    ImageSerializer,
    LogoSerializer,
    EmployeeSerializer,
    VazirlikSerializer,
    InteraktivXizmatSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from django.views.generic import TemplateView

from rest_framework import viewsets
from .models import News
from rest_framework import viewsets
from .models import (
    ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar,
    DavlatTashkilotlari,
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
    Tenderlar,
    DavlatRamzlar,
)
from .serializers import (
    ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalarSerializer,
    DavlatTashkilotlariSerializer,
    MurojaatlarniKoribchiqishTartibiSerializer,
    MurojaatlarStatistikasiSerializer,
    IshonchTelefoniReglamentiSerializer,
    LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlarSerializer,
    YoshlarSiyosatiSerializer,
    YoshlarMarkaziYangiliklariSerializer,
    YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlarSerializer,
    UmumiyMalumotlarSerializer,
    GenderTenglikAsosiyInsonHuquqlaridanBiriSerializer,
    YurtimizdaGenderTenglikniTaminlashStrategiyasiSerializer,
    MeyoriyHujjatlarSerializer,
    MeyorVazirlikdaGenderSiyosatiiyHujjatlarSerializer,
    VazirlikdaGenderSiyosatiSerializer,
    TenderlarSerializer,
    DavlatRamzlariSerializer,
)
from .models import (
    SaytHaritasi,
    HarakatlarStrategiyasi,
    QonunchilikBazasi,
    BoshIshJoylari,
    OchiqMalumotlar,
    KopKelganSavollargaJavoblar,
)
from .serializers import (
    SaytHaritasiSerializer,
    HarakatlarStrategiyasiSerializer,
    QonunchilikBazasiSerializer,
    BoshIshJoylariSerializer,
    OchiqMalumotlarSerializer,
    KopKelganSavollargaJavoblarSerializer,
)


class SaytHaritasiViewSet(viewsets.ModelViewSet):
    queryset = SaytHaritasi.objects.all()
    serializer_class = SaytHaritasiSerializer


class HarakatlarStrategiyasiViewSet(viewsets.ModelViewSet):
    queryset = HarakatlarStrategiyasi.objects.all()
    serializer_class = HarakatlarStrategiyasiSerializer


class QonunchilikBazasiViewSet(viewsets.ModelViewSet):
    queryset = QonunchilikBazasi.objects.all()
    serializer_class = QonunchilikBazasiSerializer


class BoshIshJoylariViewSet(viewsets.ModelViewSet):
    queryset = BoshIshJoylari.objects.all()
    serializer_class = BoshIshJoylariSerializer


class OchiqMalumotlarViewSet(viewsets.ModelViewSet):
    queryset = OchiqMalumotlar.objects.all()
    serializer_class = OchiqMalumotlarSerializer


class KopKelganSavollargaJavoblarViewSet(viewsets.ModelViewSet):
    queryset = KopKelganSavollargaJavoblar.objects.all()
    serializer_class = KopKelganSavollargaJavoblarSerializer


class DavlatRamzlar(viewsets.ModelViewSet):
    queryset = DavlatRamzlar.objects.all()
    serializer_class = DavlatRamzlariSerializer


class ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalarViewSet(
    viewsets.ModelViewSet
):
    queryset = ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalar.objects.all()
    serializer_class = ElektronHukumatDoirasidaAmalgaOshirilayotganLoyihalarSerializer


class DavlatTashkilotlariViewSet(viewsets.ModelViewSet):
    queryset = DavlatTashkilotlari.objects.all()
    serializer_class = DavlatTashkilotlariSerializer


class TenderlarViewSet(viewsets.ModelViewSet):
    queryset = Tenderlar.objects.all()
    serializer_class = TenderlarSerializer

    @action(detail=True, methods=["post"])
    def increment_views(self, request, pk=None):
        tenderlar = self.get_object()
        tenderlar.views += 1
        tenderlar.save()
        return Response({"status": "views incremented", "views": tenderlar.views})


class MurojaatlarniKoribchiqishTartibiViewSet(viewsets.ModelViewSet):
    queryset = MurojaatlarniKoribchiqishTartibi.objects.all()
    serializer_class = MurojaatlarniKoribchiqishTartibiSerializer


class MurojaatlarStatistikasiViewSet(viewsets.ModelViewSet):
    queryset = MurojaatlarStatistikasi.objects.all()
    serializer_class = MurojaatlarStatistikasiSerializer


class IshonchTelefoniReglamentiViewSet(viewsets.ModelViewSet):
    queryset = IshonchTelefoniReglamenti.objects.all()
    serializer_class = IshonchTelefoniReglamentiSerializer


class LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlarViewSet(viewsets.ModelViewSet):
    queryset = LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlar.objects.all()
    serializer_class = LogistikaSamaradorligiIndeksiBoyichaOchiqMalumotlarSerializer


class YoshlarSiyosatiViewSet(viewsets.ModelViewSet):
    queryset = YoshlarSiyosati.objects.all()
    serializer_class = YoshlarSiyosatiSerializer


class YoshlarMarkaziYangiliklariViewSet(viewsets.ModelViewSet):
    queryset = YoshlarMarkaziYangiliklari.objects.all()
    serializer_class = YoshlarMarkaziYangiliklariSerializer


class YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlarViewSet(viewsets.ModelViewSet):
    queryset = YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlar.objects.all()
    serializer_class = YoshlarSiyosatigaOidMeyoriyHuquqiyHujjatlarSerializer


class UmumiyMalumotlarViewSet(viewsets.ModelViewSet):
    queryset = UmumiyMalumotlar.objects.all()
    serializer_class = UmumiyMalumotlarSerializer


class GenderTenglikAsosiyInsonHuquqlaridanBiriViewSet(viewsets.ModelViewSet):
    queryset = GenderTenglikAsosiyInsonHuquqlaridanBiri.objects.all()
    serializer_class = GenderTenglikAsosiyInsonHuquqlaridanBiriSerializer


class YurtimizdaGenderTenglikniTaminlashStrategiyasiViewSet(viewsets.ModelViewSet):
    queryset = YurtimizdaGenderTenglikniTaminlashStrategiyasi.objects.all()
    serializer_class = YurtimizdaGenderTenglikniTaminlashStrategiyasiSerializer


class MeyoriyHujjatlarViewSet(viewsets.ModelViewSet):
    queryset = MeyoriyHujjatlar.objects.all()
    serializer_class = MeyoriyHujjatlarSerializer


class MeyorVazirlikdaGenderSiyosatiiyHujjatlarViewSet(viewsets.ModelViewSet):
    queryset = MeyorVazirlikdaGenderSiyosatiiyHujjatlar.objects.all()
    serializer_class = MeyorVazirlikdaGenderSiyosatiiyHujjatlarSerializer


class VazirlikdaGenderSiyosatiViewSet(viewsets.ModelViewSet):
    queryset = VazirlikdaGenderSiyosati.objects.all()
    serializer_class = VazirlikdaGenderSiyosatiSerializer


# from .models import News,Korsatkichlar,GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqish
# from .serializers import NewsSerializer,KorsatkichlarSerializer,GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqishSerializer


class VazirlikViewSet(viewsets.ModelViewSet):
    queryset = Vazirlik.objects.all()
    serializer_class = VazirlikSerializer


# class KorsatkichlarViewSet(viewsets.ModelViewSet):
#     queryset = Korsatkichlar.objects.all()
#     serializer_class = KorsatkichlarSerializer

# class GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqishViewSet(viewsets.ModelViewSet):
#     queryset = GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqish.objects.all()
#     serializer_class = GenderTenglikkaOidMeyoriyHujjatlarniIshlabChiqishSerializer


class DealDetailView(TemplateView):
    template_name = "deal_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["deal_id"] = self.kwargs["pk"]
        return context


class NewsDetailView(TemplateView):
    template_name = "news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_id"] = self.kwargs["pk"]
        return context


def link_redirect_view(request, pk):
    interaktiv_xizmat = get_object_or_404(InteraktivXizmat, pk=pk)
    interaktiv_xizmat.views += 1
    interaktiv_xizmat.save()
    return redirect(interaktiv_xizmat.url)


class InteraktivXizmatViewSet(viewsets.ModelViewSet):
    queryset = InteraktivXizmat.objects.all()
    serializer_class = InteraktivXizmatSerializer

    @action(detail=True, methods=["post"])
    def increment_views(self, request, pk=None):
        interaktiv = self.get_object()
        interaktiv.views += 1
        interaktiv.save()
        return Response({"status": "views incremented", "views": interaktiv.views})


class InteraktivXizmatListCreateAPIView(generics.ListCreateAPIView):
    queryset = InteraktivXizmat.objects.all()
    serializer_class = InteraktivXizmatSerializer


class InteraktivXizmatRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = InteraktivXizmat.objects.all()
    serializer_class = InteraktivXizmatSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class LogoViewSet(viewsets.ModelViewSet):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ApplicationListCreate(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @action(detail=True, methods=["post"])
    def increment_views(self, request, pk=None):
        news = self.get_object()
        news.views += 1
        news.save()
        return Response({"status": "views incremented", "views": news.views})


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    @action(detail=True, methods=["post"])
    def increment_views(self, request, pk=None):
        deal = self.get_object()
        deal.views += 1
        deal.save()
        return Response({"status": "views incremented", "views": deal.views})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
