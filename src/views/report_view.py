"""
Report view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.template_view import get_template, get_param
from controllers.order_controller import get_report_highest_spending_users, get_report_best_selling_products

def show_highest_spending_users():
    """ Show report of highest spending users """
    highest_spending_users = get_report_highest_spending_users()
    rows = [f"""
            <ul>
                <li>ID: {user_id}, Total dépensé: ${total_spent:.2f}</li>
            </ul> """ for user_id, total_spent in highest_spending_users]  
    return get_template(f"""
            <ul>
                <h2>Les plus gros acheteurs</h2>
                {" ".join(rows)}
            </ul>
    """)  

def show_best_sellers():
    """ Show report of best selling products """
    best_selling_products = get_report_best_selling_products()
    rows = [f"""
            <ul>
                <li>{product_name}: {total_sold} vendus</li>
            </ul> """ for product_name, total_sold in best_selling_products]  
    return get_template(f"""
        <ul>
            <h2>Les articles les plus vendus</h2>

                {" ".join(rows)}
            </ul>
    """)  
