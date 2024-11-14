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
![Capture d'écran 2024-11-14 172149](https://github.com/user-attachments/assets/26373d3e-22c2-4195-971e-e0e9911bc0fe)
![Capture d'écran 2024-11-14 172214](https://github.com/user-attachments/assets/3bad478b-f74c-4211-bacd-c7c3bc16215f)
![Capture d'écran 2024-11-14 172245](https://github.com/user-attachments/assets/29484b6b-bbf8-405e-a78a-23ec521d6aed)
## Test avec un paquet UDP
![Capture d'écran 2024-11-14 172414](https://github.com/user-attachments/assets/9e715abf-76f5-49b3-9b42-e0b6c2c0e3e0)
![Capture d'écran 2024-11-14 172428](https://github.com/user-attachments/assets/82129d91-342a-4961-b807-479e5a89c03c)
![Capture d'écran 2024-11-14 172449](https://github.com/user-attachments/assets/e5700b19-d1d2-436c-9fc8-19b5b3480111)
## Test de la réception de messages directement sur le serveur API Flask en ligne
![Capture d'écran 2024-11-14 172830](https://github.com/user-attachments/assets/6c56c454-2982-44ab-9472-59fe86ae7400)



