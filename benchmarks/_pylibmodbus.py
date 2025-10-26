import os  # noqa

from pylibmodbus import ModbusTcp

import benchmarks.constants as c

mb = ModbusTcp("127.0.0.1", 1502)
mb.connect()
mb.write_register(0, 17)

for _ in range(c.N):
    data = mb.read_registers(0, 1)
