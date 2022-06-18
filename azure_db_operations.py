import pyodbc

from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

keyVaultName = "person-selector-kv"
KVUri = "https://person-selector-kv.vault.azure.net"
secretName = "person-selector-db-password"

credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

db_password = client.get_secret(secretName)

server = 'person-selector-db-server.database.windows.net'
database = 'person_selector_db'
username = 'personselectoradmin'
password = db_password.value   
driver= '{ODBC Driver 17 for SQL Server}'

conn_string = 'DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
print(conn_string)
with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM dbo.person_selector")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()