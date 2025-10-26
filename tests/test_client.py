import errno

import pytest

from ctypes_modbus import Modbus


def test_modbus_tcp(tcp_port):
    Modbus.TCP("localhost", tcp_port).connect()


def test_modbus_tcp_conn_refused():
    client = Modbus.TCP("localhost", 999999)
    with pytest.raises(ConnectionRefusedError):
        client.connect()


def test_modbus_rtu_error():
    with pytest.raises(OSError) as e:
        Modbus.RTU("")
    assert e.value.errno == errno.EINVAL
