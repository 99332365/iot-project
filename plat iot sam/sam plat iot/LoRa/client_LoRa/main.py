import sys
from machine import Pin
import network
import socket
import time
import struct
import binascii
from network import LoRa

# Configuration LoRa en mode LoRaWAN
def configurer_lora():
    lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    dev_eui = binascii.unhexlify('0000000000000000')  # Remplacer par ton DevEUI
    app_eui = binascii.unhexlify('70B3D57ED0012345')  # Remplacer par ton AppEUI
    app_key = binascii.unhexlify('00000000000000000000000000000000')  # Remplacer par ton AppKey

    lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

    while not lora.has_joined():
        print('Connexion LoRa en cours...')
        time.sleep(2)

    print('Connecté à LoRaWAN')
    return lora

# Création d'un socket LoRa
def configurer_socket_lora(lora):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  # Définir le débit de données (DR)
    return s

# Liste de 10 valeurs de température pour les tests
temperatures = [25.0, 23.5, 29.3, 15.1, 12.0, 11.2, 13.1, 26.5, 32.0, 50.3]

def envoyer_temperature_lora(s, temperature):
    try:
        payload = struct.pack('f', temperature)  # Convertir la température en bytes
        s.setblocking(True)
        s.send(payload)
        s.setblocking(False)
        print('Température envoyée (LoRa): {:.2f} °C'.format(temperature))
    except Exception as e:
        print("Erreur lors de l'envoi LoRa:", e)

def envoyer_donnees(s):
    index = 0
    while True:
        try:
            # Obtenir la température à envoyer
            temperature = temperatures[index]

            # Envoyer les données
            envoyer_temperature_lora(s, temperature)

            # Passer à la température suivante
            index = (index + 1) % len(temperatures)

            time.sleep(5)  # Attendre 5 secondes avant d'envoyer à nouveau

        except Exception as e:
            print('Erreur d\'envoi de données: {}'.format(e))

# Configurer LoRa et démarrer l'envoi des données
lora = configurer_lora()
socket_lora = configurer_socket_lora(lora)
envoyer_donnees(socket_lora)
