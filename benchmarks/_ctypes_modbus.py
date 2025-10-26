import os

from ctypes_modbus import Modbus

import benchmarks.constants as c

dev = os.getenv("DEV", None)

if dev:
    import logging

    logging.basicConfig(level=logging.DEBUG)

    mb = Modbus.RTU(dev, 115200, "N", 8, 1, logger=logging.getLogger())
    mb.set_slave(1)
else:
    mb = Modbus.TCP("localhost", 1502)

mb.connect()

if dev:
    import time

    i = 1
    while True:
        mb.write_registers(0, [i, i])
        i += 1
        data = mb.read_registers(0, 2)
        logging.info("REGISTERS: %s", [hex(n) for n in data])
        time.sleep(2)

else:
    mb.write_register(0, 17)
    dest = mb.uint16(1)
    for _ in range(c.N):
        mb.read_registers(0, 1, dest=dest)
