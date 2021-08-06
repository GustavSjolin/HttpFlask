from flask import Flask,jsonify,request,render_template

app = Flask(__name__)


my_db = [
    {
        'name':'First',
        'items':[
            {
                'name':'banana',
                'price': 9.99
            }
        ]
    },
    {
        'name': 'Second',
        'items':[
            {
                'name':'Car',
                'price': 146399.00
            }
        ]
    }
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store')
def get_stores():
    return jsonify({'Stores': my_db})


@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[],
    }
    my_db.append(new_store)
    return jsonify(new_store)



@app.route('/store/<string:name>')
def get_store(name):
    for store in my_db:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'error'})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in my_db:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'error'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in my_db:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'error'})


app.run(port = 8080)




