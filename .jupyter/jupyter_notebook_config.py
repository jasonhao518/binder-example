from s3contents import S3ContentsManager

# Tell Jupyter to use S3ContentsManager
c.ServerApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = "zE2qJ1VCy6QnDHRG"
c.S3ContentsManager.secret_access_key = "XlEV2kRRs2Kel0JAPUZbSb01FCEVWt42"
c.S3ContentsManager.endpoint_url = "http://data-minio.data.svc.cluster.local:9000"
c.S3ContentsManager.bucket = "notebook"
c.S3ContentsManager.prefix = "notebooks/test"
