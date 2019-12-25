# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:34:25 2019

@author: NGH5KOR
"""
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


stores = [
        {
            "name":"My wonderful Store",
            "items": [
                    {
                        "name": "My Item",
                        "price":15.99
                    }
                    
                    ]
        }
        ]
            
@app.route('/')
def home():
    return render_template('index.html')            

@app.route('/store', methods = ['POST'])
def create_store():
    request_data  =request.get_json()
    print("entered", request_data)
    new_store = {
            'name': request_data['name'],
            'items' : []
            }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    
    for store in stores:
        if (store['name'] == name):
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store')
def get_stores():
    #return jsonify(dict(stores))
    return jsonify({'stores' : stores})

@app.route('/store/<string:name>/items', methods=['POST'])
def create_item_in_storename(name):
    request_data  =request.get_json()
    for store in stores:
        if (store['name'] == name):
            new_item = {
            'name': request_data['name'],
            'items' : request_data['price']
            }
            stores['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/items')
def get_item_in_store(name):
    for store in stores:
        if (store['name'] == name):
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})

if __name__ == "__main__":
    app.run()