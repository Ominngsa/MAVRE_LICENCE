from django.shortcuts import render
from rest_framework import viewsets
from .models import Utilisateur
from .serializers import UtilisateurSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

# Create your views here.

class UtilisateurViewSet(viewsets.ModelViewSet) :

    """
        -- chaque méthode est définie à l'intérieur de la classe UtilisateurViewSet, 
        -- qui hérite de viewsets.ModelViewSet. Les méthodes sont définies pour effectuer 
        -- les opérations CRUD spécifiques sur les utilisateurs.
    """

    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

    def list(request,self, pk) :

        """
            -- Cette méthode gère la récupération de la liste des utilisateurs existants. 
            -- Elle renvoie généralement une liste paginée des utilisateurs.
        """
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(request,self):
        """
            -- Cette méthode gère la création d'un nouvel utilisateur. 
            -- Elle reçoit les données du nouvel utilisateur dans le corps de la requête 
            -- (généralement au format JSON) et crée un nouvel objet Utilisateur avec ces données.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None) : 

        """
            -- Cette méthode gère la récupération d'un utilisateur spécifique en utilisant 
            -- sa clé primaire (pk). Elle renvoie généralement les détails de l'utilisateur 
            -- correspondant à la clé primaire fournie.
        """
        utilisateur = self.get_object(pk)
        serializer = self.serializer_class(utilisateur)
        return Response(serializer.data)
    def update(self,request,pk=None):

        """
            -- Cette méthode gère la mise à jour d'un utilisateur existant identifié par 
            -- sa clé primaire (pk). Elle reçoit les données de l'utilisateur mises à jour 
            -- dans le corps de la requête et met à jour les champs appropriés de l'objet Utilisateur correspondant.
        """
        utilisateur = self.get_object(pk)
        serializer = self.serializer_class(utilisateur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,request,pk):

        """
            --  Cette méthode gère la mise à jour partielle d'un utilisateur existant identifié par 
            -- sa clé primaire (pk). Elle reçoit uniquement les données mises à jour dans le corps de 
            -- la requête et met à jour les champs appropriés de l'objet Utilisateur correspondant, 
            -- en laissant les autres champs inchangés.
        """
        utilisateur = self.get_object(pk)
        serializer = self.serializer_class(utilisateur, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):

        """
            --  Cette méthode gère la suppression d'un utilisateur existant identifié par sa clé primaire (pk). 
            -- Elle supprime l'objet Utilisateur correspondant de la base de données.
        """
        utilisateur = self.get_object(pk=None)
        utilisateur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return JsonResponse({'message': 'Connexion réussie'})
        else:
            return JsonResponse({'message': 'Nom d\'utilisateur ou mot de passe incorrect'})
    else :
        return JsonResponse({'message': 'Méthode non autorisée'})