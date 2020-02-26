# endpoint-api-client

All commands have to be run in project root directory:

cd banks_storage/

## Installation

pip install endpoint-api-client


## Usage
from client import StorageAPI

your_api_url_endpoint = 'http://something.com/collection/'

headers = {\*\*StorageAPI.DEFAULT_HEADERS, 'foo': 'bar',}  \# optional

storage_client = StorageAPI(your_api_url_endpoint, headers)

#### GET
\# Methods returns "requests.Response" instances

get_response = storage_client.get_documents()


#### POST
your_document = {'field': 1, 'another_field': \['baz', 'bar',\]}

post_response = storage_client.post_document(some_doc)

