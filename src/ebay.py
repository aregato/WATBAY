from ebay_token import *
import requests
import json


def get_price(item, amount):
    '''
    Söker eBay med det värdet som Watson har gett och antalet produkter som skall jämföras.
    Returnerar genomsnittspriset för den sökta produkten.
    '''
    token = "Bearer " + get_token()
    payload = {"q": item, "limit": amount}
    headers = {"Authorization": token}
    r = requests.get("https://api.ebay.com/buy/browse/v1/item_summary/search", params=payload, headers=headers)
    result = r.json()
    avg_price = calculate_price(result, amount)
    return round(avg_price)


def calculate_price(result, amount):
    '''
    Räknar ut genomsnittspriset för varorna som eBay returnerade.
    Kollar också ifall det hittades mindre än 10 varor för att undvika fel.
    '''
    total_found = result["total"]
    if total_found < amount:
        amount = total_found
    else:
        pass
    
    total = 0
    count = 0
    while (count < int(amount)):
        total = total + float(result["itemSummaries"][count]["price"]["value"])
        count = count +1
    
    return total/int(amount)
