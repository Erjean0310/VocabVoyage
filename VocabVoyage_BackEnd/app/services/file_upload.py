import oss2
import uuid
from pathlib import Path
from app.core.config import settings
from fastapi import File


def upload_file_to_oss(file: File):
    endpoint = settings.ENDPOINT
    access_key_id = settings.ACCESS_KEY_ID
    access_key_secret = settings.ACCESS_KEY_SECRET
    bucket_name = settings.BUCKET_NAME

    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    file_name = Path(file.filename)
    key = f"{uuid.uuid4().hex}.{file_name.suffix}"

    result = bucket.put_object(key, file.file)

    if result.status == 200:
        url = f"http://{bucket_name}.{endpoint}/{file_name}"
        return url
    return None
