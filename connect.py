import pyodbc


def connect_to_db():

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=CSE1405377\SQL;'
                          'Database=AuditTool;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    return cursor

