import http.client
from Modules.connect import connect_to_db


def get_data(connection):
    result = connection.execute("select AuditTool.dbo.Test.result,AuditTool.dbo.Test.Coreappid,AuditTool.dbo.Test.Alias,AuditTool.dbo.Test.installScenario,AuditTool.dbo.Test.AppName,AuditTool.dbo.Test.Appversion from AuditTool.dbo.Test inner join AuditTool.dbo.Main on Test.Coreappid=Main.Coreappid where AuditTool.dbo.Test.result='NotRun' and AuditTool.dbo.Main.result!='Not Run'")

    X = result.fetchall()

    for x in X:
        print(x)

    email_ids = list(connection.execute("select distinct Alias from AuditTool.dbo.Test"))

    email_ids = [''.join(x) + '@microsoft.com' if x[0] is not None else "" for x in email_ids]

    email_ids = list(filter(lambda x: len(x) > 0, email_ids))

    print(email_ids)


    email_ids = ['arnabkhan1995@gmail.com']
    conn = http.client.HTTPSConnection("control.msg91.com")

    payload = ""

    for email in email_ids:

        conn.request("POST",
                    "https://control.msg91.com/api/sendmailotp.php?otp=456789&authkey=120784AMGtwZHOGVI5ab0170a&email="+email,payload)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))


if __name__ == '__main__':
    get_data(connect_to_db())
