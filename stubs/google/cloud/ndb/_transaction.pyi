from google.cloud.ndb import exceptions as exceptions, tasklets as tasklets
from typing import Any, Optional

log: Any

def in_transaction(): ...
def transaction(
    callback: Any,
    retries: Any = ...,
    read_only: bool = ...,
    join: bool = ...,
    xg: bool = ...,
    propagation: Optional[Any] = ...,
): ...
def transaction_async(
    callback: Any,
    retries: Any = ...,
    read_only: bool = ...,
    join: bool = ...,
    xg: bool = ...,
    propagation: Optional[Any] = ...,
): ...
def transactional(
    retries: Any = ...,
    read_only: bool = ...,
    join: bool = ...,
    xg: bool = ...,
    propagation: Optional[Any] = ...,
): ...
def transactional_async(
    retries: Any = ...,
    read_only: bool = ...,
    join: bool = ...,
    xg: bool = ...,
    propagation: Optional[Any] = ...,
): ...
def transactional_tasklet(
    retries: Any = ...,
    read_only: bool = ...,
    join: bool = ...,
    xg: bool = ...,
    propagation: Optional[Any] = ...,
): ...
def non_transactional(allow_existing: bool = ...): ...
