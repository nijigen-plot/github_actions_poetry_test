import base64
import os

from google.cloud import bigquery
from google.oauth2 import service_account

cred = eval(base64.b64decode(os.environ.get('gcp_service_key')))

credentials = service_account.Credentials.from_service_account_info(
    cred,
    scopes = ['https://www.googleapis.com/auth/bigquery']
)

client = bigquery.Client(
    project='voltaic-country-281210',
    credentials=credentials
)

query = """
SELECT current_datetime
"""

print(client.query(query).to_dataframe())
