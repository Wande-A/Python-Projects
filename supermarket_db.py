import sqlite3
import time
import datetime

db_conn = None


def create_or_connect_to_db():
    """will create a data base if it doesnt exist or open one if it exists"""
    global db_conn
    my_db_pathname = "db_supermarket"
    db_conn = sqlite3.connect(my_db_pathname)


def create_table():
    """this will create the table and the columns in it. the different case (capital and lower letter) is
    just a formality so the code can look neat."""
    global db_conn
    query = """
            CREATE TABLE IF NOT EXISTS tbl_products
            (
                prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
                prod_name VARCHAR(50) NOT NULL,
                prod_qty INT NOT NULL,
                prod_price FLOAT(14,2) NOT NULL,
                prod_date VARCHAR NOT NULL,
                exp_date VARCHAR NOT NULL
            )
            """
    print("Preparing Products table...\t\t", end="")
    db_conn.execute(query)
    time.sleep(0.5)
    print("Table Created!")


def create_init_rec():
    """This enters the existing products at the time the product database was created"""
    global db_conn
    prodct_name = input("What's the name of the product?")
    try:
        prodct_qty = int(input("How many of it is in stock?"))
    except ValueError:
        print("Enter a number please")
    prodct_price = float(input("How much is it?"))
    prodctn_date = ""
    expiry_date = ""
    expiry_d8 = input("Enter the date the item will expire: Format: yyyy-mm-dd")
    date_valid1 = expiry_d8.split('-')
    if len(date_valid1) == 3 and len(date_valid1[0]) == 4:
        if int(date_valid1[1]) <= 12 and int(date_valid1[2]) <= 31:
            expiry_date = expiry_d8
        else:
            print("Invalid format")
    else:
        print("invalid format")
    productn_date = input("Enter the date the item was produced: Format: yyyy-mm-dd")
    date_valid = productn_date.split('-')
    if len(date_valid) == 3 and len(date_valid[0]) == 4:
        if int(date_valid[1]) <= 12 and int(date_valid[2]) <= 31:
            prodctn_date = productn_date
        else:
            print("Invalid format")
    else:
        print("invalid format")
    prod_deets = ["INSERT INTO tbl_products(prod_name, prod_qty, prod_price, prod_date, exp_date) VALUES('{}', {}, {}, '{}', '{}')".format(prodct_name, prodct_qty, prodct_price, prodctn_date, expiry_date)
                ]
    print("Entering available products...\t\t", end="")
    for a_prod in prod_deets:
        db_conn.execute(a_prod)
    db_conn.commit()
    time.sleep(0.5)
    print("Products details Entered!")


def read_prod_tbl():
    """pull up product details for viewing"""
    global db_conn
    query = "SELECT * FROM tbl_products"
    prod_lst = db_conn.execute(query)
    for a_prod in prod_lst:
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(a_prod[0], a_prod[1], a_prod[2], a_prod[3], a_prod[4], a_prod[5]))


def read_deet_frm_prod_tbl():
    """pull up a particular product's details for viewing"""
    global db_conn
    search_keyword = int(input("""
                                Would you like to search with name or id?
                                1. Name
                                2. ID
                                Enter a number: 
                            """))
    if search_keyword == 1:
        search_name = input("Enter name of product: ").lower()
        query1 = "SELECT * FROM tbl_products"
        prod_lst1 = db_conn.execute(query1)
        count = 0
        for a_prod1 in prod_lst1:
            if a_prod1[1] == search_name:
                count = count + 1
        if count <= 0:
            print("{} does not exist in database!!!".format(search_name))
        elif count > 0:
            query = "SELECT * FROM tbl_products WHERE prod_name= '{}'".format(search_name)
            prod_lst = db_conn.execute(query)
            for a_prod in prod_lst:
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(a_prod[0], a_prod[1], a_prod[2], a_prod[3], a_prod[4], a_prod[5]))
    elif search_keyword == 2:
        search_id = int(input("Enter id of product: "))
        query2 = "SELECT * FROM tbl_products"
        prod_lst2 = db_conn.execute(query2)
        count2 = 0
        for a_prod2 in prod_lst2:
            if a_prod2[0] == search_id:
                count2 = count2 + 1
        if count2 <= 0:
            print("No Product exist with ID {}".format(search_id))
        elif count2 > 0:
            query = "SELECT * FROM tbl_products WHERE prod_id= '{}'".format(search_id)
            prod_lst = db_conn.execute(query)
            for a_prod in prod_lst:
                print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(a_prod[0], a_prod[1], a_prod[2], a_prod[3], a_prod[4], a_prod[5]))
    else:
        print("Invalid Entry!!!")


def change_prod_deets():
    """change or update product details"""
    global db_conn
    prodct_id = int(input("Enter the id of product you want to update: "))
    query2 = "SELECT * FROM tbl_products"
    prod_lst2 = db_conn.execute(query2)
    count2 = 0
    for a_prod2 in prod_lst2:
        if a_prod2[0] == prodct_id:
            count2 = count2 + 1
    if count2 <= 0:
        print("No Product exist with ID {}".format(prodct_id))
    elif count2 > 0:
        detail_2_b_changd = int(input("""
                                    What do you want to change?
                                    Enter a number:
                                    1. product name
                                    2. Product quantity
                                    3. Product price
                                    4. Expiry date
                                    5. Manufacture date
                            """))
        if detail_2_b_changd == 1:
            new_name = input("Enter the new name of the product: ")
            query = "UPDATE tbl_products SET prod_name='{}' WHERE prod_id={}".format(new_name, prodct_id)
            db_conn.execute(query)
            db_conn.commit()
        elif detail_2_b_changd == 2:
            new_qty = input("How many is left now?")
            query = "UPDATE tbl_products SET prod_qty={} WHERE prod_id={}".format(new_qty, prodct_id)
            db_conn.execute(query)
            db_conn.commit()
        elif detail_2_b_changd == 3:
            new_price = input("How much is it now?")
            query = "UPDATE tbl_products SET prod_price={} WHERE prod_id={}".format(new_price, prodct_id)
            db_conn.execute(query)
            db_conn.commit()
        elif detail_2_b_changd == 4:
            expiry_d8 = input("Enter the date the item will expire: Format: yyyy-mm-dd")
            date_valid1 = expiry_d8.split('-')
            if len(date_valid1) == 3 and len(date_valid1[0]) == 4:
                if int(date_valid1[1]) <= 12 and int(date_valid1[2]) <= 31:
                    query = "UPDATE tbl_products SET exp_date='{}' WHERE prod_id={}".format(expiry_d8, prodct_id)
                    db_conn.execute(query)
                    db_conn.commit()
                else:
                    print("Invalid format")
            else:
                print("invalid format")
        elif detail_2_b_changd == 5:
            productn_date = input("Enter the date the item was produced: Format: yyyy-mm-dd")
            date_valid = productn_date.split('-')
            if len(date_valid) == 3 and len(date_valid[0]) == 4:
                if int(date_valid[1]) <= 12 and int(date_valid[2]) <= 31:
                    query = "UPDATE tbl_products SET prod_date='{}' WHERE prod_id={}".format(productn_date, prodct_id)
                    db_conn.execute(query)
                    db_conn.commit()
                else:
                    print("Invalid format")
            else:
                print("invalid format")
        else:
            print("Invalid Entry!!!")


def has_prod_expired():
    """check if the product has expired"""
    now = datetime.date.today()
    global db_conn
    query = "SELECT * FROM tbl_products"
    prod_lst = db_conn.execute(query)
    for a_prod in prod_lst:
        if a_prod[5] == str(now):
            print("""{} is expiring today {}!!!""".format(a_prod[1], a_prod[5]))


def has_prod_finished():
    """check if the product has finished"""
    global db_conn
    query = "SELECT * FROM tbl_products"
    prod_lst = db_conn.execute(query)
    for a_prod in prod_lst:
        if a_prod[2] <= 2:
            print("""{} is remaining {}!!!""".format(a_prod[1], a_prod[2]))



def sell_a_prodct():
    """search for a product, confirm how many the customer wants and deduct from the existing quantity"""
    global db_conn
    sold_prdct_lst = []
    while True:
        prodct_name = input("Enter the name of product you want to sell: ")
        query1 = "SELECT * FROM tbl_products"
        prod_lst1 = db_conn.execute(query1)
        count = 0
        for a_prod1 in prod_lst1:
            if a_prod1[1] == prodct_name:
                count = count + 1
        if count <= 0:
            print("{} does not exist in database!!!".format(prodct_name))
        elif count > 0:
            now = datetime.date.today()
            query = "SELECT * FROM tbl_products WHERE prod_name= '{}'".format(prodct_name)
            prod_lst = db_conn.execute(query)
            # current_qtce = None
            for a_prod in prod_lst:
                current_qty = a_prod[2]
                prodct_price = a_prod[3]
                if a_prod[5] == str(now):
                    print("{}\t\t{}\t\t{}\t\t{}".format(a_prod[0], a_prod[1], a_prod[2], a_prod[3]))
                qty_2b_sold = int(input("How many do you want to sell?: "))
                if qty_2b_sold > current_qty:
                    print("Not enough stock!!! There's only {} in stock".format(current_qty))
                else:
                    new_qty = current_qty - qty_2b_sold
                    query1 = "UPDATE tbl_products SET prod_qty={} WHERE prod_name='{}'".format(new_qty, prodct_name)
                    db_conn.execute(query1)
                    db_conn.commit()
                    time.sleep(0.5)
                    print("Sales price is {}".format(qty_2b_sold * prodct_price))
                    time.sleep(2)
        sales_lst = []
        sales_lst.append(prodct_name)
        sales_lst.append(qty_2b_sold)
        sales_lst.append(prodct_price)
        sold_prdct_lst.append(sales_lst)
        total = 0
        for item1 in sold_prdct_lst:
            total = total + item1[2]
        print(sold_prdct_lst)
        more_sales = input("Do you want to sell more items? Enter Y/N").lower()
        if more_sales == "y":
            continue
        elif more_sales == "n":
            print("""
                        <<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><>
                        **                                              **
                        **         DANGOTE SUPERMARKET & STORES         ** 
                        **          ADDRESS: IBEJU LEKKI                **  
                        **          TEL: 0908809                        **
                        **                                              **
                        **   INVOICE:                                   **""")
            for item in sold_prdct_lst:
                print("""
                        **   {} \t{} x {}\t   {}               **""".format(item[0], item[1], item[2], item[1] * item[2]))
            print(""" 
                        **                                              **
                        **    Total: #{}                             **
                        **                                              **
                        **       THANK YOU FOR SHOPPING WITH US         **
                        **                                              **
                        <<>><<>><<>><<>><<>>><<>><<>><<>><<>><<>><<>><<>><""".format(total))

            break
        else:
            print("Invalid Entry!")
            break


def del_prod_deets():
    """delete product details out of the database of products"""
    global db_conn
    del_prod_id = input("Enter the id of the product you want deleted: ")
    query = "DELETE FROM tbl_products WHERE prod_id={}".format(del_prod_id)
    db_conn.execute(query)
    db_conn.commit()


def exit_db():
    """Exit the database after usage"""
    global db_conn
    db_conn.close()


while True:
    create_or_connect_to_db()
    has_prod_expired()
    has_prod_finished()
    try:
        user = int(input("""
                                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                <>           PICK A NUMBER:              <>
                                <>***************************************<>
                                <>                                       <>
                                <>     1: MANAGER                        <>
                                <>     2. TELLER                         <>
                                <>                                       <>
                                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                Enter a number:
                                """))

        if user == 1:
            password = 12345
            p_word = int(input("Enter the password: "))
            if password == p_word:
                print("Password Accepted!!!")
                time.sleep(1)
                manager_act = int(input("""
                                            :::::::::::::::::::::::::::::::::::::::::::
                                            ::                MENU                   ::
                                            ::    1: Add new product                 ::
                                            ::    2: Update Existing product         ::
                                            ::    3: Delete a product                ::
                                            ::    4: Check a Product Detail          ::
                                            ::    5: Close the Database              ::
                                            ::                                       ::
                                            :::::::::::::::::::::::::::::::::::::::::::
                                            Enter a number: 
                                    """))
                if manager_act == 1:
                    create_or_connect_to_db()
                    create_table()
                    create_init_rec()
                elif manager_act == 2:
                    create_or_connect_to_db()
                    read_prod_tbl()
                    change_prod_deets()
                    read_prod_tbl()
                elif manager_act == 3:
                    create_or_connect_to_db()
                    del_prod_deets()
                    read_prod_tbl()
                elif manager_act == 4:
                    create_or_connect_to_db()
                    read_deet_frm_prod_tbl()
                elif manager_act == 5:
                    create_or_connect_to_db()
                    exit_db()
                    print("DATABASE CLOSED!!!")
                else:
                    print("Invalid Entry!!! Enter between numbers 1 and 5")
            elif password != p_word:
                print("Incorrect Password!!! Please enter password again")

        elif user == 2:
            teller_act = int(input("""
                          :::::::::::::::::::::::::::::::::::::::::::
                          ::                MENU                   ::
                          ::    1: Check a Product Detail          ::
                          ::    2: Sell a Product                  ::
                          ::    3: Close the Database              ::
                          :::::::::::::::::::::::::::::::::::::::::::
                          ENTER A NUMBER:
                        """))

            if teller_act == 1:
                create_or_connect_to_db()
                read_deet_frm_prod_tbl()
            elif teller_act == 2:
                create_or_connect_to_db()
                sell_a_prodct()
            elif teller_act == 3:
                create_or_connect_to_db()
                exit_db()
                print("DATABASE CLOSED!!!")
            else:
                print("Invalid Entry!!! Enter between numbers 1 and 3")
        else:
            print("Invalid Entry!!!")
    except ValueError:
        print("Please enter a number!!!")
    # except UnboundLocalError:
    #     print("Try Again!")
    except KeyboardInterrupt:
        exit_db()


