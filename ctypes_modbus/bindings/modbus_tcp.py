# script is auto-generated

"""Usage example:
import ctypes as C

from . import bind, bind_all

lib = ...


class CType:
    modbus_t_p = C.c_void_p
    int_p = C.c_void_p


bind_all(lib, CType)


"""

import ctypes as C


def bind(restype, func, *argtypes):
    func.restype = restype
    func.argtypes = argtypes


def bind_all(lib, ctx):
    # modbus_t *modbus_new_tcp(const char *ip_address, int port);
    bind(ctx.modbus_t_p, lib.modbus_new_tcp, C.c_char_p, C.c_int)
    # int modbus_tcp_listen(modbus_t *ctx, int nb_connection);
    bind(C.c_int, lib.modbus_tcp_listen, ctx.modbus_t_p, C.c_int)
    # int modbus_tcp_accept(modbus_t *ctx, int *s);
    bind(C.c_int, lib.modbus_tcp_accept, ctx.modbus_t_p, ctx.int_p)
    # modbus_t *modbus_new_tcp_pi(const char *node, const char *service);
    bind(ctx.modbus_t_p, lib.modbus_new_tcp_pi, C.c_char_p, C.c_char_p)
    # int modbus_tcp_pi_listen(modbus_t *ctx, int nb_connection);
    bind(C.c_int, lib.modbus_tcp_pi_listen, ctx.modbus_t_p, C.c_int)
    # int modbus_tcp_pi_accept(modbus_t *ctx, int *s);
    bind(C.c_int, lib.modbus_tcp_pi_accept, ctx.modbus_t_p, ctx.int_p)
