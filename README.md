# BruteForce IR TV Code

## Description
Ce projet vise à effectuer un Bruteforce sur une télévision bloqué via un code parental (4 chiffres) en utilisant de l'Infrarouge.

## Outils Utilisés
- **ZazaRemote** (Application Android)
  - [Lien de Téléchargement](https://play.google.com/store/apps/details?id=com.tiqiaa.remote&hl=fr&gl=US)

- **Python** (Logiciel)
  - [Lien de Téléchargement](https://www.python.org/)

- **Screen Coordinates** (Application Android)
  - [Lien de Téléchargement](https://play.google.com/store/apps/details?id=com.app.firescript.screencoordinates&hl=en_US)

- **SDK Platform Tools** (Logiciel)
  - [Lien de Téléchargement](https://developer.android.com/tools/releases/platform-tools)

## Appareils Nécessaires

- **Smartphone Android** (compatible avec l'IR) avec un câble USB
  - Assurez-vous que le téléphone est connecté à l'ordinateur à l'aide d'ADB.
 
- **Ordinateur**
  - Système d'exploitation Windows 10 minimum.

## Annexe Importante
- Le script Python peut ne pas fonctionner sur tous les smartphones en raison de dimensions différentes. 
- L'utilisation de l'application "Screen Coordinates" est recommandée si le script ne tape pas aux emplacement des chiffres à l'écran. 
- Vous devrez modifier le script Python avec les paramètres obtenus via Screen Coordinates (valeurs x, y pour différents chiffres).

## Utilisation

### 1. Sur l'Ordinateur
- Installer Python et SDK Platform Tools.

### 2. Sur le Smartphone Android
- Installer ZazaRemote et Screen Coordinates.

### 3. Connecter le Smartphone Android à l'Ordinateur
- Connectez le Smartphone Android à l'ordinateur à l'aide d'un câble USB et assurez-vous que le mode développeur est activé sur votre Smartphone Android.

### 4. Sur l'Ordinateur
- Ouvrez l'invite de commande Windows.
- Naviguez vers le répertoire où SDK Platform Tools est installé (exemple : `cd C:\Users\*VotreNomDutilisateur*\Downloads\platform-tools_r34.0.5-windows\platform-tools`).
- Exécutez adb.exe depuis le répertoire platform-tools (exemple : `adb.exe devices`, `adb.exe devices -l`).
- En cas de problème, utilisez : `adb.exe kill-server`.

### 5. Sur le Smartphone Android
- Ouvrez ZazaRemote, configurez-le avec votre télévision IR en plaçant le smartphone devant la lumière infrarouge de la télévision jusqu'à obtenir la bonne fréquence.
  ![Capture d'écran ZazaRemote](https://github.com/maxaft/BruteforceIRTVcode/assets/150711329/d24c120a-b232-4f2c-a463-52c716fde357)
- Cliquez sur les chiffres "123" en bas à gauche de l'écran.
  ![Capture d'écran ZazaRemote](https://github.com/maxaft/BruteforceIRTVcode/assets/150711329/1b3a545c-62b3-475e-ab90-301c1fa7d776)

### 6. Sur l'Ordinateur
- Déplacez le script Python dans le répertoire "platform-tools".
  ![Capture d'écran du déplacement du script](https://github.com/maxaft/BruteforceIRTVcode/assets/150711329/4d04e2ed-5a01-453e-a896-2d56109cd17f)
- Depuis l'invite de commande, tapez : `slow_nostuckBruteforceIRTVbymax.py`.

- Pour arrêter le script, utilisez la combinaison de touches : `Ctrl + C`.

### 7. Fin
- Attendez jusqu'à obtenir le bon code.

## Note Importante
Ce projet est destiné à des fins éducatives et de test uniquement. Assurez-vous d'avoir le droit légal d'utiliser et de tester les codes IR sur les appareils concernés.
