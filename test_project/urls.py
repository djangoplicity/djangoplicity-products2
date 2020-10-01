"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from test_project.admin import admin_site
from djangoplicity.products2.models import Calendar, Logo, Exhibition, Sticker, PostCard, \
    PrintedPoster, ConferencePoster, ElectronicPoster, Merchandise, Presentation, Model3d, \
    AnnualReport, Book, Brochure, Flyer, Handout, Map, PressKit, EducationalMaterial, MiniSite, \
    MountedImage, PaperModel, PlanetariumShow, Visit, OnlineArtAuthor, Mirror, TechnicalDocument, \
    GeminiFocus, NOAONewsletter, EducationalProgram, CitizenScienceProgram

from djangoplicity.products2.options import CalendarOptions, LogoOptions, ExhibitionOptions, \
    StickerOptions, PostCardOptions, PrintedPosterOptions, ConferencePosterOptions, \
    ElectronicPosterOptions, MerchandiseOptions, PresentationOptions, Model3dOptions, \
    AnnualReportOptions, BookOptions, BrochureOptions, FlyerOptions, HandoutOptions, \
    MapOptions, PressKitOptions, EducationalMaterialOptions, MiniSiteOptions, MountedImageOptions, \
    PaperModelOptions, PlanetariumShowOptions, VisitOptions, OnlineArtAuthorOptions, MirrorOptions, \
    TechnicalDocumentOptions, GeminiFocusOptions, NOAONewsletterOptions, EducationalProgramOptions, \
    CitizenScienceProgramOptions


urlpatterns = [
    url(r'^admin/', include(admin_site.urls)),
    url(r'^admin/import/', include('djangoplicity.archives.importer.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    # Products
    url( r'^products/models3d/', include('djangoplicity.products2.urls.models3d'), { 'model': Model3d, 'options': Model3dOptions, 'translate': True } ),
    url( r'^products/annual-reports/', include('djangoplicity.products2.urls.annualreports'), { 'model': AnnualReport, 'options': AnnualReportOptions, 'translate': True  } ),
    url( r'^products/books/', include('djangoplicity.products2.urls.books'), { 'model': Book, 'options': BookOptions, 'translate': True } ),
    url( r'^products/brochures/', include('djangoplicity.products2.urls.brochures'), { 'model': Brochure, 'options': BrochureOptions, 'translate': True  } ),
    url( r'^products/calendars/', include('djangoplicity.products2.urls.calendars'), { 'model': Calendar, 'options': CalendarOptions, 'translate': True  } ),
    url( r'^products/conf-posters/', include('djangoplicity.products2.urls.conf_posters'), { 'model': ConferencePoster, 'options': ConferencePosterOptions, 'translate': True  } ),
    url( r'^products/education/', include('djangoplicity.products2.urls.education'), { 'model': EducationalMaterial, 'options': EducationalMaterialOptions, 'translate': True  } ),
    url( r'^products/educational-programs/', include('djangoplicity.products2.urls.educational_programs'), { 'model': EducationalProgram, 'options': EducationalProgramOptions, 'translate': True  } ),
    url( r'^products/elec-cards/', include('djangoplicity.products2.urls.electroniccards'), { 'model': EducationalMaterial, 'options': EducationalMaterialOptions, 'translate': True  } ),
    url( r'^products/elec-posters/', include('djangoplicity.products2.urls.elec_posters'), { 'model': ElectronicPoster, 'options': ElectronicPosterOptions, 'translate': True  } ),
    url( r'^products/exhibitions/', include('djangoplicity.products2.urls.exhibitions'), { 'model': Exhibition, 'options': ExhibitionOptions, 'translate': True  } ),
    url( r'^products/flyers/', include('djangoplicity.products2.urls.flyers'), { 'model': Flyer, 'options': FlyerOptions, 'translate': True  } ),
    url( r'^products/handouts/', include('djangoplicity.products2.urls.handouts'), { 'model': Handout, 'options': HandoutOptions, 'translate': True  } ),
    url( r'^products/logos/', include('djangoplicity.products2.urls.logos'), { 'model': Logo, 'options': LogoOptions, 'translate': True  } ),
    url( r'^products/maps/', include('djangoplicity.products2.urls.maps'), { 'model': Map, 'options': MapOptions, 'translate': True  } ),
    url( r'^products/merchandise/', include('djangoplicity.products2.urls.merchandise'), { 'model': Merchandise, 'options': MerchandiseOptions, 'translate': True  } ),
    url( r'^products/minisites/', include('djangoplicity.products2.urls.minisites'), { 'model': MiniSite, 'options': MiniSiteOptions, 'translate': True  } ),
    url( r'^products/citizenscienceprograms/', include('djangoplicity.products2.urls.citizenscienceprograms'), { 'model': CitizenScienceProgram, 'options': CitizenScienceProgramOptions, 'translate': True  } ),
    url( r'^products/mirrors/', include('djangoplicity.products2.urls.mirrors'), { 'model': Mirror, 'options': MirrorOptions, 'translate': True  } ),
    url( r'^products/gemini-focus/', include('djangoplicity.products2.urls.geminifocus'), { 'model': GeminiFocus, 'options': GeminiFocusOptions, 'translate': True  } ),
    url( r'^products/noao-newsletters/', include('djangoplicity.products2.urls.noaonewsletters'), { 'model': NOAONewsletter, 'options': NOAONewsletterOptions, 'translate': True  } ),
    url( r'^products/mounted-images/', include('djangoplicity.products2.urls.mountedimages'), { 'model': MountedImage, 'options': MountedImageOptions, 'translate': True  } ),
    url( r'^products/paper-models/', include('djangoplicity.products2.urls.papermodels'), { 'model': PaperModel, 'options': PaperModelOptions, 'translate': True  } ),
    url( r'^products/plant-shows/', include('djangoplicity.products2.urls.planetariumshows'), { 'model': PlanetariumShow, 'options': PlanetariumShowOptions, 'translate': True  } ),
    url( r'^products/postcards/', include('djangoplicity.products2.urls.postcards'), { 'model': PostCard, 'options': PostCardOptions, 'translate': True  } ),
    url( r'^products/presentations/', include('djangoplicity.products2.urls.presentations'), { 'model': Presentation, 'options': PresentationOptions, 'translate': True  } ),
    url( r'^products/kits/', include('djangoplicity.products2.urls.presskits'), { 'model': PressKit, 'options': PressKitOptions, 'translate': True  } ),
    url( r'^products/print-posters/', include('djangoplicity.products2.urls.print_posters'), { 'model': PrintedPoster, 'options': PrintedPosterOptions, 'translate': True  } ),
    url( r'^products/stickers/', include('djangoplicity.products2.urls.stickers'), { 'model': Sticker, 'options': StickerOptions, 'translate': True  } ),
    url( r'^products/techdocs/', include('djangoplicity.products2.urls.techdocs'), { 'model': TechnicalDocument, 'options': TechnicalDocumentOptions, 'translate': True  } ),
    # Virtual tours
    url( r'^products/visits/', include('djangoplicity.products2.urls.visits'), { 'model': Visit, 'options': VisitOptions, 'translate': True  } ),
    url( r'^products/artists/', include('djangoplicity.products2.urls.artists'), { 'model': OnlineArtAuthor, 'options': OnlineArtAuthorOptions, 'translate': True  } ),
]
