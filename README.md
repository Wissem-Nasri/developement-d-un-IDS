# Description du projet
Ce projet consiste en un système qui capture des paquets réseau à partir d'une interface réseau locale, puis les envoie à un serveur API Flask pour un traitement supplémentaire.

# Structure du projet
## flask_api_for_packet_processing.py:
Ce fichier contient une API RESTful développée avec Flask.
Elle écoute les requêtes HTTP sur le port 8080 et attend un paramètre de type payload dans l'URL.
Le payload est un message encodé en base64, que l'API décode, le transforme en un dictionnaire Python, puis affiche.
Elle répond avec un message de succès ou une erreur selon que le traitement du payload a réussi ou non.
## packet_capture_and_report.py :
Ce fichier capture des paquets réseau en temps réel à l'aide de la bibliothèque pyshark.
Il surveille les paquets ICMP, TCP, et UDP qui circulent sur le réseau et filtre ceux qui sont envoyés à un serveur API spécifique.
Chaque paquet capturé est transformé en un objet contenant des informations sur le paquet, comme l'adresse IP source et destination, le port source et destination, et l'heure de capture.
Ces informations sont ensuite envoyées à l'API Flask sous forme de message encodé en base64 pour être traitées.
Si le paquet est un ICMP, TCP ou UDP et qu'il n'est pas destiné au serveur API, il est envoyé à l'API pour traitement.
# Fonctionnement détaillé :
## Test avec un paquet ICMP
![Capture d'écran 2024-11-14 171459](https://github.com/user-attachments/assets/0249eb15-32da-4567-930e-d9504582ff08)
![Capture d'écran 2024-11-14 171551](https://github.com/user-attachments/assets/945da31d-2e26-4724-9d8e-5176c3f3622a)
![Capture d'écran 2024-11-14 171615](https://github.com/user-attachments/assets/f8bb6ed9-db13-4e42-ae08-3cecf70a5d39)
## Test avec un paquet TCP
![Uploading Capture d'écran 2024-11-14 172149.png…]()
![Uploading Capture d'écran 2024-11-14 172149.png…]()
![Uploading Capture d'écran 2024-11-14 172245.png…]()
## Test avec un paquet UDP
![Uploading Capture d'écran 2024-11-14 172414.png…]()
![Uploading Capture d'écran 2024-11-14 172428.png…]()
![Uploading Capture d'écran 2024-11-14 172449.png…]()
## Test de la réception de messages directement sur le serveur API Flask en ligne
![Uploading Capture d'écran 2024-11-14 172830.png…]()

