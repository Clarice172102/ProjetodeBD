import sqlite3

def connect_db(db_library: str):
    """
    Connect to an existent data base.
    If ont exist, it will create one.

    args
        db_name (str): A datebase name. 
    
    """

    conn = sqlite3.connect(db_library)

    return conn

import sqlite3
import pandas as pd

# Criar conexão SQLite em memória
conn = sqlite3.connect("tads")

# Criando DataFrames
customers_df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ['Clarice', 'Rebeka', 'Stella', 'Alana'],
    "email": ['fregbbv@gmail.com', 
        'danvbabn@gmail.com', 
        'dksnvjnf@gmail.com', 
        'fnbs@gmail.com', 
    ],
    "telephone": ['81 986446679', '81 965636482', '81 964321564', '81 975432145']
})

book_df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ['Language in C', '1984', 'Hunder games', 'Little prince'],
    "author": ['Victorine V.', 'George O.', 'Suzanne C.', 'Antoine de S.'],
    "volume":[2, '-', '-', 1]
})

loan_df = pd.DataFrame({
    "id":[1, 2, 3, 4],
    "return_loan":['Available', 'Unavailable', 'Available', 'Unavailable'],
    "date": [12/1/2025, 24/4/2025, 1/5/2025, 9/6/2025],
    "customer_id": [1, 2, 3, 4,],
    "book_name": ['Language in C', '-', 'Hunder games', 'Little prince']
})

# Salvando os DataFrames no banco SQLite
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
book_df.to_sql("book", conn, index=False, if_exists="replace")
loan_df.to_sql("loan", conn, index=False, if_exists="replace")

# Executar INNER JOIN
query_inner = """
SELECT customers.id, customers.name, loan.book_name
FROM customers
INNER JOIN loan ON customers.id = loan.customer_id
WHERE loan.book_name != '-'
"""
inner_join_df = pd.read_sql(query_inner, conn)
print("INNER JOIN:")
print(inner_join_df)

# Executar LEFT JOIN
query_left = """
SELECT customers.id, customers.name, loan.book_name
FROM customers
LEFT JOIN loan ON customers.id = loan.customer_id
"""
left_join_df = pd.read_sql(query_left, conn)
print("\nLEFT JOIN:")
print(left_join_df)

# Fechar conexão
conn.close()