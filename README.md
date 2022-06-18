# simple_connect_azure_sql

# Learning Links
[Create an app that connects to Azure SQL](https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql) <br>
[Create a Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli) <br>
[Connect Django to Azure SQL](https://docs.microsoft.com/en-us/samples/azure-samples/azure-sql-db-django/azure-sql-db-django/) <br>
[Example code from Microsoft with SQL and REST API](https://github.com/Azure-Samples/azure-sql-db-django/tree/main/customerapi) <br>
[Generating models.py for existing databases](https://docs.djangoproject.com/en/4.0/howto/legacy-databases/)

# Command to fix pyodbc install problems on MacOS Monterey
<br> NOTE : Check path for unixodbc by running `ls /opt/homebrew/Cellar/unixodbc/` <br>
CPPFLAGS='-I/opt/homebrew/Cellar/unixodbc/2.3.11/include' LDFLAGS='-L/opt/homebrew/Cellar/unixodbc/2.3.11/lib' pip install pyodbc
## Links to help
[Microsoft Intsructions](https://docs.microsoft.com/en-us/azure/azure-sql/database/connect-query-python?view=azuresql)
[Stackexchange](https://stackoverflow.com/questions/71138425/installing-pyodbc-fails-on-osx-12-2-monterey#new-answer)

# packages to be installed in venv
- pyodbc
- azure-identity
- azure-keyvault-secrets