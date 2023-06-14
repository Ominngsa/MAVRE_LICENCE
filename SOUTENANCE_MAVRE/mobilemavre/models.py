from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.translation import gettext_lazy as _

class Utilisateur(models.Model):
    nom = models.CharField(max_length=200)
    email = models.EmailField(_("Adresse email"), max_length=254)
    mot_de_passe = models.CharField(max_length=128)  # Champ pour stocker le mot de passe

    def set_mot_de_passe(self, mot_de_passe):
        # Méthode pour définir le mot de passe en le hashant
        self.mot_de_passe = make_password(mot_de_passe)

    def verifier_mot_de_passe(self, mot_de_passe):
        # Méthode pour vérifier si le mot de passe fourni correspond au mot de passe hashé
        return check_password(mot_de_passe, self.mot_de_passe)
