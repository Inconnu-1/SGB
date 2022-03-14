import pickle
import os
import pathlib
class Account :
    accountNumber = 0
    name = ''
    deposit=0
    type = ''
    
    def creationCompte(self):
        self.accountNumber= int(input("Entrez le numéro de compte : "))
        self.name = input("Entrez le nom du titulaire du compte : ")
        self.type = input("Entrez le type de compte courant ou épargne : ")
        self.deposit = int(input("Entrez le montant initial: "))
        print("\n\nCompte crée")
    
    def affichageCompte(self):
        print("Numéro de compte : ",self.accountNumber)
        print("Nom du titulaire du compte : ", self.name)
        print("Type de compte",self.type)
        print("Solde : ",self.deposit)
    
    def modifierCompte(self):
        print("Numéro de compte : ",self.accountNumber)
        self.name = input("Modifier le nom du titulaire du compte :")
        self.type = input("Modifier le type de compte :")
        self.deposit = int(input("Modifier la solde :"))
        
    def deposerMontant(self,amount):
        self.deposit += amount
    
    def retirerMontant(self,amount):
        self.deposit -= amount
    
    def to_String(self):
        print(self.accountNumber, " ",self.name ," ",self.type," ", self.deposit)
    
    def getNumeroCompte(self):
        return self.accountNumber
    def getNomTitulaireCompte(self):
        return self.name
    def getTypeCompte(self):
        return self.type
    def getDepot(self):
        return self.deposit
    

def intro():
    print("\t ______________________")
    print("\t|                      |")
    print("\t| SGB DE MARZOUK ABDEL |")
    print("\t|______________________|")
    print("\n")
    print("appuyez sur la touche entrée")
    input()



def ecrireCompte():
    account = Account()
    account.creationCompte()
    ecrireFichierComptes(account)

def afficherTout():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accountNumber," ", item.name, " ",item.type, " ",item.deposit )
        infile.close()
    else :
        print("Aucun enregistrement à afficher")
        

def afficherSolde(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accountNumber == num :
                print("Your account Solde is = ",item.deposit)
                found = True
    else :
        print("Aucun enregistrement à rechercher")
    if not found :
        print("Aucun enregistrement existant avec ce numéro")

def depotEtRetrait(num1,num2): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist :
            if item.accountNumber == num1 :
                if num2 == 1 :
                    amount = int(input("Entrez le montant à déposer : "))
                    item.deposit += amount
                    print("Votre compte a été mis à jour")
                elif num2 == 2 :
                    amount = int(input("Entrez le montant à retirer : "))
                    if amount <= item.deposit :
                        item.deposit -=amount
                    else :
                        print("Vous ne pouvez pas retirer un montant plus grand que ce que vous possédez")
                
    else :
        print("Aucun enregistrement à rechercher")
    outfile = open('newaccounts.data','wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

    
def supprimerCompte(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = []
        for item in oldlist :
            if item.accountNumber != num :
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data','wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
     
def modifierCompte(num):
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist :
            if item.accountNumber == num :
                item.name = input("Entrez le nom du titulaire du compte : ")
                item.type = input("Entrez le type de compte : ")
                item.deposit = int(input("Entrez le montant : "))
        
        outfile = open('newaccounts.data','wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')
   

def ecrireFichierComptes(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')
    
        
ch=''
num=0
intro()

while ch != 8:
    print("\tMenu principal")
    print("\t1. Nouveau compte")
    print("\t2. Montant du depot")
    print("\t3. Montant du retrait")
    print("\t4. Demande de solde")
    print("\t5. Liste de tous les titulaires de compte")
    print("\t6. Fermer un compte")
    print("\t7. Modifier un compte")
    print("\t8. Sortir")
    print("\tSelectionnez votre choix de 1 a 8 seulement")
    ch = input()
    
    if ch == '1':
        ecrireCompte()
    elif ch =='2':
        num = int(input("\tEntrez le numéro de compte. : "))
        depotEtRetrait(num, 1)
    elif ch == '3':
        num = int(input("\tEntrez le numéro de compte. : "))
        depotEtRetrait(num, 2)
    elif ch == '4':
        num = int(input("\tEntrez le numéro de compte. : "))
        afficherSolde(num)
    elif ch == '5':
        afficherTout()
    elif ch == '6':
        num =int(input("\tEntrez le numéro de compte. : "))
        supprimerCompte(num)
    elif ch == '7':
        num = int(input("\tEntrez le numéro de compte. : "))
        modifierCompte(num)
    elif ch == '8':
        print("\tMerci d'avoir utilisé l'SGB et à la prochaine !")
        break
    else :
        print("Choix invalide")
    
    ch = input("Appuyez sur la touche entrée ")
    