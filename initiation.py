#Initiation anla programmation Orientee Objet
#Raisonnement
#Personne( class)
#   possède des Données: nom,age
#   Peut faire des acrtions: DemanderNom(), sePresenter()

#---Definition---
# Heritage

class Etre_vivant:
    Espece_etre_vivant= ""

    def afficher_espece(self):
        print("Espece: " +self.Espece_etre_vivant)



class Chat(Etre_vivant): # Un chat etant un etre vivant, il herite ainsi du code de la class parente

    Espece_etre_vivant = "Animal, Felin"
    def __init__(self, nom : str=""):
        self.nom = nom
    def SePresenter(self):
        print("Je suis un chat, Je m'appelle: " +self.nom)

    #def afficher_espece(self):
       # print("Espece: " +self.Espece_etre_vivant)

class Personne(Etre_vivant): # De meme l'homme est un être vivant
    Espece_etre_vivant = "Etre Humain" # Variable de classe (commune a chaque instance)
    def __init__(self, nom: str, age: int=0):     #Constructeur; self sert de conteneur pour nos attributs.

        self.nom = nom                               # Creation d'une variable d'instance: les parametres stockes dans self.parametre seront accessible dans les objets a l'appel de self. La bonne pratique est de les céer TOUJOURS au niveau du constructeur parce que sinon il faudra faire attention a l'ordre d'appel des fonctions 

        self.age = age
        print("Constructeur Personne  " +self.nom)

    #def DemanderNom(self):
        #self.nom = input("Entrez votre nom: ")

    def EstMajeur(self):
        return self.age >= 18

    def SePresenter(self):
        info_personne = "Bonjour, je m'appelle " +self.nom

        if self.age !=0:
            info_personne += ", j'ai " + str(self.age) +"ans"
        print (info_personne)

        if self.age !=0:
            if self.EstMajeur():
                print("je suis majeur")
            else:
                print("je suis mineur")
        #print("Est majeur: ", self.EstMajeur())
    
   # def afficher_espece(self): #commune a l'hoe et au chat
      #  print("Espece: " +self.Espece_etre_vivant)

class Etudiant(Personne): # Etudiant hérite de Personne car Etudiant --> Personne
    def __init__(self, nom: str, age: int, Etude: str):
        super().__init__(nom,age)
        self.etude = Etude

    def SePresenter(self):

        super().SePresenter() # appel de la fonction SePresenter de la classe parente
        print("Je suis Etudiant en: " +self.etude)
    
#---Utilisation---   

#personne1 = Personne("Jean", 30) #les instances herite de la class Personne; ayant declaré un parametre dans la classe, les objet doivent être appaelee avec ce parametre sinon on reçoit un msg d'erreur
#personne2 = Personne("Paul", 15)
#personne3 = Personne()
#personne4 = Personne(age=20)

liste_personnes = [Personne("Jean", 30),
                   Personne("Paul", 15),]
liste_personnes[0].Espece_etre_vivant = "Mutant"
#Personne.Espece_etre_vivant = "Alien"
#for i in range (len(liste_personnes)):
    #liste_personnes[i].SePresenter()
for personne in liste_personnes:
    personne.SePresenter()
    personne.afficher_espece()
    print()

chat1 = Chat("Garfield")
chat1.SePresenter()
chat1.afficher_espece()
print()

chat2 = Chat()
chat2.SePresenter()
chat2.afficher_espece()
print()

etudiant1 = Etudiant("Vamara",14,"Communication")
etudiant1.SePresenter()
etudiant1.afficher_espece() # Ayant herité de Personne, Etudiant hérite aussi de la classe grand-parente.


