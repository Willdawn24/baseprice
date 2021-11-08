from functools import wraps
from flask import request, Blueprint, render_template, jsonify, flash, \
    redirect, url_for
from app import app
from app.control.control import plot

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import Form, StringField, BooleanField, DateTimeField, RadioField, SelectField, TextField, TextAreaField, SubmitField

# catalog = Blueprint('catalog', __name__)

class RegForm(FlaskForm):
    date        = DateTimeField("date",format='%Y-%m-%d', validators=[])
    gender      = RadioField('Gender', choices=[('M','Male'),('F','Female')])
    feedcode    = StringField('feedcode',validators=[DataRequired()])
    submit      = SubmitField("Submit")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = RegForm()
    if request.method == "POST" and form.validate_on_submit():
        return render_template('result.html', form = form)
    return render_template('home.html', notes = [{'data': "data1", 'id': 1}, {'data': "data2", 'id': 1}], form = form)

@app.route('/result', methods=['POST'])
def result():
    form = RegForm()
    fig = plot("")
    return render_template('result.html', form = form, fig = fig)

# @catalog.route('/product/<id>')
# def product(id):
#     product = Product.query.get_or_404(id)
#     return render_template('product.html', product=product)


# @catalog.route('/products')
# @catalog.route('/products/<int:page>')
# def products(page=1):
#     products = Product.query.paginate(page, 10)
#     return render_template('products.html', products=products)


# @catalog.route('/product-create', methods=['GET', 'POST'])
# def create_product():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         price = request.form.get('price')
#         categ_name = request.form.get('category')
#         category = Category.query.filter_by(name=categ_name).first()
#         if not category:
#             category = Category(categ_name)
#         product = Product(name, price, category)
#         db.session.add(product)
#         db.session.commit()
#         flash('The product %s has been created' % name, 'success')
#         return redirect(url_for('catalog.product', id=product.id))
#     return render_template('product-create.html')


# @catalog.route('/product-search')
# @catalog.route('/product-search/<int:page>')
# def product_search(page=1):
#     name = request.args.get('name')
#     price = request.args.get('price')
#     company = request.args.get('company')
#     category = request.args.get('category')
#     products = Product.query
#     if name:
#         products = products.filter(Product.name.like('%' + name + '%'))
#     if price:
#         products = products.filter(Product.price == price)
#     if company:
#         products = products.filter(Product.company.like('%' + company + '%'))
#     if category:
#         products = products.select_from(join(Product, Category)).filter(
#             Category.name.like('%' + category + '%')
#         )
#     return render_template(
#         'products.html', products=products.paginate(page, 10)
#     )


# @catalog.route('/category-create', methods=['POST',])
# def create_category():
#     name = request.form.get('name')
#     category = Category(name)
#     db.session.add(category)
#     db.session.commit()
#     return render_template('category.html', category=category)


# @catalog.route('/category/<id>')
# def category(id):
#     category = Category.query.get_or_404(id)
#     return render_template('category.html', category=category)


# @catalog.route('/categories')
# def categories():
#     categories = Category.query.all()
#     return render_template('categories.html', categories=categories)
