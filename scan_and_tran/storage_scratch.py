from google.cloud import storage  # need `pip install --upgrade google-cloud-storage`

# Need to set up credentials: https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#how-to
# Run this: `gcloud auth application-default login`
# And you'll be authenticated in a browser pop-up, with Google cloud auth, and then you can do the rest.

# Will need auth. try https://pypi.org/project/google-auth/ as oauth2client is deprecated



# WORKS (with the above auth steps) Create bucket for temporary usage in GCS
# storage_client = storage.Client()
# bucket_name = "test_transient_bucket"
# bucket = storage_client.create_bucket(bucket_name)

# print(f"Bucket {bucket.name} created.")

## Confirmed that the bucket was created: https://console.cloud.google.com/storage/browser?project=project-9301190b-e716-4e6e-a10&prefix=&forceOnBucketsSortingFiltering=true&bucketType=live


# WORKS! Delete the bucket
storage_client = storage.Client()
bucket_name = "test_transient_bucket"
bucket = storage_client.get_bucket(bucket_name)
bucket.delete(force=True)
print(f"Bucket {bucket.name} deleted")

# Upload a local file to GCS

# TODO: upload a file from Google drive directly to Cloud Storage
# The source drive is shared with me so hopefully I can use this method of mounting the drive:
# https://colab.research.google.com/notebooks/io.ipynb#scrollTo=c2W5A2px3doP


# Delete a file from cloud storage

