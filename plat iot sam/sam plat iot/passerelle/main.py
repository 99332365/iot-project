 
# from network import Bluetooth
# import struct

# # Initialisation du Bluetooth
# bluetooth = Bluetooth()
# bluetooth.init()

# # UUIDs pour le service et la caractéristique
# SERVICE_UUID = 0xec00
# CHARACTERISTIC_UUID = 0xec0e

# def handle_client(value):
#     """Gère les données reçues d'un client BLE."""
#     try:
#         # Affiche les données brutes pour débogage
#         #print("Données brutes reçues:", value)
        
#         # Décompresser les données reçues (format float)
#         temperature = struct.unpack('f', value)[0]
#         print("Température reçue: {:.2f} °C".format(temperature))
#     except Exception as e:
#         print("Erreur lors du traitement des données reçues:", e)

# def conn_cb(event):
#     """Callback pour les événements de connexion/déconnexion."""
#     if event == Bluetooth.CLIENT_CONNECTED:
#         print('Client connecté')
#     elif event == Bluetooth.CLIENT_DISCONNECTED:
#         print('Client déconnecté')

# def chr1_handler(chr, value):
#     """Callback pour gérer les données reçues dans la caractéristique."""
#     try:
#         # Extraire les données binaires du tuple reçu
#         if isinstance(value, tuple) and len(value) > 1:
#             value = value[1]  # Obtenir les données binaires
#         # Lire la valeur de la caractéristique
#         handle_client(value)
#     except Exception as e:
#         print("Erreur dans le handler de caractéristique:", e)

# # Initialiser le Bluetooth et diffuser le service BLE
# bluetooth.set_advertisement(name='FiPy Server', service_uuid=SERVICE_UUID)
# bluetooth.advertise(True)

# # Créer un service et une caractéristique
# srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=1)
# chr1 = srv1.characteristic(uuid=CHARACTERISTIC_UUID, value=b'')  # Créer une caractéristique vide

# # Configurer les callbacks pour les événements de lecture et d'écriture
# chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=chr1_handler)
# bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

# print('Serveur BLE démarré et en attente de connexions...')

# while True:
#     pass  # Maintenir le serveur en marche
##### essai
# from network import Bluetooth
# import struct
# import _thread
# import time

# # Initialisation du Bluetooth
# bluetooth = Bluetooth()
# bluetooth.init()

# # UUIDs pour le service et la caractéristique
# SERVICE_UUID = 0xec00
# CHARACTERISTIC_UUID = 0xec0e

# # Dictionnaire pour stocker les connexions des clients
# clients = {}

# def handle_client(value):
#     """Gère les données reçues d'un client BLE."""
#     try:
#         # Affiche les données brutes pour débogage
#         # print("Données brutes reçues:", value)
        
#         # Décompresser les données reçues (format float)
#         temperature = struct.unpack('f', value)[0]
#         print("Température reçue: {:.2f} °C".format(temperature))
#     except Exception as e:
#         print("Erreur lors du traitement des données reçues:", e)

# def client_thread(conn_handle):
#     """Thread pour gérer la communication avec un client spécifique."""
#     try:
#         while conn_handle in clients:
#             # Simule la gestion des données du client
#             # (Remplacez ceci par des opérations réelles si nécessaire)
#             time.sleep(1)  # Par exemple, attendre ou effectuer des tâches
#     except Exception as e:
#         print("Erreur dans le thread du client {}:".format(conn_handle), e)
#     finally:
#         print("Thread du client {} terminé.".format(conn_handle))

# def conn_cb(event, conn_handle):
#     """Callback pour les événements de connexion/déconnexion."""
#     if event == Bluetooth.CLIENT_CONNECTED:
#         print('Client connecté:', conn_handle)
#         clients[conn_handle] = None  # Ajouter le client au dictionnaire
#         # Démarrer un nouveau thread pour gérer ce client
#         _thread.start_new_thread(client_thread, (conn_handle,))
#     elif event == Bluetooth.CLIENT_DISCONNECTED:
#         print('Client déconnecté:', conn_handle)
#         if conn_handle in clients:
#             del clients[conn_handle]  # Supprimer le client du dictionnaire

# def chr1_handler(value):
#     """Callback pour gérer les données reçues dans la caractéristique."""
#     try:
#         # Lire la valeur de la caractéristique
#         handle_client(value)
#     except Exception as e:
#         print("Erreur dans le handler de caractéristique:", e)

# # Initialiser le Bluetooth et diffuser le service BLE
# bluetooth.set_advertisement(name='FiPy Server', service_uuid=SERVICE_UUID)
# bluetooth.advertise(True)

# # Créer un service et une caractéristique
# srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=1)
# chr1 = srv1.characteristic(uuid=CHARACTERISTIC_UUID, value=b'')  # Créer une caractéristique vide

# # Configurer les callbacks pour les événements de lecture et d'écriture
# chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=chr1_handler)
# bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

# print('Serveur BLE démarré et en attente de connexions...')

# while True:
#     pass  # Maintenir le serveur en marche
# from network import Bluetooth, WLAN
# import struct
# import socket
# import time
# from machine import Pin
# import _thread as thread # Utilisation du module thread de MicroPython

# # Configuration du réseau Wi-Fi
# ssid = 'IoT IMT Nord Europe'
# password = '72Hin@R*'

# def configurer_reseau():
#     wlan = WLAN(mode=WLAN.STA)
#     wlan.connect(ssid, auth=(WLAN.WPA2, password))

#     while not wlan.isconnected():
#         print('Connecting to Wi-Fi...')
#         time.sleep(1)

#     print('Connected to Wi-Fi')
#     print('IP Address: {}'.format(wlan.ifconfig()[0]))
#     return wlan.ifconfig()[0]  # Retourner l'adresse IP

# # Fonction pour envoyer des données de température au TcpSenderNode
# def envoyer_temperature_tcp_sender(temperature):
#     command = 'Temperature: {}\n'.format(temperature)
#     try:
#         conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         conn.connect(('10.89.1.86', 1235))  # Adresse IP et port du TcpSenderNode
#         conn.send(command.encode())
#         print('Température envoyée: {}'.format(command.strip()))
#     except Exception as e:
#         print('Erreur d\'envoi de température: {}'.format(e))
#     finally:
#         conn.close()  # Fermer la connexion après envoi

# # Initialisation du Bluetooth
# bluetooth = Bluetooth()
# bluetooth.init()

# # UUIDs pour le service et la caractéristique
# SERVICE_UUID = 0xec00
# CHARACTERISTIC_UUID = 0xec0e

# def handle_client(value):
#     """Gère les données reçues d'un client BLE."""
#     try:
#         # Décompresser les données reçues (format float)
#         temperature = struct.unpack('f', value)[0]
#         print("Température reçue (BLE): {:.2f} °C".format(temperature))
#         # Envoyer les données de température au TcpSenderNode
#         envoyer_temperature_tcp_sender(temperature)
#     except Exception as e:
#         print("Erreur lors du traitement des données reçues:", e)

# def conn_cb(event):
#     """Callback pour les événements de connexion/déconnexion."""
#     if event == Bluetooth.CLIENT_CONNECTED:
#         print('Client connecté')
#     elif event == Bluetooth.CLIENT_DISCONNECTED:
#         print('Client déconnecté')

# def chr1_handler(chr, value):
#     """Callback pour gérer les données reçues dans la caractéristique."""
#     try:
#         if isinstance(value, tuple) and len(value) > 1:
#             value = value[1]  # Obtenir les données binaires
#         handle_client(value)
#     except Exception as e:
#         print("Erreur dans le handler de caractéristique:", e)

# def serveur_tcp(wlan_ip):
#     port = 1234
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((wlan_ip, port))
#     s.listen(1)
#     print('Serveur TCP en écoute sur {}:{}'.format(wlan_ip, port))

#     while True:
#         conn, _ = s.accept()
#         print('Connexion acceptée')

#         try:
#             while True:
#                 data = conn.recv(1024).decode()
#                 if not data:
#                     break

#                 print('Données reçues (Wi-Fi): {}'.format(data.strip()))

#                 if data.startswith('Temperature:'):
#                     temperature = data.split(':')[1].strip()
#                     print('Température reçue (Wi-Fi): {}'.format(temperature))
#                     # Envoyer les données de température au TcpSenderNode
#                     envoyer_temperature_tcp_sender(temperature)

#                 else:
#                     print('Message reçu: {}'.format(data))

#                 conn.send('Message reçu et traité\n'.encode())

#         except OSError as e:
#             print('Erreur de connexion: {}'.format(e))
#         finally:
#             conn.close()  # Fermer la connexion après avoir traité toutes les commandes
#             print('Connexion fermée')

# def serveur_ble():
#     # Initialiser le Bluetooth et diffuser le service BLE
#     bluetooth.set_advertisement(name='FiPy Server', service_uuid=SERVICE_UUID)
#     bluetooth.advertise(True)

#     # Créer un service et une caractéristique
#     srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=1)
#     chr1 = srv1.characteristic(uuid=CHARACTERISTIC_UUID, value=b'')  # Créer une caractéristique vide

#     # Configurer les callbacks pour les événements de lecture et d'écriture
#     chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=chr1_handler)
#     bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

#     print('Serveur BLE démarré et en attente de connexions...')
#     while True:
#         pass  # Maintenir le serveur BLE en marche

# # Configurer le réseau Wi-Fi et démarrer le serveur TCP
# wlan_ip = configurer_reseau()

# # Démarrer les serveurs dans des threads séparés
# thread.start_new_thread(serveur_tcp, (wlan_ip,))
# thread.start_new_thread(serveur_ble, ())

# # Boucle principale pour maintenir les threads en exécution
# while True:
#     time.sleep(1)
####
from network import Bluetooth, WLAN, LoRa
import struct
import socket
import time
from machine import Pin
import _thread as thread
import binascii

# Configuration du réseau Wi-Fi
ssid = 'IoT IMT Nord Europe'
password = '72Hin@R*'

def configurer_reseau():
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid, auth=(WLAN.WPA2, password))

    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)

    print('Connected to Wi-Fi')
    print('IP Address: {}'.format(wlan.ifconfig()[0]))
    return wlan.ifconfig()[0]  # Retourner l'adresse IP

# Configuration LoRa en mode LoRaWAN
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
dev_eui = binascii.unhexlify('0000000000000000')  # DevEUI de ton dispositif
app_eui = binascii.unhexlify('70B3D57ED0012345')  # AppEUI de ton dispositif
app_key = binascii.unhexlify('00000000000000000000000000000000')  # AppKey

# Création d'un socket LoRa
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  # Définir le débit de données (DR)

def verifier_connexion_lora():
    while True:
        if not lora.has_joined():
            print('Reconnexion LoRa en cours...')
            lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=300000)
        time.sleep(60)  # Vérifier toutes les 60 secondes

# Fonction pour envoyer des données de température au TcpSenderNode
def envoyer_temperature_tcp_sender(temperature):
    command = 'Temperature: {}\n'.format(temperature)
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(('10.89.1.86', 1235))  # Adresse IP et port du TcpSenderNode
        conn.send(command.encode())
        print('Température envoyée: {}'.format(command.strip()))
    except Exception as e:
        print('Erreur d\'envoi de température: {}'.format(e))
    finally:
        conn.close()  # Fermer la connexion après envoi

# Fonction pour envoyer la température en LoRa
def envoyer_temperature_lora(temperature):
    try:
        payload = struct.pack('f', temperature)  # Convertir la température en bytes
        s.setblocking(True)
        s.send(payload)
        s.setblocking(False)
        print('Température envoyée (LoRa): {:.2f} °C'.format(temperature))
    except Exception as e:
        print("Erreur lors de l'envoi LoRa:", e)

# Initialisation du Bluetooth
bluetooth = Bluetooth()
bluetooth.init()

# UUIDs pour le service et la caractéristique
SERVICE_UUID = 0xec00
CHARACTERISTIC_UUID = 0xec0e

def handle_client(value):
    """Gère les données reçues d'un client BLE."""
    try:
        # Décompresser les données reçues (format float)
        temperature = struct.unpack('f', value)[0]
        print("Température reçue (BLE): {:.2f} °C".format(temperature))
        # Envoyer les données de température au TcpSenderNode
        envoyer_temperature_tcp_sender(temperature)
        # Envoyer les données de température via LoRa
        envoyer_temperature_lora(temperature)
    except Exception as e:
        print("Erreur lors du traitement des données reçues:", e)

def conn_cb(event):
    """Callback pour les événements de connexion/déconnexion."""
    if event == Bluetooth.CLIENT_CONNECTED:
        print('Client connecté')
    elif event == Bluetooth.CLIENT_DISCONNECTED:
        print('Client déconnecté')

def chr1_handler(chr, value):
    """Callback pour gérer les données reçues dans la caractéristique."""
    try:
        if isinstance(value, tuple) and len(value) > 1:
            value = value[1]  # Obtenir les données binaires
        handle_client(value)
    except Exception as e:
        print("Erreur dans le handler de caractéristique:", e)

def serveur_tcp(wlan_ip):
    port = 1234
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((wlan_ip, port))
    s.listen(1)
    print('Serveur TCP en écoute sur {}:{}'.format(wlan_ip, port))

    while True:
        conn, _ = s.accept()
        print('Connexion acceptée')

        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break

                print('Données reçues (Wi-Fi): {}'.format(data.strip()))

                if data.startswith('Temperature:'):
                    temperature = data.split(':')[1].strip()
                    print('Température reçue (Wi-Fi): {}'.format(temperature))
                    # Envoyer les données de température au TcpSenderNode
                    envoyer_temperature_tcp_sender(temperature)
                    # Envoyer les données de température via LoRa
                    envoyer_temperature_lora(float(temperature))
                else:
                    print('Message reçu: {}'.format(data))

                conn.send('Message reçu et traité\n'.encode())

        except OSError as e:
            print('Erreur de connexion: {}'.format(e))
        finally:
            conn.close()  # Fermer la connexion après avoir traité toutes les commandes
            print('Connexion fermée')

def serveur_ble():
    # Initialiser le Bluetooth et diffuser le service BLE
    bluetooth.set_advertisement(name='FiPy Server', service_uuid=SERVICE_UUID)
    bluetooth.advertise(True)

    # Créer un service et une caractéristique
    srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=1)
    chr1 = srv1.characteristic(uuid=CHARACTERISTIC_UUID, value=b'')  # Créer une caractéristique vide

    # Configurer les callbacks pour les événements de lecture et d'écriture
    chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=chr1_handler)
    bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

    print('Serveur BLE démarré et en attente de connexions...')
    while True:
        time.sleep(1)  # Maintenir le serveur BLE en marche

def serveur_lora():
    while True:
        try:
            s.setblocking(True)
            data = s.recv(256)  # Recevoir jusqu'à 256 octets
            if data:
                temperature = struct.unpack('f', data)[0]
                print("Température reçue (LoRa): {:.2f} °C".format(temperature))
                # Envoyer les données de température au TcpSenderNode
                envoyer_temperature_tcp_sender(temperature)
        except Exception as e:
            print("Erreur lors de la réception LoRa:", e)
        finally:
            s.setblocking(False)
        time.sleep(5)  # Attendre avant la prochaine vérification

# Configurer le réseau Wi-Fi
wlan_ip = configurer_reseau()

# Démarrer les serveurs dans des threads séparés
thread.start_new_thread(serveur_tcp, (wlan_ip,))
thread.start_new_thread(serveur_ble, ())
thread.start_new_thread(serveur_lora, ())  # Démarrer le serveur LoRa

# Démarrer la vérification de la connexion LoRa dans un thread séparé
thread.start_new_thread(verifier_connexion_lora, ())

# Boucle principale pour maintenir les threads en exécution
while True:
    time.sleep(1)
