import csv
import time


def bruteforce(budget, file):
    """Permet de fixer un budget et d'appeler un fichier

    Args:
        budget (_int_): _Fixe la limite du budget investie_
        file (_str_): _nom du fichier à analyser_
    """
    start_forcebrute = time.time()
    data = read_csv(file)
    result = forcebrute_calculation(budget, data)
    print(result)
    end_forcebrute = time.time()
    print(f"La durée du calcul est de {str(round(end_forcebrute - start_forcebrute, 2))} secondes")

def read_csv(file):
    """Lecture d'un fichier csv pour récupérer les données

    Args:
        file (_str_): _récupération des données brutes_

    Returns:
        _array_: _tableau avec une ligne pour chaque action_
    """
    with open("data/" + str(file)) as csvfile:
        data = []
        tempory_file = csv.reader(csvfile, delimiter=',')
        for row in tempory_file:
                tempory = (row[0], int(float(row[1])), float(row[2]) / 100)
                data.append(tempory)
        return data
    
def forcebrute_calculation(budget, data, list_actions_selected=[]):
    """_summary_

    Args:
        budget (_int_): _Budget pouvant être investie_
        data (_array_): _Données des actions_
        list_actions_selected (list, optional): _Liste initialisée à vide pour le lancement_

    Returns:
        _print_: _Information du résultat des calculs_
    """
    if data:
        
        first_result, list_first_result = forcebrute_calculation(budget, data[1:], list_actions_selected)
        select_action = data[0]
        if select_action[1] <= budget:
            second_result, list_second_result = forcebrute_calculation(budget - select_action[1], data[1:], list_actions_selected + [select_action])
            
            if first_result < second_result:
                return second_result, list_second_result
        return first_result, list_first_result
    else:

        return f"La rentabilité sera de {round(sum([i[1] * i[2] for i in list_actions_selected]), 2)} euros", \
        f"le budget maximum investi sera de : {sum([i[1] for i in list_actions_selected])} euros, " \
        f"avec les actions suivantes : {[i[0] for i in list_actions_selected]}"


if __name__ == "__main__":
    
    bruteforce(500, "forcebrute.csv")


