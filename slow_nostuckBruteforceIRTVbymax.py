import subprocess
import time

# Coordonnées des chiffres 0-9 sur l'écran
coordinates = {
    '0': (539, 1561),
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

# Attente de 2 secondes avant de commencer
time.sleep(2)

# Fonction pour générer et taper une combinaison de 4 chiffres
def generate_and_type_combination(combination):
    print("Combinaison:", combination)  # Afficher la combinaison actuelle
    for digit in combination:
        x, y = coordinates[digit]
        # Exécutez la commande ADB pour simuler un clic à la position spécifiée
        subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)])
        time.sleep(0.5)  # Pause de 0,5 seconde entre chaque tape
    time.sleep(2)  # Attente de 2 secondes avant de passer à la combinaison suivante

# Génération et saisie de toutes les combinaisons de 4 chiffres, en commençant à partir de 0000
starting_combination = '0000'
for i in range(10000):
    generate_and_type_combination(starting_combination)
    starting_combination = str(int(starting_combination) + 1).zfill(4)
