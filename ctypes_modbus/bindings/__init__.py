import ctypes as C
import errno

from ..core import load_library, LibraryError
from .modbus import bind, bind_all
from .modbus_rtu import bind_all as bind_all_rtu
from .modbus_tcp import bind_all as bind_all_tcp

lib = load_library("modbus")


class Struct:
    class Mapping(C.Structure):
        _fields_ = [
            ("nb_bits", C.c_int),
            ("start_bits", C.c_int),
            ("nb_input_bits", C.c_int),
            ("start_input_bits", C.c_int),
            ("nb_input_registers", C.c_int),
            ("start_input_registers", C.c_int),
            ("nb_registers", C.c_int),
            ("start_registers", C.c_int),
            ("tab_bits", C.POINTER(C.c_uint8)),
            ("tab_input_bits", C.POINTER(C.c_uint8)),
            ("tab_input_registers", C.POINTER(C.c_uint16)),
            ("tab_registers", C.POINTER(C.c_uint16)),
        ]


class Function:
    SET_RTS = C.CFUNCTYPE(None, C.c_void_p, C.c_int)


class CType:
    modbus_t_p = C.c_void_p
    modbus_error_recovery_mode = C.c_int
    uint32_t_p = C.POINTER(C.c_uint32)
    uint8_t_p = C.POINTER(C.c_uint8)
    uint16_t_p = C.POINTER(C.c_uint16)
    modbus_mapping_t_p = C.POINTER(Struct.Mapping)
    int_p = C.POINTER(C.c_int)


bind_all(lib, CType)
bind_all_rtu(lib, CType)
bind_all_tcp(lib, CType)

# int modbus_rtu_set_custom_rts(modbus_t *ctx, void (*set_rts)(modbus_t *ctx, int on));
bind(C.c_int, lib.modbus_rtu_set_custom_rts, CType.modbus_t_p, Function.SET_RTS)


def strerror(code):
    return lib.modbus_strerror(code).decode()


class ModbusError(LibraryError):
    def strerror(self):
        return strerror(self.code)


def throw(code=None):
    code = code or C.get_errno()
    if code in errno.errorcode:
        raise OSError(code, strerror(code))
    raise ModbusError(code)


def call(func, *args):
    ret = func(*args)
    if func.restype == C.c_int and ret == -1:
        throw()
    elif func.restype == C.c_void_p and ret is None:
        throw()
    return ret
