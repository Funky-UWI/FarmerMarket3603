from operator import index
from flask import Blueprint, jsonify, redirect, render_template, request, send_file, send_from_directory, url_for, flash
from flask_login import current_user, login_required
from App.controllers import *
from flask import session

from uuid import uuid4

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/cart', methods=['GET'])
def get_cart_page():
    cart = get_cart_by_current_user(current_user, session)
    return jsonify(cart.toJSON())

@index_views.route('/cart', methods=['POST'])
def post_order():
    # data = request.json
    data = request.form
    listing_id = int(data['listing_id'])
    listing = get_listing(listing_id)
    cart = get_cart_by_current_user(current_user, session)
    order = create_order(listing=listing, cart=cart)
    return redirect(url_for('index_views.index_page'))

@index_views.route('/session', methods=['GET'])
def get_session():
    cart = None
    if current_user.is_authenticated:
        cart = get_cart_by_session(current_user.id)
        if not cart:
            cart = create_cart(current_user.id)
    else:
        cart = get_cart_by_session(session['uuid'])
        if not cart:
            session['uuid'] = uuid4().hex
            cart = create_cart(session['uuid'])

    return jsonify(cart.toJSON(), session)

@index_views.route('/', methods=['GET'])
def index_page():

    # establish cart existence
    # cart = None
    return jsonify({'session': session['uuid'], 'current_user': current_user.is_authenticated})
    # if current_user.is_authenticated:
    #     cart = get_cart_by_session(current_user.id)
    #     if not cart:
    #         cart = create_cart(current_user.id)
    # else:
    #     if 'uuid' in session:
    #         cart = get_cart_by_session(int(session['uuid']))
    #     if not cart:
    #         session['uuid'] = uuid4().hex
    #         cart = create_cart(int(session['uuid']))
    
    listings = get_all_listings_json()
    # listings.sort(reverse=True, id=id)
    return render_template('feed.html', listings=listings)

@index_views.route('/listings', methods=['GET'])
def search_listings():
    query = request.args
    listings = get_listings_by_name(query['search'])
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
    user = authenticate(data['username'], data['password'])
    if not user:
        flash('Invalid Credentials.')
        return redirect(url_for("index_views.index_page"))

    try:
        login_user(user, remember=False)
    except Exception as e:
        flash(str(e))
        return redirect(url_for("index_views.index_page"))
    # return redirect(url_for("index_views.index_page"))

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
    shop = create_shop(
        data['shopName'],
        data['shopDescription'],
        data['address1'],
        data['address2'],
        user
    )
    # return user.toJSON()

    # create cart
    # cart = create_cart(user.id)

    return redirect(url_for('index_views.login_page', id=user.id))

@index_views.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index_views.index_page'))

@index_views.route('/images/<path>', methods=['GET'])
def get_picture(path):
    # return send_from_directory("./images", 'fig1.png')
    img_dir = "./images"
    # return send_file(os.path.join())