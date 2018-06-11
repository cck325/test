import csv
import os


def menu(username="@prof-rossetti", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product."""
    #Please select an operation: # end of multi- line string. also using string interpolation
    return menu



##### Read

products = []

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            #print(row["name"], row["price"])
            products.append(dict(row))

    return products

    #TODO: open the file and populate the products list with product dictionaries



#####  Write

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")

    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for p in products:
            writer.writerow(p)



    #TODO: open the file and write a list of dictionaries. each dict should represent a product.


def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)


###############################################################################

def get_product_id(product): return int(product["id"])

def auto_incremented_id():
    product_ids = map(get_product_id, products)
    return max(product_ids) + 1

headers = ["id", "name", "aisle", "department", "price"] # for "Further Exploration" use: ["product_id", "product_name", "aisle_id", "aisle_name", "department_id", "department_name", "price"]
user_input_headers = [header for header in headers if header != "id"] # don't prompt the user for the product_id



#List functions


def list_products():
    print("---------------------")
    print("LISTING PRODUCTS HERE")
    print("---------------------")
    for product in products:
        print(" + Product #" + str(product["id"]) + ": " + product["name"])

def show_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id]

    if product:
        print("READING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)

def create_product():
    print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
    product = {"id": auto_incremented_id() }
    for header in user_input_headers:
        product[header] = input("The '{0}' is: ".format(header))
    products.append(product)
    print("CREATING PRODUCT HERE", product)
    write_products_to_file(products=products)

def update_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("OK. PLEASE PROVIDE THE PRODUCT'S INFORMATION...")
        for header in user_input_headers:
            product[header] = input("Change '{0}' from '{1}' to: ".format(header, product[header]))
        print("UPDATING PRODUCT HERE", product)
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)
    write_products_to_file(products=products)


def destroy_product():
    product_id = input("OK. WHAT IS THE PRODUCT'S ID? ")
    product = [p for p in products if p["id"] == product_id][0]
    if product:
        print("DESTROYING PRODUCT HERE", product)
        del products[products.index(product)]
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER", product_id)
    write_products_to_file(products=products)

def enlarg(my_number):
    return my_number*100











def run():
    # First, read products from file...
    products = read_products_from_file()
    input_username = input("Please input username: ")

    # Then, prompt the user to select an operation...
    print(menu(username= input_username , products_count= len(products))) #TODO instead of printing, capture user input


    crud_operation = input("Please select an operation: ")

    if crud_operation.title() == "List":
        list_products()
    elif crud_operation.title() == "Show":
        show_product()
    elif crud_operation.title() == "Create":
        create_product()
    elif crud_operation.title() == "Update":
        update_product()
    elif crud_operation.title() == "Destroy":
        destroy_product()
    else:
        print("OOPS SORRY. PLEASE TRY AGAIN.")


# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
