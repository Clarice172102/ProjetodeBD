import pandas as pd

pd.DataFrame({
    'Atribute': ['client_id', 'client_name', 'client_email', 'client_tephone'],
    'Type': ['int', 'char', 'varchar','char'],
    'Key': ['Pk', '-', '-', '-'],
    'Nullable': ['no', 'no', 'no', 'no'],
    'Len': [10, 20, 50, 11],
    'Description': ['And the primary key that identifies the customer', 'The customer is name, without special characters', 'The customer is email, to get in touch, just one.', 'The customer is phone number without special characters and with the state area code. Just to put a phone number.']
})

pd.DataFrame({
    'Atribute': ['book_id',  'book_name', 'book_author', 'book_volume'],
    'Type': ['int', 'char', 'char', 'int'],
    'Key': ['Pk', '-', '-', '-'],
    'Nullable': ['no', 'no', 'no', 'no'],
    'Len': [10, 50, 50, 10],
    'Description': ['is the primary key that identifies the book', ' the book name', 'the name of the author of the book', 'the volume of the book']
})

pd.DataFrame({
    'Atribute': ['id_loan', 'return_loan', 'date_loan', 'id_book', 'id_client'],
    'Type': ['int', 'date', 'date', 'int','int'],
    'Key': ['Pk', '-', '-', 'FK', 'FK'],
    'Nullable': ['no', 'no', '-', 'no', 'no'],
    'Len': [10, 8, 8, 10, 10],
    'Description': ['It is the primary key that identifies the loan', 'It is the date the book was returned without special characters YYYY-MM-D0', 'It is the date on which the book was borrowed without special characters', 'It is the foreign key that identifies the book', 'It is the foreign key that identifies the customer']
})