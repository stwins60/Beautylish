import requests
import json
import unittest
import app
def test_get_data():
    url = "https://www.beautylish.com/rest/interview-product/list"
    data = app.get_data(url)
    assert type(data) == type(dict())

def test_get_product_list():
    url = "https://www.beautylish.com/rest/interview-product/list"
    data = app.get_data(url)
    product_list, brand_name, product_name, product_price = app.get_product_list(data)
    assert product_list != None
    assert "Anvil" in product_name
    assert "Acme" in brand_name
    assert "99.99" in product_price

def test_get_unique_brands():
    url = "https://www.beautylish.com/rest/interview-product/list"
    data = app.get_data(url)
    product_list, brand_name, product_name, product_price = app.get_product_list(data)
    unique_brands = app.get_unique_brands(brand_name)
    assert int(len(unique_brands)) > 0

def test_get_unique_products():
    url = "https://www.beautylish.com/rest/interview-product/list"
    data = app.get_data(url)
    product_list, brand_name, product_name, product_price = app.get_product_list(data)
    unique_products = app.get_unique_products(product_name)
    assert int(len(unique_products)) > 0

def test_get_average_price():
    # s = ['123.45', '123.45', '10.00', '99.99', '10.00', '123.45']
    url = "https://www.beautylish.com/rest/interview-product/list"
    data = app.get_data(url)
    product_list, brand_name, product_name, product_price = app.get_product_list(data)
    avg = app.get_average_price(product_price)
    assert avg > 10.00
    