import requests as r
import json
import pytest

# get data from the url
def get_data(url):
    try:
        response = r.get(url)
        data = json.loads(response.text)
    except:
        print("Error: unable to fetch data")

    return data

def shouldShowItem(item):
    return (not item['hidden']) and (not item['deleted'])

# get product list from the data
def get_product_list(data):
    products = data
    product_list = []
    brand_name = []
    product_name = []
    product_price = []
    # for p in products['products']:
    product = [x for x in filter(shouldShowItem, products['products'])]
        # if p['hidden'] == False or p['deleted'] == False:
    for p in product:
        brand_name.append(p['brand_name'])
        product_name.append(p['product_name'])
        product_price.append(str(p['price'].lstrip('$')))

    # map the brand, product, and price to a list
    product_list = list(zip(brand_name, product_name, product_price))

    # sort the list by price if two products have the same price, sort by product name ascending
    product_list.sort(key=lambda x: (x[2], x[1]), reverse=False)

    # display once if the same product is found
    product_list = list(dict.fromkeys(product_list))
    return product_list, brand_name, product_name, product_price

# get the unique brands
def get_unique_brands(brand_name):
    unique_brands = []
    for b in brand_name:
        if b not in unique_brands:
            unique_brands.append(b)
    return unique_brands

# get the unique products
def get_unique_products(product_name):
    unique_products = []
    for p in product_name:
        if p not in unique_products:
            unique_products.append(p)
    return unique_products

# get the average price
def get_average_price(product_price):
    sum = 0
    # calculate the average price
    try:
        for i in product_price:
            sum += float(i)
        avg = sum / len(product_price)
        avg = round(avg, 2)
    except ZeroDivisionError:
        avg = 0

    return avg

# # test the functions
def main():    
    url = "https://www.beautylish.com/rest/interview-product/list"
    data = get_data(url)
    product_list, brand_name, product_name, product_price = get_product_list(data)
    unique_brands = get_unique_brands(brand_name)
    unique_products = get_unique_products(product_name)
    avg = get_average_price(product_price)
    count = 0
    print("The list of products sorted by price:")
    for p in product_list:
        print(p)
   
    print("The total number of unique products: {}".format(len(product_list)))
    print("The total number of unique brands: {}".format(len(unique_brands)))
    print("The average price of products: {}".format(avg))

# run the test
main()

