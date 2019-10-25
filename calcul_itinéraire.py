# Importation des librairies "requests" et "json"
import requests, json 

# Clé de l'API 
api_key ='AIzaSyA0DukmggykrgnxEFOqQ3R37OnbpfEPtqc'

# Entrée de la ville de départ 
dep = input('Départ: ') 

# Entrée de la ville finale
dest = input('Arrivé: ') 

# Génération du lien
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'

 
# Ajoute des paramètres nécessaires pour calculer le trajet 
requete = requests.get(url + 'origins=' + dep +
				'&destinations=' + dest +
				'&key=' + api_key + '&transitmode=bus'
				# + '&sensor=false'
				) 
					

# Met le résultat final en format JSON 
information = requete.json() 


# Affiche le résultat final 
print(information) 
