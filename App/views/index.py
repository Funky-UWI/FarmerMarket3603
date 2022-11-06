from operator import index
from flask import Blueprint, jsonify, redirect, render_template, request, send_from_directory, url_for
from flask_login import current_user, login_required
from App.controllers import *

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@login_required
@index_views.route('/', methods=['GET'])
def index_page():
    listings = get_all_listings_json()
    return render_template('feed.html', listings=listings)

@index_views.route('/shops', methods=["GET"])
def get_all_shops():
    shops = get_all_shops_json()
    return jsonify(shops)
    # return render_template('store.html', shops=shops)

@index_views.route('/shop/<id>', methods=["GET"])
def get_shop_page(id):
    shop = get_shop(id)
    listings = get_listings_by_shop(id)
    return render_template('store.html', shop=shop, listings=listings)

@index_views.route('/login', methods=["POST"])
def login():
    data = request.form
    # return jsonify(data)
    try:
        user = authenticate(data['username'], data['password'])
        login_user(user, remember=False)
    except:
        return 400
    # return redirect(url_for("index_views.index_page")), 200

    # if next:
    #     return redirect(next)
    return redirect(url_for('farmer_views.get_farmer_profile', id=user.id))

@index_views.route('/login', methods=["GET"])
def login_page():
    return render_template("login.html")

@index_views.route('/signup', methods=["GET"])
def signup_page():
    return render_template("signup.html")

@index_views.route('/signup', methods=["POST"])
def signup():
    data = request.form
    # return jsonify(data)
    user = create_user(
        data['username'], 
        data['password'], 
        data['firstName'], 
        data['lastName'], 
        data['email'], 
        data['phone']
    )
    # create shop
    # shop = create_shop(

    # )
    # return user.toJSON()
    return redirect(url_for('farmer_views.get_farmer_profile', id=user.id))

@index_views.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('feed.html')

@index_views.route('/images/<path>', methods=['GET'])
def get_picture(path):
    return send_from_directory('../', 'images', 'tomato.png')