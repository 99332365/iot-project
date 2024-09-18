# wifi_server.py

from machine import Pin
import network
import socket
import time
from network import WLAN

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

# Fonction pour gérer les connexions TCP et traiter les données reçues
def serveur_tcp():
    wlan = WLAN(mode=WLAN.STA)
    addr = wlan.ifconfig()[0]  # Adresse IP du FiPy
    port = 1234

    # Création d'un socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((addr, port))
    s.listen(1)

    print('Serveur TCP en écoute sur {}:{}'.format(addr, port))

    while True:
        conn, _ = s.accept()
        print('Connexion acceptée')

        try:
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break

                # Traitement des données reçues
                print('Données reçues: {}'.format(data.strip()))

                if data.startswith('Temperature:'):
                    temperature = data.split(':')[1].strip()
                    print('Température reçue: {}'.format(temperature))
                    # Envoyer les données de température au TcpSenderNode
                    envoyer_temperature_tcp_sender(temperature)

                else:
                    print('Message reçu: {}'.format(data))

                # Envoyer une réponse au client après traitement
                conn.send('Message reçu et traité\n'.encode())

        except OSError as e:
            print('Erreur de connexion: {}'.format(e))
        finally:
            conn.close()  # Fermer la connexion après avoir traité toutes les commandes
            print('Connexion fermée')

# Fonction pour envoyer des données de température au TcpSenderNode
def envoyer_temperature_tcp_sender(temperature):
    command = 'Temperature: {}\n'.format(temperature)
    try:
        # Connexion à l'adresse IP du nœud TcpSenderNode et envoi de la commande
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(('10.89.1.86', 1235))  # Adresse IP et port du TcpSenderNode
        conn.send(command.encode())
        print('Température envoyée: {}'.format(command.strip()))
    except Exception as e:
        print('Erreur d\'envoi de température: {}'.format(e))
    finally:
        conn.close()  # Fermer la connexion après envoi

# Configurer le réseau et démarrer le serveur TCP
configurer_reseau()
serveur_tcp()