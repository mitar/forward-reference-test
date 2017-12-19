import typing

from . import container

Container = typing.Union[
    container.List['Data'],
]

Data = typing.Union[
    Container,
    str, bytes, bool, float, int, dict,
]
