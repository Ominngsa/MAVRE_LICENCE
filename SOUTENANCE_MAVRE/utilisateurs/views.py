from django.shortcuts import render

# Create your views here.
#Methodes d'affichages des listes 
def Acceuil(request):
    return  render (request, 'index.html')
def Dashboard(request):
    return  render (request, 'dashboard.html')
def TableAssure(request):
    return  render (request, 'tablesAssures.html')

def TableAyantDroit(request):
    return  render (request, 'tablesAyantDroit.html')

def TableCampagnieAssurance(request):
    return  render (request, 'tablesCampagnieAssurance.html')

def TableCommande(request):
    return  render (request, 'tablesCommandes.html')

def TableLivraison(request):
    return  render (request, 'tablesLivraisons.html')

def TableLivreur(request):
    return  render (request, 'tablesLivreurs.html')

def TableMedicament(request):
    return  render (request, 'tablesMedicaments.html')

def TableSociete(request):
    return  render (request, 'tablesSocietes.html')

def TableSouche(request):
    return  render (request, 'tablesSouches.html')

def TableVendeur(request):
    return  render (request, 'tablesVendeurs.html')

#Methodes d'affichages des formulaires 
def FicheAssure(request):
    return  render (request, 'Assures.html')

def FicheAyantDroit(request):
    return  render (request, 'AyantDroit.html')

def FicheCampagnieAssurance(request):
    return  render (request, 'CampagnieAssurance.html')

def FicheCommande(request):
    return  render (request, 'Commande.html')

def FicheLivraison(request):
    return  render (request, 'Livraison.html')

def FicheLivreur(request):
    return  render (request, 'Livreur.html')

def FicheMedicament(request):
    return  render (request, 'Medicament.html')

def FicheSociete(request):
    return  render (request, 'Societe.html')

def FicheSouche(request):
    return  render (request, 'Souche.html')

def FicheVendeur(request):
    return  render (request, 'Vendeur.html')

def FicheConnexion(request):
    return  render (request, 'sign-in.html')

def FicheInscription(request):
    return  render (request, 'sign-up.html')