from queries.read_order import get_highest_spending_users, get_best_selling_products

def get_report_highest_spending_users():
    """ Get report of highest spending users """
    try :
        return get_highest_spending_users()
    except Exception as e:
        print(e)
        return "Une erreur s'est produite lors de la requête de base de données. Veuillez consulter les logs pour plus d'informations." 

def get_report_best_selling_products():
    """ Get report of best selling products """
    try :
        return get_best_selling_products()
    except Exception as e:
        print(e)
        return "Une erreur s'est produite lors de la requête de base de données. Veuillez consulter les logs pour plus d'informations."