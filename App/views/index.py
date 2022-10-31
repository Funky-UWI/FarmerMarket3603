from operator import index
from flask import Blueprint, redirect, render_template, request, send_from_directory
from App.controllers import *

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    listings = get_all_listings_json()
    return render_template('feed.html', listings=listings)

@index_views.route('/shop', methods=["GET"])
def shop_page():
    shop = get_all_shops_json()
    return render_template('store.html', shop=shop)

@index_views.route('/login', methods=["POST"])
def login():
    data = request.json
    user = authenticate(data['username'], data['password'])
    return user.toJSON(), 200

@index_views.route('/login', methods=["GET"])
def login_page():
    return render_template("login.html")

@index_views.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return render_template('feed.html')