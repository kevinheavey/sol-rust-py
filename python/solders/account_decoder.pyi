class UiDataSliceConfig:
    def __init__(self, offset: int, length: int) -> None: ...
    @property
    def offset(self) -> int: ...
    @property
    def length(self) -> int: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "UiDataSliceConfig", op: int) -> bool: ...

class UiAccountEncoding:
    Binary: "UiAccountEncoding"
    Base58: "UiAccountEncoding"
    Base64: "UiAccountEncoding"
    JsonParsed: "UiAccountEncoding"
    Base64Zstd: "UiAccountEncoding"
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, o: object) -> bool: ...


class ParsedAccount:
    def __init__(
        self, program: str, parsed: str, space: int
    ) -> None: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "ParsedAccount", op: int) -> bool: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "ParsedAccount": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "ParsedAccount": ...
    @property
    def program(self) -> str: ...
    @property
    def parsed(self) -> str: ...
    @property
    def space(self) -> int: ...
