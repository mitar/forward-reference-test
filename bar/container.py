import typing

from . import something

T = typing.TypeVar('T', covariant=True)

class List(typing.List[T]):
    pass
