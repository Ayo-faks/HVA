# from azure.storage.blob import BlockBlobService, ContentSettings

# # Set your Azure Storage account name and account key
# account_name = 'csb100320026accc72e'
# account_key = 'IecPJxp2rOaN7MhKAjqShLXi5AjSXOJJmxiViYX9+lUBhNRgebo/mlVdZfYxfsQ+7SMJauAs222C+AStoez3qQ=='

# # Create a BlockBlobService object
# blob_service = BlockBlobService(account_name=account_name, account_key=account_key)

# # Set the container name and model path
# container_name = 'pocva'
# model_path = '/workspace/HVA/assistant/models/20230306-162155-numerous-expenditure.tar.gz'

# # Upload the Rasa trained model to Azure Blob Storage
# with open(model_path, 'rb') as data:
#     blob_service.create_blob_from_stream(container_name, 'model.tar.gz', data, content_settings=ContentSettings(content_type='application/gzip'))

from azure.storage.blob import BlobServiceClient, BlobClient, BlobSasPermissions, generate_blob_sas, ContainerSasPermissions, generate_container_sas, ContentSettings

# Set your Azure Storage account name and account key
account_name = 'hvassistant'
account_key = 'cIeYqbkzV23sh2H3MrDuvk2jIasOhHGPczCVLIgzIWwDs8s3C6n2lb/o9nObGUX+AzzHWYg135qz+AStPxVxxw=='

# Create a BlobServiceClient object
connection_string = f"DefaultEndpointsProtocol=https;AccountName={account_name};AccountKey={account_key};EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Set the container name and model path
container_name = 'conva'
model_path = '/workspace/HVA/assistant/models/20230306-162155-numerous-expenditure.tar.gz'

# Get a BlobClient object for the new blob blob
blob_client = blob_service_client.get_blob_client(container_name, 'model.tar.gz')

# Upload the Rasa trained model to Azure Blob Storage
with open(model_path, 'rb') as data:
    blob_client.upload_blob(data, blob_type="BlockBlob", content_settings=ContentSettings(content_type='application/gzip'))
