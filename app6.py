from flask import *

app = Flask(__name__)

@app.route('/')
def shop():
    return render_template('/shoppinglist.html')

@app.route('/shoplist', methods=['POST'])
def shoplist():
    name = request.form['item_name']
    id = request.form['item_id']
    quantity = request.form['item_quantity']
    price = request.form['item_price']
    return render_template('/cart.html',
                           name=name,
                           id=id,
                           quantity=quantity,
                           price=price)

if __name__ == '__main__':
    app.debug = True
    app.run()
