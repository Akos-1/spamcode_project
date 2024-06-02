#!/usr/bin/env python3

from flask import Blueprint, request, jsonify
from models import db, Brand, Category, ProductType, ProductName

api = Blueprint('api', __name__)

# Brand transactions
@api.route('/brands', methods=['GET', 'POST'])
def handle_brands():
    if request.method == 'GET':
        brands = Brand.query.all()
        return jsonify([brand.name for brand in brands])
    if request.method == 'POST':
        new_brand = Brand(name=request.json['name'])
        db.session.add(new_brand)
        db.session.commit()
        return jsonify({'message': 'Brand created successfully'}), 201

@api.route('/brands/<int:id>', methods=['PUT', 'DELETE'])
def handle_brand(id):
    brand = Brand.query.get_or_404(id)
    if request.method == 'PUT':
        brand.name = request.json['name']
        db.session.commit()
        return jsonify({'message': 'Brand updated successfully'})
    if request.method == 'DELETE']:
        db.session.delete(brand)
        db.session.commit()
        return jsonify({'message': 'Brand deleted successfully'})

# Category transactions
@api.route('/categories', methods=['GET', 'POST'])
def handle_categories():
    if request.method == 'GET']:
        categories = Category.query.all()
        return jsonify([category.name for category in categories])
    if request.method == 'POST':
        new_category = Category(name=request.json['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify({'message': 'Category created successfully'}), 201

@api.route('/categories/<int:id>', methods=['PUT', 'DELETE'])
def handle_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'PUT']:
        category.name = request.json['name']
        db.session.commit()
        return jsonify({'message': 'Category updated successfully'})
    if request.method == 'DELETE']:
        db.session.delete(category)
        db.session.commit()
        return jsonify({'message': 'Category deleted successfully'})

# ProductType transactions
@api.route('/product_types', methods=['GET', 'POST'])
def handle_product_types():
    if request.method == 'GET']:
        product_types = ProductType.query.all()
        return jsonify([product_type.name for product_type in product_types])
    if request.method == 'POST':
        new_product_type = ProductType(name=request.json['name'])
        db.session.add(new_product_type)
        db.session.commit()
        return jsonify({'message': 'ProductType created successfully'}), 201

@api.route('/product_types/<int:id>', methods=['PUT', 'DELETE'])
def handle_product_type(id):
    product_type = ProductType.query.get_or_404(id)
    if request.method == 'PUT']:
        product_type.name = request.json['name']
        db.session.commit()
        return jsonify({'message': 'ProductType updated successfully'})
    if request.method == 'DELETE']:
        db.session.delete(product_type)
        db.session.commit()
        return jsonify({'message': 'ProductType deleted successfully'})

# ProductName transactions
@api.route('/product_names', methods=['GET', 'POST'])
def handle_product_names():
    if request.method == 'GET']:
        product_names = ProductName.query.all()
        return jsonify([product_name.name for product_name in product_names])
    if request.method == 'POST']:
        new_product_name = ProductName(
            name=request.json['name'],
            brand_id=request.json['brand_id'],
            category_id=request.json['category_id'],
            product_type_id=request.json['product_type_id']
        )
        db.session.add(new_product_name)
        db.session.commit()
        return jsonify({'message': 'ProductName created successfully'}), 201

@api.route('/product_names/<int:id>', methods=['PUT', 'DELETE'])
def handle_product_name(id):
    product_name = ProductName.query.get_or_404(id)
    if request.method == 'PUT']:
        product_name.name = request.json['name']
        product_name.brand_id = request.json['brand_id']
        product_name.category_id = request.json['category_id']
        product_name.product_type_id = request.json['product_type_id']
        db.session.commit()
        return jsonify({'message': 'ProductName updated successfully'})
    if request.method == 'DELETE']:
        db.session.delete(product_name)
        db.session.commit()
        return jsonify({'message': 'ProductName deleted successfully'})
