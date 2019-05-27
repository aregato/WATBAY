from watson import *
from ebay import *

def watson_ebay():
    '''
    Returnerar en lista med två sorterade dictionaries där de är sorterade efter den med högst score kommer först. 
    '''
    watson_result = classify()
    
    name_a = get_name(watson_result, 0)
    name_b = get_name(watson_result, 1)
    score_a = get_score(watson_result, 0)
    score_b = get_score(watson_result, 1)

    amount = 10
    
    name_a_price = get_price(name_a, amount)
    name_b_price = get_price(name_b, amount)

    dict_1 = {"item": name_a, "avg_price": name_a_price, "score": score_a, "link": "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.X" + name_a.replace(" ", "+") + ".TRS0&_nkw=" + name_a.replace(" ", "+") + "&_sacat=0"}
    dict_2 = {"item": name_b, "avg_price": name_b_price, "score": score_b, "link": "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2050601.m570.l1313.TR0.TRC0.H0.X" + name_b.replace(" ", "+") + ".TRS0&_nkw=" + name_b.replace(" ", "+") + "&_sacat=0"}

    result = compare_score(dict_1, dict_2)
    
    return result

def compare_score(dict_1, dict_2):
    '''
    Jämför resultatens score och sorterar den med högst score först.
    Returnerar en sorterad lista med två dictionaries i.
    '''
    result = []
    
    if dict_1.get("score") >= dict_2.get("score"):
        result.append(dict_1)
        result.append(dict_2)
    else:
        result.append(dict_2)
        result.append(dict_1)

    return result

def generate_json(result):
    '''
    Genererar och returnerar json av listan med resultaten.
    '''
    json_data = json.dumps(result)
    return json_data

