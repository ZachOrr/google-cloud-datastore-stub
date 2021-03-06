from google.cloud.datastore.batch import Batch as Batch
from google.cloud.datastore_v1.types import TransactionOptions as TransactionOptions
from typing import Any

class Transaction(Batch):
    _status: Any = ...
    _id: Any = ...
    _options: Any = ...
    def __init__(self, client: Any, read_only: bool = ...) -> None: ...
    @property
    def id(self): ...
    def current(self): ...
    def begin(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def put(self, entity: Any) -> None: ...
