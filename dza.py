import os

# Afficher le nom de l'utilisateur connecté à l'ordinateur.
print("Nom d'utilisateur connecte a l'ordinateur:", os.getlogin())

# Se déplacer sur le bureau de votre machine.
os.chdir(os.path.expanduser("~/Desktop"))

# Créer un dossier nommé DATA.
if not os.path.exists("DATA"):
    os.mkdir("DATA")
    print("Le dossier DATA a ete cree avec succes")
else:
    print("Le dossier DATA existe deja")

# Tester si DATA est un dossier et qu'il existe. Si oui, vous allez y créer un fichier nommé file.txt, puis écrire dans ce fichier Python est un langage de programmation de hautniveau ».
if os.path.isdir("DATA"):
    with open(os.path.join("DATA", "file.txt"), "w") as f:
        f.write("Python est un langage de programmation de haut niveau.")
    print("Le fichier file.txt a ete cree avec succes")
else:
    print("Ce n'est pas un dossier")

