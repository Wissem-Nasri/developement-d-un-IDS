import pyshark  # pour capturer les paquets réseau
import netifaces # pour gérer les interfaces réseau
import ipaddress
import json
import requests # pour effectuer des requêtes HTTP
import base64

class pckt(object):
    def __init__(self, sniff_timestamp:str='', layer:str='', srcPort:str='', dstPort:str='', ipSrc:str='', ipDst:str='', highest_layer=''):
        self.sniff_timestamp = sniff_timestamp
        self.layer = layer
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.ipSrc = ipSrc
        self.ipDst = ipDst
        self.highest_layer = highest_layer

class apiServer(object):
    def __init__(self, ip:str, port:str):
        self.ip = ip
        self.port = port

server = apiServer('192.168.142.132', '8080')  # adresse IP de votre serveur API Flask

# Interface réseau par défaut
intF = netifaces.gateways()['default'][netifaces.AF_INET][1]
capture = pyshark.LiveCapture(interface=intF)

def report(message:pckt):   
    temp = json.dumps(message.__dict__)
    jsonString = temp.encode('ascii')
    b64 = base64.b64encode(jsonString)

    jsonPayload = b64.decode('utf8').replace("'",'"')
    print(f"Payload encodé en base64: {jsonPayload}")

    try:
        x = requests.get(f'http://{server.ip}:{server.port}/api/?payload={jsonPayload}')
        if x.status_code == 200:
            print("Données envoyées avec succès.")
        else:
            print(f"Erreur lors de l'envoi : {x.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de connexion : {e}")

def is_api_server(packet, server: apiServer) -> bool:
    if hasattr(packet, 'ip') and hasattr(packet, 'tcp'):
        if (packet.ip.src == server.ip or packet.ip.dst == server.ip) and \
           (packet.tcp.dstport == server.port or packet.tcp.srcport == server.port):
            return True
    return False

def is_private_ip(ip_address):
    ip = ipaddress.ip_address(ip_address)
    return ip.is_private

def packetFilter(packet):
    if is_api_server(packet, server):
        return

    # Pour les paquets ICMP
    if hasattr(packet, 'icmp'):
        p = pckt()
        p.ipDst = packet.ip.dst
        p.ipSrc = packet.ip.src
        p.highest_layer = packet.highest_layer
        p.sniff_timestamp = packet.sniff_timestamp if hasattr(packet, 'sniff_timestamp') else 'N/A'
        p.layer = 'ICMP'  # Définir la couche manuellement pour ICMP
        print(f"ICMP packet: ipSrc={p.ipSrc}, ipDst={p.ipDst}, highest_layer={p.highest_layer}")
        report(p)
        return
    
    # Pour les paquets TCP et UDP
    if packet.transport_layer == 'TCP' or packet.transport_layer == 'UDP':
        if hasattr(packet, 'ipv6'):
            return
        
        if hasattr(packet, 'ip'):
            if is_private_ip(packet.ip.src) and is_private_ip(packet.ip.dst):
                p = pckt()
                p.ipSrc = packet.ip.src
                p.ipDst = packet.ip.dst
                p.sniff_timestamp = packet.sniff_timestamp if hasattr(packet, 'sniff_timestamp') else 'N/A'
                p.highest_layer = packet.highest_layer
                p.layer = packet.transport_layer

                # Gestion des ports pour TCP et UDP
                if hasattr(packet, 'udp'):
                    p.dstPort = packet.udp.dstport
                    p.srcPort = packet.udp.srcport
                elif hasattr(packet, 'tcp'):
                    p.dstPort = packet.tcp.dstport
                    p.srcPort = packet.tcp.srcport

                print(f"{p.layer} packet: ipSrc={p.ipSrc}, ipDst={p.ipDst}, srcPort={p.srcPort}, dstPort={p.dstPort}")
                report(p)

for packet in capture.sniff_continuously():
    packetFilter(packet)
