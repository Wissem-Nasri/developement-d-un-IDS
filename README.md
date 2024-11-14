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
