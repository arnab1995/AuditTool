import pyodbc

if __name__ == '__main__':

    def test_connection():
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=CSE1405377\SQL;'
                              'Database=AuditTool;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()

        rows = cursor.execute('SELECT * FROM AuditTool.dbo.main')

        for row in rows:
            print(row)

    test_connection()
