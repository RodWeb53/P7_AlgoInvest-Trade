import csv
import time


def optimized(budget, file, list_actions=[]):
    """_Méthodes optimisé pour l'analyse des investissement_

    Args:
        budget (_int_): _Budget pouvant être investie_
        file (_text_): _Nom du fichier à lire_
        list_actions (list, optional): _Liste initialisée à vide pour le lancement_
    """
    start_forcebrute = time.time()
    data = read_csv(file)
    for action in data:
        if action[1] >= budget:
            pass
        else:
            budget -= action[1]
            list_actions.append(action)
    end_forcebrute = time.time()
    print(f"Les résultats de calcul pour le fichier {file} est :")
    print(f"La rentabilité sera de {round(sum([i[1] * i[2] for i in list_actions]), 2)} euros",)
    print(f"Le montant investie sera de {round(sum([i[1] for i in list_actions]), 2)} euros",)
    print(f"Avec les actions suivantes : {[i[0] for i in list_actions]}")
    print(f"La durée du calcul est de {str(round(end_forcebrute - start_forcebrute, 4))} secondes \n\n")   

def read_csv(file):
    """Lecture d'un fichier csv pour récupérer les données et les triées

    Args:
        file (_str_): _récupération des données brutes sans la 1° ligne_

    Returns:
        _array_: _tableau avec une ligne pour chaque action_
    """
    with open("data/" + str(file)) as csvfile:
        data = []
        tempory_file = csv.reader(csvfile, delimiter=',')
        for row in tempory_file:
            if row[0] == "name" or float(row[1]) <= 0:
                pass
            else:
                tempory = (row[0], float(row[1]), float(row[2]) / 100)
                data.append(tempory)
        data = sorted(data, key=lambda profit: profit[2], reverse=True )

        return data
    
if __name__ == "__main__":
    
    optimized(500, "dataset2_Python+P7.csv")
    # optimized(500, "forcebrute.csv")
