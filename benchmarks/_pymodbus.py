import asyncio
import os  # noqa

import pymodbus.client as modbus

import benchmarks.constants as c


async def main():
    client = modbus.AsyncModbusTcpClient("localhost", port=1502)
    await client.connect()
    await client.write_registers(0, [17])

    for _ in range(c.N):
        await client.read_holding_registers(0, count=1)


asyncio.run(main())
