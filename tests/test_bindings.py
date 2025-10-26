import ctypes as C

import pytest

from ctypes_modbus.bindings import lib, call


RC_CALLS = []
SEGFAULTING = {"modbus_mask_write_register"}

for name in dir(lib):
    if name.startswith("modbus_") and name not in SEGFAULTING:
        func = getattr(lib, name)
        if func.restype == C.c_int:
            RC_CALLS.append(func)


@pytest.mark.parametrize("func", RC_CALLS)
def test_rc_call(func):
    with pytest.raises(OSError):
        call(func, *[t() for t in func.argtypes])


def test_modbus_new_rtu():
    ptr = call(lib.modbus_new_rtu, b"/dev/ttyS0", 19200, b"N", 8, 1)
    assert ptr > 0


def test_modbus_new_rtu_error():
    with pytest.raises(OSError):
        call(lib.modbus_new_rtu, b"", 19200, b"N", 8, 1)


def test_modbus_new_tcp():
    ptr = call(lib.modbus_new_tcp, b"127.0.0.1", 3333)
    assert ptr > 0


def test_modbus_new_tcp_error():
    with pytest.raises(OSError):
        call(lib.modbus_new_tcp, b"", 3333)
