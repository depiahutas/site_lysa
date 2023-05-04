from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path("produits/", views.produits, name="produits"),

    path("informations/", views.plus_infos, name="informations"),

    path("pourquoi-acheter/", views.pk_acheter, name="pourquoi-acheter"),
]