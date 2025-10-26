import ctypes as C
import struct

from .bindings import lib, call


def unpack(data, size):
    return struct.unpack(f"<{size}H", data)


class Modbus:
    def __init__(self, ctx: C.c_void_p, logger=None):
        self._ctx = ctx
        self._logger = logger

    def __del__(self):
        self.close()

    @classmethod
    def TCP(cls, host="127.0.0.1", port=502, **kwargs):
        import socket

        ip = socket.getaddrinfo(host, None, socket.AF_INET, socket.SOCK_STREAM)[0][4][0]
        ctx = call(lib.modbus_new_tcp, ip.encode(), port)
        return cls(ctx, **kwargs)

    @classmethod
    def RTU(
        cls,
        device="/dev/ttyS0",
        baud=19200,
        parity="N",
        data_bit=8,
        stop_bit=1,
        **kwargs,
    ):
        ctx = call(
            lib.modbus_new_rtu,
            device.encode(),
            baud,
            parity.encode(),
            data_bit,
            stop_bit,
        )
        return cls(ctx, **kwargs)

    def _run(self, func, *args):
        if self._logger:
            self._logger.debug("CALL: %s%s", func.__name__, args)
        return call(func, self._ctx, *args)

    def get_socket(self):
        return self._run(lib.modbus_get_socket)

    def connect(self):
        self._run(lib.modbus_connect)

    def set_slave(self, slave):
        return self._run(lib.modbus_set_slave, slave)

    def get_response_timeout(self):
        sec = C.c_uint32()
        usec = C.c_uint32()
        self._run(lib.modbus_get_response_timeout, C.byref(sec), C.byref(usec))
        return sec.value + (usec.value / 1_000_000)

    def set_response_timeout(self, seconds):
        sec = int(seconds)
        usec = int((seconds - sec) * 1_000_000)
        self._run(lib.modbus_set_response_timeout, sec, usec)

    def close(self):
        if self._ctx:
            lib.modbus_close(self._ctx)
            self._ctx = None

    def flush(self):
        lib.modbus_flush(self._ctx)

    def read_bits(self, addr, nb, dest=None):
        dest = dest or (C.c_uint8 * nb)()
        self._run(lib.modbus_read_bits, addr, nb, dest)
        return unpack(dest, nb)

    def read_input_bits(self, addr, nb, dest=None):
        dest = dest or (C.c_uint8 * nb)()
        self._run(lib.modbus_read_input_bits, addr, nb, dest)
        return unpack(dest, nb)

    def read_registers(self, addr, nb, dest=None):
        dest = dest or (C.c_uint16 * nb)()
        self._run(lib.modbus_read_registers, addr, nb, dest)
        return unpack(dest, nb)

    def read_input_registers(self, addr, nb, dest=None):
        dest = dest or (C.c_uint16 * nb)()
        self._run(lib.modbus_read_input_registers, addr, nb, dest)
        return unpack(dest, nb)

    def write_bit(self, addr, status):
        self._run(lib.modbus_write_bit, addr, status)

    def write_register(self, addr, value):
        self._run(lib.modbus_write_register, addr, value)

    def write_bits(self, addr, nb, data):
        arr = (C.c_uint8 * nb)(*data)
        self._run(lib.modbus_write_bits, addr, nb, arr)

    def write_registers(self, addr, data):
        nb = len(data)
        arr = (C.c_uint16 * nb)(*data)
        self._run(lib.modbus_write_registers, addr, nb, arr)

    def write_and_read_registers(self, write_addr, data, read_addr, read_nb, dest=None):
        src = (C.c_uint16 * len(data))(*data)
        dest = dest or (C.c_uint16 * read_nb)()
        self._run(
            lib.modbus_write_and_read_registers,
            write_addr,
            len(data),
            src,
            read_addr,
            read_nb,
            dest,
        )
        return unpack(dest, read_nb)

    @staticmethod
    def uint8(nb):
        return (C.c_uint8 * nb)()

    @staticmethod
    def uint16(nb):
        return (C.c_uint16 * nb)()
