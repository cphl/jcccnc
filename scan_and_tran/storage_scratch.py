from google.cloud import storage

# Will need auth. try https://pypi.org/project/google-auth/ as oauth2client is deprecated

# Create bucket for temporary usage in GCS
storage_client = storage.Client()

bucket_name = "test_transient_bucket"

bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")



# Delete the bucket
# bucket.delete(force=True)

# Upload a local file to GCS

# TODO: upload a file from Google drive directly to Cloud Storage
# The source drive is shared with me so hopefully I can use this method of mounting the drive:
# https://colab.research.google.com/notebooks/io.ipynb#scrollTo=c2W5A2px3doP


# Delete a file from cloud storage

