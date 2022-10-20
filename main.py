def variable():
    prenom = "Pierre"
    age = 20
    majeur = True
    compte_en_banque = 20135.384
    amis = ["Marie", "Julien", "Adrien"]
    parents = ("Marc", "Caroline")
    print(prenom, age, majeur, compte_en_banque, amis, parents)
    
variable()

def exo5():
    a = 2
    b = 6
    c = 3
    print(a, "+", b, "+", c)
    
exo5()

def exo6():
    prenom = "Pierre"
    if(type(prenom) == str):
        print("C'est un Str")
    prenom = 0
    if isinstance(prenom, int):
        print("Variable est une chaine")
        
exo6()
#Faire un programme qui permet à l'utilisateur de choisir le type à tester

def exo7():
    phrase = "Bonjour les amis"
    nouvelle_phrase = phrase.replace("Bonjour", "Salut")
    print(nouvelle_phrase)
exo7()
#Un programme qui demande a l utilisateur le nombre d'occurence qu"il veut retirer et aussi lui demander ce qu'il veut enlever 

def exo8():
    liste = ["Python", "C++", "HTML", "Java"]
    for i in range(len(liste)):
        print(liste[i])
exo8()

def exo9():
    chaine = "pomme, abricot, cerise, fraise, orange"
    liste = chaine.split(", ")
    liste.sort()
    print(liste)
exo9()

def exo11():
    liste = []
    for i in range(10, 101):
        liste.append(i)
    print(liste)
exo11()

def exo12():
    liste = []
    for i in range(1, 101):
        liste.append(i*2)
    print(liste)
exo12()

def exo13():
    import random
    lancer = int(input("Lancer votre des : ")) 
    des = []
    for i in range(lancer):
        de = random.randint(1, 6)
        des.append(de)
    somme = sum(des)
    moy_des = somme / lancer
    print(des, moy_des)
exo13()

def exo14():
    lettre_a_chercher = "a"
    phrase = "voila les amis. Alors ca va ?"
    print(phrase.lower().count(lettre_a_chercher))
exo14()

def exo15():
    liste = [100, 50, 65, 82, 23]
    for i in range(len(liste)):
        if i%2==0 : 
            print(liste[i])
exo15()