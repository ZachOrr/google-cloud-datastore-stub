from google.cloud.ndb import exceptions as exceptions
from typing import Any

class RemoteCall:
    future: Any = ...
    info: Any = ...
    def __init__(self, future: Any, info: Any) -> None: ...
    def exception(self): ...
    def result(self): ...
    def add_done_callback(self, callback: Any): ...
    def cancel(self): ...
