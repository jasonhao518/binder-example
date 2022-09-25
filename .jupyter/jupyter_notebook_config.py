from s3contents import S3ContentsManager
from hybridcontents import HybridContentsManager
from notebook.services.contents.largefilemanager import LargeFileManager

c.HybridContentsManager.manager_classes = {
    # Associate the root directory with an S3ContentsManager.
    # This manager will receive all requests that don"t fall under any of the
    # other managers.
    "": S3ContentsManager,
    # Associate /local_directory with a LargeFileManager.
    "local_directory": LargeFileManager,
}

c.HybridContentsManager.manager_kwargs = {
    # Args for root S3ContentsManager.
    "": {
        "access_key_id": "obEfZT1z6wV5W6vH",
        "secret_access_key": "j20r5NujjTQz9iFl3XJMAgAphkco30ez",
        "bucket": "notebook",
        "endpoint_url" = "http://data-minio.data.svc.cluster.local:9000"
    },
    # Args for the LargeFileManager mapped to /local_directory
    "local_directory": {
        "root_dir": "/home/jovyan/local",
    },
}

# Tell Jupyter to use S3ContentsManager
#c.ServerApp.contents_manager_class = HybridContentsManager
#c.ServerApp.root_dir=""
#c.S3ContentsManager.access_key_id = "obEfZT1z6wV5W6vH"
#c.S3ContentsManager.secret_access_key = "j20r5NujjTQz9iFl3XJMAgAphkco30ez"
#c.S3ContentsManager.endpoint_url = "http://data-minio.data.svc.cluster.local:9000"
#c.S3ContentsManager.bucket = "notebook"
