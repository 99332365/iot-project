# from network import Bluetooth
# import time
# import struct

# # Liste des valeurs de température à envoyer
# temperature_values = [20.0, 21.5, 22.3, 23.1, 24.0, 25.2, 26.1, 27.5, 28.0, 29.3]

# def send_temperature(conn, char):
#     """Envoie les valeurs de température au serveur BLE."""
#     for temp in temperature_values:
#         byte_data = struct.pack('f', temp)  # Convertir la température en format binaire (float)
#         char.write(byte_data)  # Écrire la température dans la caractéristique
#         print("Température envoyée :", temp)
#         time.sleep(5)  # Pause de 5 secondes entre chaque envoi

# # Initialisation du Bluetooth
# bt = Bluetooth()
# print('Démarrage du scan pour les serveurs BLE...')
# bt.start_scan(-1)

# while True:
#     adv = bt.get_adv()
#     if adv:
#         try:
#             if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == "FiPy Server":
#                 conn = bt.connect(adv.mac)
#                 print("Connecté au serveur BLE")

#                 try:
#                     # Recherche des services
#                     services = conn.services()
#                     for service in services:
#                         chars = service.characteristics()
#                         for char in chars:
#                             c_uuid = char.uuid()
#                             if c_uuid == 0xec0e:
#                                 print("Caractéristique trouvée avec UUID:", c_uuid)
#                                 # Envoyer les températures
#                                 send_temperature(conn, char)
#                                 break
#                 except Exception as e:
#                     print("Erreur :", e)
#                 finally:
#                     conn.disconnect()
#                     print("Déconnecté du serveur BLE")
#                 break
#         except Exception as e:
#             print("Erreur de connexion :", e)
#             continue

# bt.stop_scan()



###
from network import Bluetooth
import time
import struct

# Liste des valeurs de température à envoyer
temperature_values = [20.0, 21.5, 22.3, 23.1, 24.0, 25.2, 26.1, 27.5, 28.0, 29.3]

def send_temperature(conn, char):
    """Envoie les valeurs de température au serveur BLE."""
    for temp in temperature_values:
        byte_data = struct.pack('f', temp)  # Convertir la température en format binaire (float)
        char.write(byte_data)  # Écrire la température dans la caractéristique
        print("Température envoyée :", temp)
        time.sleep(5)  # Pause de 5 secondes entre chaque envoi

# Initialisation du Bluetooth
bt = Bluetooth()
print('Démarrage du scan pour les serveurs BLE...')
bt.start_scan(-1)

while True:
    adv = bt.get_adv()
    if adv:
        try:
            if bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == "FiPy Server":
                conn = bt.connect(adv.mac)
                print("Connecté au serveur BLE")

                try:
                    # Recherche des services
                    services = conn.services()
                    for service in services:
                        chars = service.characteristics()
                        for char in chars:
                            c_uuid = char.uuid()
                            if c_uuid == 0xec0e:
                                print("Caractéristique trouvée avec UUID:", c_uuid)
                                # Envoyer les températures
                                send_temperature(conn, char)
                                break
                except Exception as e:
                    print("Erreur :", e)
                finally:
                    conn.disconnect()
                    print("Déconnecté du serveur BLE")
                break
        except Exception as e:
            print("Erreur de connexion :", e)
            continue

bt.stop_scan()















