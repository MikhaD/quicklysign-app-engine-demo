from google.cloud import datastore
import os

os.environ.setdefault("GCLOUD_PROJECT", "data-fabric-413816")
datastore_client = datastore.Client()