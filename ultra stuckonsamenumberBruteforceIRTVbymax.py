import subprocess
import time

# Coordonnées des chiffres 0-9 sur l'écran
coordinates = {
    '0': (539, 1561),  # Coordonnées pour '0'
    '1': (272, 722),
    '2': (525, 746),
    '3': (808, 725),
    '4': (253, 1014),
    '5': (520, 1012),
    '6': (801, 1031),
    '7': (278, 1332),
    '8': (529, 1287),
    '9': (799, 1294)
}

# Attente de 4 secondes avant de commencer
time.sleep(4)

# Génération de combinaisons de 4 chiffres de 0000 à 9999
for i in range(0000, 10000):
    combination = str(i).zfill(4)  # Convertir en chaîne de 4 chiffres avec des zéros à gauche
    print("Combinaison:", combination)  # Afficher la combinaison actuelle
    for digit in combination:
        x, y = coordinates[digit]
        # Exécutez la commande ADB pour simuler un clic à la position spécifiée
        subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])
    if i < 9999:
        time.sleep(4)  # Attente de 4 secondes avant de passer à la combinaison suivante
