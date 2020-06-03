from google.api_core import client_info as client_info
from google.cloud import client as google_client, environment_vars as environment_vars
from google.cloud.datastore_v1.gapic import datastore_client as datastore_client
from google.cloud.datastore_v1.proto import datastore_pb2_grpc as datastore_pb2_grpc
from typing import Any, Optional

DATASTORE_API_HOST: Any

class Client(google_client.ClientWithProject):
    SCOPE: Any = ...
    namespace: Any = ...
    host: Any = ...
    client_info: Any = ...
    secure: Any = ...
    stub: Any = ...
    def __init__(
        self,
        project: Optional[Any] = ...,
        namespace: Optional[Any] = ...,
        credentials: Optional[Any] = ...,
    ) -> None: ...
    def context(
        self,
        namespace: Any = ...,
        cache_policy: Optional[Any] = ...,
        global_cache: Optional[Any] = ...,
        global_cache_policy: Optional[Any] = ...,
        global_cache_timeout_policy: Optional[Any] = ...,
        legacy_data: bool = ...,
    ) -> None: ...
