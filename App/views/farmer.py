from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity
from flask_login import login_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    get_user,
    get_shop_by_farmer,
    get_listings_by_shop
)

farmer_views = Blueprint('farmer_views', __name__, template_folder='../templates')

@farmer_views.route('/farmer/<id>', methods=['GET'])
# @login_required
def get_farmer_profile(id):
    farmer = get_user(id)
    shop = get_shop_by_farmer(farmer.id)
    listings = get_listings_by_shop(shop.id)
    return render_template('farmer.html', farmer=farmer, shop=shop, listings=listings)

@farmer_views.route('/farmer/<id>/newlisting', methods=['GET'])
def get_new_listing_form(id):
    farmer = get_user(id)
    shop = get_shop_by_farmer(farmer.id)
    listings = get_listings_by_shop(shop.id)
    return render_template('addlisting.html', farmer=farmer, shop=shop, listings=listings)

@farmer_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@farmer_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@farmer_views.route('/api/users', methods=['POST'])
def create_user_action():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})


@farmer_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

@farmer_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')