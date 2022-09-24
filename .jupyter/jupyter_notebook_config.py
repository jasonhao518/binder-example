from s3contents import S3ContentsManager

# Tell Jupyter to use S3ContentsManager
c.NotebookApp.contents_manager_class = S3ContentsManager
c.S3ContentsManager.access_key_id = "obEfZT1z6wV5W6vH"
c.S3ContentsManager.secret_access_key = "j20r5NujjTQz9iFl3XJMAgAphkco30ez"
c.S3ContentsManager.endpoint_url = "http://data-minio.data.svc.cluster.local:9000"
c.S3ContentsManager.bucket = "notebook"
