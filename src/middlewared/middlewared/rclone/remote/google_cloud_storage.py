import json

from middlewared.rclone.base import BaseRcloneRemote
from middlewared.schema import Str


class GoogleCloudStorageRcloneRemote(BaseRcloneRemote):
    name = "GOOGLE_CLOUD_STORAGE"
    title = "Google Cloud Storage"

    buckets = True

    rclone_type = "google cloud storage"

    credentials_schema = [
        Str("service_account_credentials", verbose="Service Account", required=True),
    ]

    def get_credentials_extra(self, credentials):
        return dict(
            service_account_credentials=(credentials["attributes"]["service_account_credentials"].
                                         replace("\r", "").
                                         replace("\n", "")),
            project_number=json.loads(credentials["attributes"]["service_account_credentials"])["project_id"],
        )
