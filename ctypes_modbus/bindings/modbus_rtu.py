# script is auto-generated

"""Usage example:
import ctypes as C

from . import bind, bind_all

lib = ...


class CType:
    modbus_t_p = C.c_void_p


bind_all(lib, CType)

# int modbus_rtu_set_custom_rts(modbus_t *ctx, void (*set_rts)(modbus_t *ctx, int on));
bind(C.c_int, lib.modbus_rtu_set_custom_rts, ...)

"""

import ctypes as C


def bind(restype, func, *argtypes):
    func.restype = restype
    func.argtypes = argtypes


def bind_all(lib, ctx):
    # modbus_t * modbus_new_rtu(const char *device, int baud, char parity, int data_bit, int stop_bit);
    bind(
        ctx.modbus_t_p,
        lib.modbus_new_rtu,
        C.c_char_p,
        C.c_int,
        C.c_char,
        C.c_int,
        C.c_int,
    )
    # int modbus_rtu_set_serial_mode(modbus_t *ctx, int mode);
    bind(C.c_int, lib.modbus_rtu_set_serial_mode, ctx.modbus_t_p, C.c_int)
    # int modbus_rtu_get_serial_mode(modbus_t *ctx);
    bind(C.c_int, lib.modbus_rtu_get_serial_mode, ctx.modbus_t_p)
    # int modbus_rtu_set_rts(modbus_t *ctx, int mode);
    bind(C.c_int, lib.modbus_rtu_set_rts, ctx.modbus_t_p, C.c_int)
    # int modbus_rtu_get_rts(modbus_t *ctx);
    bind(C.c_int, lib.modbus_rtu_get_rts, ctx.modbus_t_p)
    # int modbus_rtu_set_rts_delay(modbus_t *ctx, int us);
    bind(C.c_int, lib.modbus_rtu_set_rts_delay, ctx.modbus_t_p, C.c_int)
    # int modbus_rtu_get_rts_delay(modbus_t *ctx);
    bind(C.c_int, lib.modbus_rtu_get_rts_delay, ctx.modbus_t_p)
