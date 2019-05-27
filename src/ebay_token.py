import requests
import json


def get_token():
    '''
    Hämtar den unika token som behövs för att söka eBay.
    '''
    headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic RGF2aWRIdXItV0FUQkFZLVBSRC1jNWQ3NGZjOGYtZDU4YTBkMzY6UFJELTVkNzRmYzhmNTAzOC1jZjNiLTRmYjctOGVmYi05NTIw"}
    payload = {"grant_type": "client_credentials", "redirect_uri": "David_Hurtig-DavidHur-WATBAY-yhtouj", "scope": "https://api.ebay.com/oauth/api_scope"}
    r = requests.post("https://api.ebay.com/identity/v1/oauth2/token", headers=headers, data=payload)
    result = r.json()
    token = result["access_token"]
    
    return token
