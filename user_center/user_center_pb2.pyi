from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class NewCaptchaResponse(_message.Message):
    __slots__ = ("code", "message", "serial", "image", "expire_sec", "text")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_SEC_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    serial: str
    image: str
    expire_sec: int
    text: str
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., serial: _Optional[str] = ..., image: _Optional[str] = ..., expire_sec: _Optional[int] = ..., text: _Optional[str] = ...) -> None: ...

class NewJWKSRequest(_message.Message):
    __slots__ = ("issuss", "key_qty")
    ISSUSS_FIELD_NUMBER: _ClassVar[int]
    KEY_QTY_FIELD_NUMBER: _ClassVar[int]
    issuss: _containers.RepeatedScalarFieldContainer[str]
    key_qty: int
    def __init__(self, issuss: _Optional[_Iterable[str]] = ..., key_qty: _Optional[int] = ...) -> None: ...

class NewJWKSResponse(_message.Message):
    __slots__ = ("code", "message", "status")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    status: bool
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., status: bool = ...) -> None: ...

class UserRegistryRequest(_message.Message):
    __slots__ = ("username", "password", "mobile", "email", "serial", "code")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    mobile: str
    email: str
    serial: str
    code: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ..., mobile: _Optional[str] = ..., email: _Optional[str] = ..., serial: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class UserRegistryResponse(_message.Message):
    __slots__ = ("code", "message", "uid", "token", "expire_sec")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_SEC_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    uid: int
    token: str
    expire_sec: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., uid: _Optional[int] = ..., token: _Optional[str] = ..., expire_sec: _Optional[int] = ...) -> None: ...

class UserLoginRequest(_message.Message):
    __slots__ = ("password", "mobile", "email", "serial", "code")
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    MOBILE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    password: str
    mobile: str
    email: str
    serial: str
    code: str
    def __init__(self, password: _Optional[str] = ..., mobile: _Optional[str] = ..., email: _Optional[str] = ..., serial: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class UserLoginResponse(_message.Message):
    __slots__ = ("code", "message", "uid", "token", "expire_sec")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_SEC_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    uid: int
    token: str
    expire_sec: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., uid: _Optional[int] = ..., token: _Optional[str] = ..., expire_sec: _Optional[int] = ...) -> None: ...

class UpdateTokenResponse(_message.Message):
    __slots__ = ("code", "message", "token", "expire_sec")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_SEC_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    token: str
    expire_sec: int
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., token: _Optional[str] = ..., expire_sec: _Optional[int] = ...) -> None: ...
