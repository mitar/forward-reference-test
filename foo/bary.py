import typing

from bar import types

Container = typing.TypeVar('Container', bound=types.Container)

class Bary(typing.Generic[Container]):
    def compute(self) -> Container:
        pass
