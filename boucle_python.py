for number in ["okok", 3, 1]:
    # ici je lis un par un les valeurs de ma liste
    print(number)

a = 0
b = 5

a = a + 1
while a < b:
    print(a)

# La fonction range renvoie une liste
# range(7) = [0,1,2,3,4,5,6]
for x in range(1, 11):
    print(x * 34)

# Cette fonction va afficher la table de 10 du chiffre que l'on aura renseigné en parametre
# Par exemple tableDe10(3) => la variable unChiffre sera égale a 3
def tableDe10(unChiffre):
    for x in range(1, 11):
        print(x * unChiffre)


# On fais appel la fonction précédement créer à la ligne 19
tableDe10(3)

# Syntaxe pour la création d'une liste
t = [2, 3]

# Synxtaxe pour lire un seul élement d'une liste => t[1]
print(t[1])
