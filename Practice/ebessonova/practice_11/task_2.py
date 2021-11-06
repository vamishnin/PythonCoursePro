# -*- coding: utf-8 -*-

from task_1 import SQLiteWrapper
import sqlite3
import os


def configure_db(connection_db):
    cur = connection_db.cursor()
    cur.execute('CREATE TABLE CUSTOMER'
                '    (ID                INT   PRIMARY KEY  NOT NULL,'
                '     CUSTOMER_NAME     TEXT               NOT NULL,'
                '     PRODUCT           CHAR(50),'
                '     PRODUCT_AMOUNT    INT);')
    cur.execute('CREATE TABLE PRODUCT'
                '    (ID               INT   PRIMARY KEY  NOT NULL,'
                '     PRODUCT_NAME     TEXT               NOT NULL,'
                '     COMPANY_NAME     TEXT               NOT NULL,'
                '     PRICE            REAL);')
    cur.execute('CREATE TABLE COMPANY'
                '    (ID               INT   PRIMARY KEY  NOT NULL,'
                '     COMPANY_NAME     TEXT               NOT NULL);')


db_name = 'new_retail.db'
db_exists = os.path.exists(db_name)
conn = sqlite3.connect(db_name)
obj = SQLiteWrapper(conn)

if not db_exists:
    configure_db(conn)
    obj.execute("INSERT INTO COMPANY (ID, COMPANY_NAME)"
                "VALUES (1, 'Lenta')")
    obj.execute("INSERT INTO COMPANY (ID, COMPANY_NAME)"
                "VALUES (2, 'Magnit')")
    obj.execute("INSERT INTO COMPANY (ID, COMPANY_NAME)"
                "VALUES (3, 'Spar')")

    obj.execute("INSERT INTO PRODUCT (ID, PRODUCT_NAME, COMPANY_NAME, PRICE)"
                "VALUES (1, 'Apple', 'Lenta', 15.00)")
    obj.execute("INSERT INTO PRODUCT (ID, PRODUCT_NAME, COMPANY_NAME, PRICE)"
                "VALUES (2, 'Orange', 'Lenta', 2.00)")
    obj.execute("INSERT INTO PRODUCT (ID, PRODUCT_NAME, COMPANY_NAME, PRICE)"
                "VALUES (3, 'Juice', 'Magnit', 10.00)")
    obj.execute("INSERT INTO PRODUCT (ID, PRODUCT_NAME, COMPANY_NAME, PRICE)"
                "VALUES (4, 'Tomat', 'Spar', 5.00)")
    obj.execute("INSERT INTO PRODUCT (ID, PRODUCT_NAME, COMPANY_NAME, PRICE)"
                "VALUES (5, 'Cucumber', 'Spar', 2.00)")
    obj.execute("INSERT INTO PRODUCT (ID, PRODUCT_NAME, COMPANY_NAME, PRICE)"
                "VALUES (6, 'Onion', 'Spar', 3.00)")

    obj.execute("INSERT INTO CUSTOMER (ID, CUSTOMER_NAME, PRODUCT, PRODUCT_AMOUNT)"
                "VALUES (1, 'Mark Ivanov', 'Apple', 6)")
    obj.execute("INSERT INTO CUSTOMER (ID, CUSTOMER_NAME, PRODUCT, PRODUCT_AMOUNT)"
                "VALUES (2, 'Vladimir Markov', 'Orange', 5)")
    obj.execute("INSERT INTO CUSTOMER (ID, CUSTOMER_NAME, PRODUCT, PRODUCT_AMOUNT)"
                "VALUES (3, 'Ivan Vladimirov', 'Tomat', 10)")
    obj.execute("INSERT INTO CUSTOMER (ID, CUSTOMER_NAME, PRODUCT, PRODUCT_AMOUNT)"
                "VALUES (4, 'Petr Sidorov', 'Cucumber', 15)")
    obj.execute("INSERT INTO CUSTOMER (ID, CUSTOMER_NAME, PRODUCT, PRODUCT_AMOUNT)"
                "VALUES (5, 'Vasiliy Petrov', 'Apple', 23)")

# 1 подвопрос
# производители у которых более 2 товаров по цене 10 долларов и ниже
obj.select('SELECT  company_name FROM PRODUCT WHERE price <= 10 '
           'GROUP BY company_name HAVING COUNT(company_name) > 2')

# 2 подвопрос
# покупатели, которые делали заказы, сгруппированные их по компаниям производителей чьи товары покупались
obj.select('SELECT customer_name, company_name '
           'FROM CUSTOMER JOIN PRODUCT ON CUSTOMER.product = PRODUCT.PRODUCT_NAME '
           'ORDER BY PRODUCT.company_name')

# 3 подвопрос
# самые популярные товары у каждого производителя, и сколько таких товаров было куплено
obj.select('SELECT product, company_name, MAX(sum_prod) AS amount FROM '
           '(SELECT product, company_name, SUM(product_amount) as sum_prod '
           'FROM CUSTOMER JOIN PRODUCT on CUSTOMER.product = PRODUCT.product_name GROUP BY product, company_name)'
           'GROUP BY company_name')

# 4 подвопрос
# производители товаров, которые продавались, с указанием их выручек по каждому виду товара
obj.select('SELECT company_name, product, SUM(product_amount * price) as earning '
           'FROM CUSTOMER JOIN PRODUCT on CUSTOMER.product = PRODUCT.product_name GROUP BY product, company_name')

# товары, которые не продавались
obj.select('SELECT product_name, company_name from PRODUCT '
           'LEFT JOIN CUSTOMER ON PRODUCT.product_name = CUSTOMER.product '
           'WHERE CUSTOMER.product is NULL')



