from typing import (
    TYPE_CHECKING,
    NamedTuple,
    Tuple,
)

from wasm.typing import (
    Expression,
)

from .indices import (
    TypeIdx,
)
from .val_type import (
    ValType,
)

if TYPE_CHECKING:
    from wasm.instructions import (  # noqa: F401
        Instruction,
    )


class FunctionType(NamedTuple):
    """
    https://webassembly.github.io/spec/core/bikeshed/index.html#function-types%E2%91%A0
    """
    params: Tuple[ValType, ...]
    results: Tuple[ValType, ...]


class Function(NamedTuple):
    """
    https://webassembly.github.io/spec/core/bikeshed/index.html#functions%E2%91%A0
    """
    type: TypeIdx
    locals: Tuple[ValType, ...]
    body: Expression
