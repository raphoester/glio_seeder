from pymongo import MongoClient
from dotenv import load_dotenv
import os
from pprint import pprint
from random import randint 

idsEcoles = ["fkgrq6gr5", "z2ea323fd5e", "f45eze4z59", "h8r9kjh56", "d1za327e", "zea13245z"]
villes = ["Paris", "Marseille", "Lyon", "Strasbourg", "Nantes", "Toulouse", "Bordeaux"]
idsAdmins = ["e456za", "za5ds6e", "56d6s648f", "d45dfdds30", "f1ds12z","nb55de", "123sqdvu4i", "e5re6x2a3"]


def randListe(liste):
    return liste[randint(0, (len(liste)-1))]



def seed_ecoles(db):
    nomsEcoles = ["Ynov", "Epitech", "ief2i", "HEC", "Epita", "42", "Hetic"]
    idsEcoles = ["fkgrq6gr5", "z2ea323fd5e", "f45eze4z59", "h8r9kjh56", "d1za327e", "zea13245z"]

    
    for i in range(20):
        ecole = {
            'Id':  randListe(idsEcoles),
            'School': randListe(nomsEcoles),
            'City': [
                    randListe(villes),
                    randListe(villes),
                    randListe(villes)

                ],
            'Admin': [
                randListe(idsAdmins),
                randListe(idsAdmins),
                randListe(idsAdmins)
            ],
        }
        result=db.ecole.insert_one(ecole)
        print(f'Creation de l\'école #{i} sur 20 : {result.inserted_id}')
    print("Création terminée")

def seed_admins(db):
    prenoms = ["Ynov", "Epitech", "ief2i", "HEC", "Epita", "42", "Hetic"]
    noms = ["fkgrq6gr5", "z2ea323fd5e", "f45eze4z59", "h8r9kjh56", "d1za327e", "zea13245z"]
    domaines = ["Paris", "Marseille", "Lyon", "Strasbourg", "Nantes", "Toulouse", "Bordeaux"]
    mdps = ["e456za", "za5ds6e", "56d6s648f", "d45dfdds30", "f1ds12z","nb55de", "123sqdvu4i", "e5re6x2a3"]
    roles = ["admin"]

    for i in range(40):
        nom = randListe(noms)
        prenom = randListe(prenoms)
        dom = randListe(domaines)
        admin = {
            'id': randListe(idsAdmins),
            'cred':{
                'lastname': nom,
                'firstname': prenom,
                'email': f"{prenom}.{nom}@{dom}",
                'password': randListe(mdps),
            },
            'schools' : [
                randListe(idsEcoles),
                randListe(idsEcoles),
                randListe(idsEcoles)
            ],
            'cities': [
                randListe(villes),
                randListe(villes),
                randListe(villes)
            ],
            'Role': randListe(roles)
        }
        result=db.admin.insert_one(admin)
        print(f'Création de l\'admin #{i} sur 20 : {result.inserted_id}')
    print("Création terminée")


def main():
    load_dotenv()
    client = MongoClient(os.environ["MongoDB"])
    # db=client.os.environ["nom_DB"]
    db=client.MOCK_V2
    seed_ecoles(db)
    seed_admins(db)
    
    

    # pprint(db.command("serverStatus"))

if __name__ == "__main__":
    main()
