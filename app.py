from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {'id': 1, 'name': 'Product A', 'description': 'Description of Product A'},
    {'id': 2, 'name': 'Product B', 'description': 'Description of Product B'}
]

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
