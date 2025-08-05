from flask import Flask, render_template

app = Flask(__name__)

PRODUCT = [{
    'id': 1,
    'product': 'Hardware',
    'Name': 'Ardean Drone',
    'Description': 'N/A'
}, {
    'id': 2,
    'product': 'Software',
    'Name': 'QuMapp',
    'Description': 'N/A'
}]


@app.route('/')
def homepage():
  return render_template('home.html')


@app.route('/about')
def product_page():
  return render_template('product.html', products=PRODUCT)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
