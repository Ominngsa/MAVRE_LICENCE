from django.urls import include, path
from .import views 

urlpatterns = [
    path('', views.Acceuil, name="acceuil"),
    path('/tableauBord', views.Dashboard, name="dashboard"),
    path('/assureTable', views.TableAssure, name="tablesAssure"),
    path('/ayantDroitTable', views.TableAyantDroit, name="tableAyantDroit"),
    path('/CampagnieAssuranceTable', views.TableCampagnieAssurance, name="tableCampagnieAssurance"),
    path('/commandeTable', views.TableCommande, name="tableCommande"),
    path('/livraisonTable', views.TableLivraison, name="tableLivraison"),
    path('/livreurTable', views.TableLivreur, name="tableLivreur"),
    path('/medicamentTable', views.TableMedicament, name="tableMadicament"),
    path('/societeTable', views.TableSociete, name="tableSociete"),
    path('soucheTable', views.TableSouche, name="tableSouche"),
    path('/vendeurTable', views.TableVendeur, name="tableVendeur"),
    path('/assureFiche', views.FicheAssure, name="ficheAssure"),
    path('/ayantDroitFiche', views.FicheAyantDroit, name="ficheAyantDroit"),
    path('/CampagnieAssuranceFiche', views.FicheCampagnieAssurance, name="ficheCampagnieAssurance"),
    path('/commandeFiche', views.FicheCommande, name="ficheCommande"),
    path('/livraisonFiche', views.FicheLivraison, name="ficheLivraison"),
    path('/livreurFiche', views.FicheLivreur, name="ficheLivreur"),
    path('/medicamentFiche', views.FicheMedicament, name="ficheMedicament"),
    path('/societeFiche', views.FicheSociete, name="ficheSociete"),
    path('/soucheFiche', views.FicheSouche, name="ficheSouche"),
    path('/vendeurFiche', views.FicheVendeur, name="ficheVendeur"),
    path('/incriptionFiche', views.FicheInscription, name="ficheInscription"),
    path('/connexionFiche', views.FicheConnexion, name="ficheConnexion"),
]

