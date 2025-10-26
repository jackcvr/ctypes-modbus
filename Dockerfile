FROM python:3.14-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential autoconf automake libtool git ca-certificates time libmodbus5

RUN git clone https://github.com/stephane/libmodbus.git \
    && cd libmodbus \
    && ./autogen.sh \
    && ./configure --disable-dependency-tracking \
    && make -j$(nproc)

RUN git clone https://github.com/pymodbus-dev/pymodbus.git

ENV PYTHONUNBUFFERED=1

RUN pip install \
    build \
    twine \
    pyserial \
    pymodbus \
    pylibmodbus \
    pytest \
    pytest-asyncio \
    matplotlib

WORKDIR /app

ADD . .

RUN pip install -e .
