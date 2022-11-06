import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.controllers.listing import create_listing, delete_listing, get_all_listings, get_all_listings_json
from App.controllers.shop import create_shop, get_all_shops, get_all_shops_json

from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import ( 
    create_user, 
    get_all_users_json, 
    get_all_users,
    get_shop
    )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    create_db(app)
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
farmer_cli = AppGroup('farmer', help='Farmer object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@farmer_cli.command("create", help="Creates a farmer")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
@click.argument("first_name", default="robpass")
@click.argument("last_name", default="robpass")
@click.argument("email", default="robpass")
@click.argument("phone", default="robpass")
def create_user_command(username, password, first_name, last_name, email, phone):
    create_user(username, password, first_name, last_name, email, phone)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@farmer_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(farmer_cli) # add the group to the cli


'''
Generic Commands
'''

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)


# ---SHOP GROUP------
shop_cli = AppGroup('shop', help='Shop object commands') 

# flask shop create
@shop_cli.command("create", help="Creates a shop")
@click.argument("name", default="Bob's Shop")
@click.argument("description", default="Welcome to Bob's Shop! We sell most things under the sun!")
@click.argument("address1", default="Corner Trace")
@click.argument("address2", default="Street Avenue")
@click.argument("farmer_id", default="1")
def create_shop_command(name, description, address1, address2, farmer_id):
    create_shop(name, description, address1, address2, farmer_id)
    print(f'{name} created!')

# flask shop list
@shop_cli.command("list", help="Lists listings in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_shops())
    else:
        print(get_all_shops_json())

app.cli.add_command(shop_cli) # add the group to the cli

# ---LISTINGS GROUP------
listing_cli = AppGroup('listing', help='User object commands') 

# flask listing create
@listing_cli.command("create", help="Creates a listing")
@click.argument("name", default="Tomato")
@click.argument("ask_price", default="1.00")
@click.argument("unit", default="Pound")
@click.argument("shop_id", default="1")
def create_listing_command(name, ask_price, unit, shop_id):
    shop = get_shop(shop_id)
    create_listing(name, ask_price, unit, shop)
    print(f'{name} created!')

# flask listing list
@listing_cli.command("list", help="Lists listings in the database")
@click.argument("format", default="string")
def list_listing_command(format):
    if format == 'string':
        print(get_all_listings())
    else:
        print(get_all_listings_json())

# flask listing delete
@listing_cli.command("delete", help="Deletes a listing")
@click.argument("id")
def create_listing_command(id):
    delete_listing(id)
    print(f'{id} deleted!')

app.cli.add_command(listing_cli) # add the group to the cli