import os
from google.cloud import storage



# credentials_dict = {
#     'type': 'service_account',
#     'client_id': os.environ['BACKUP_CLIENT_ID'],
#     'client_email': os.environ['BACKUP_CLIENT_EMAIL'],
#     'private_key_id': os.environ['BACKUP_PRIVATE_KEY_ID'],
#     'private_key': os.environ['BACKUP_PRIVATE_KEY'],
# }
# credentials = ServiceAccountCredentials.from_json_keyfile_dict(
#     credentials_dict
# )
#
# client = storage.Client.from_service_account_json(credentials_dict)
#
# client = storage.Client(credentials=credentials, project='myproject')
# bucket = client.get_bucket('mybucket')
# blob = bucket.blob('myfile')