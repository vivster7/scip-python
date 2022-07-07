# This sample tests the synthesized methods get, setdefault
# pop, and __delitem__ for a TypedDict.

# pyright: strict

from typing import Optional, TypedDict, Union, final
from typing_extensions import NotRequired, Required


class TD1(TypedDict):
    bar: NotRequired[str]


class TD2(TD1):
    foo: Required[str]


td1: TD1 = {}
td2: TD2 = {"foo": "hi"}

v1: Optional[str] = td1.get("bar")

v2: str = td1.get("bar", "")

v3: Union[str, int] = td1.get("bar", 3)

v4: str = td1.setdefault("bar", "1")

# This should generate an error.
td1.setdefault("bar", 3)

# This should generate an error.
td1.setdefault("bar")

# This should generate an error.
td1.setdefault("baz", "")

v6: str = td1.pop("bar")
v7: str = td1.pop("bar", "none")
v8: Union[str, int] = td1.pop("bar", 3)

# This should generate an error.
v9: str = td2.pop("foo")

td1.__delitem__("bar")


@final
class A(TypedDict):
    foo: int
    baz: NotRequired[int]


class B(TypedDict):
    bar: str


C = Union[A, B]


def test(a: A, b: B, c: C, s: str) -> Optional[int]:
    a1 = a.get("foo")
    reveal_type(a1, expected_text="int")
    a2 = a.get("foo", 1.0)
    reveal_type(a2, expected_text="int")
    a3 = a.get("bar")
    reveal_type(a3, expected_text="None")
    a4 = a.get("bar", 1.0)
    reveal_type(a4, expected_text="float")
    a5 = a.get("baz")
    reveal_type(a5, expected_text="int | None")
    a6 = a.get("baz", 1.0)
    reveal_type(a6, expected_text="int | float")
    a7 = a.get(s)
    reveal_type(a7, expected_text="Any | None")
    a8 = a.get(s, 1.0)
    reveal_type(a8, expected_text="Any | float")

    b1 = b.get("bar")
    reveal_type(b1, expected_text="str")
    b2 = b.get("bar", 1.0)
    reveal_type(b2, expected_text="str")
    b3 = b.get("foo")
    reveal_type(b3, expected_text="Any | None")
    b4 = b.get("foo", 1.0)
    reveal_type(b4, expected_text="Any | float")
    b5 = b.get(s)
    reveal_type(b5, expected_text="Any | None")
    b6 = b.get(s, 1.0)
    reveal_type(b6, expected_text="Any | float")

    c1 = c.get("foo")
    reveal_type(c1, expected_text="int | Any | None")
    c2 = c.get("foo", 1.0)
    reveal_type(c2, expected_text="int | Any | float")
    c3 = c.get("bar")
    reveal_type(c3, expected_text="str | None")
    c4 = c.get("bar", 1.0)
    reveal_type(c4, expected_text="float | str")
    c5 = c.get("baz")
    reveal_type(c5, expected_text="int | Any | None")
    c6 = c.get("baz", 1.0)
    reveal_type(c6, expected_text="int | float | Any")
