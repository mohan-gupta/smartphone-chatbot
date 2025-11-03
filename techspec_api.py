import requests

from cfg import techspec_api_id, techspec_api_key

def get_smartphone_id(smartphone_name: str):
    url = f"https://api.techspecs.io/v5/products/search?query={smartphone_name}&keepCasing=true&page=0&size=10"

    headers = {
        "accept": "application/json",
        "x-api-id": techspec_api_id,
        "x-api-key": techspec_api_key
    }
    
    response = requests.get(url=url, headers=headers)
    data = response.json()
    
    product_id = data["data"][0]["Product"]["id"]
    
    return product_id


def get_smartphone_data(phone_id):
    url = f"https://api.techspecs.io/v5/products/{phone_id}?lang=en"

    headers = {
        "accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "x-api-id": techspec_api_id,
        "x-api-key": techspec_api_key
    }
    
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def parse_product_details(details):
    if details.get("data") is None:
        return []
    
    manufacturer = details["data"]["Product"]["Manufacturer"]
    brand = details["data"]["Product"]["Brand"]
    model = details["data"]["Product"]["Model"]
    version = details["data"]["Product"]["Version"]
    
    design = details["data"]["Design"]
    
    key_aspects = details["data"]["Key Aspects"]
    
    details_obj = {
        "brand": brand,
        "model": model,
        "version": version,
        "key_aspects": key_aspects,
        "desing": design,
        "maufacturer": manufacturer
    }
    
    return details_obj


def get_smartphone_details(smartphone_name: str):
    phone_id = get_smartphone_id(smartphone_name=smartphone_name)
    
    phone_details = get_smartphone_data(phone_id=phone_id)
    
    details = parse_product_details(phone_details)
    
    return details
