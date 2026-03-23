from google.cloud import storage  # need `pip install --upgrade google-cloud-storage`

# Need to set up credentials: https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#how-to
# Run this: `gcloud auth application-default login` (which in turn needs gcloud: https://docs.cloud.google.com/sdk/docs/install-sdk#latest-version)
# And you'll be authenticated in a browser pop-up, with Google cloud auth, and then you can do the rest.

# Will need auth. try https://pypi.org/project/google-auth/ as oauth2client is deprecated

def create_bucket(bucket_name):
	"""Needs the above auth steps."""
	storage_client = storage.Client()
	bucket = storage_client.create_bucket(bucket_name)
	print(f"Bucket {bucket.name} created.")

	return bucket

# Upload from a TSV of the URL of the Drive files
# https://docs.cloud.google.com/storage-transfer/docs/create-url-list
# The list needs to be stored at a public URL or in a bucket, let's put it there first for simplicity

# Not working yet!
# From gcs but using the publicly accessible https instead of gcs address...
# Instructions are to make a transfer job using the REST API but
# this runs periodically and we only need to run this once
# at the beginning of one Drive folder being processed.
# Oh well, try to make it simpler later.
# We want to do
# POST https://storagetransfer.googleapis.com/v1/transferJobs
# {
#   "projectId": "project-9301190b-e716-4e6e-a10",
#   "transferSpec": {
#     "httpDataSource": {
#       "listUrl": "https://storage.googleapis.com/test_transient_bucket/urllist/sample_urllist.tsv"
#     },
#     "gcsDataSink": {
#       "bucketName": "test_transient_bucket"
#     }
#   },
#   "status": "ENABLED"
# }

# TODO: delete contents of bucket or make force actually work


def delete_bucket(bucket_name):
	"""Bucket needs to be empty."""
	storage_client = storage.Client()
	bucket = storage_client.get_bucket(bucket_name)
	bucket.delete(force=True)  # interesting... this doesn't work
	print(f"Bucket {bucket.name} deleted")

# Upload a local file to GCS
# via colab
# https://colab.research.google.com/notebooks/io.ipynb#scrollTo=c2W5A2px3doP

# Delete a file from cloud storage


# Do all the things
bucket_name = "test_transient_bucket"
# bucket = create_bucket(bucket_name)  # See it at https://console.cloud.google.com/storage/browser?project=project-9301190b-e716-4e6e-a10&prefix=&forceOnBucketsSortingFiltering=true&bucketType=live
# delete_bucket
