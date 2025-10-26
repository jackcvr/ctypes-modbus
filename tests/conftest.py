import socket
import threading

import pytest


@pytest.fixture
def tcp_port():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 0))
    server.listen(1)
    port = server.getsockname()[1]

    def handler():
        conn, _ = server.accept()
        conn.close()
        server.close()

    t = threading.Thread(target=handler, daemon=True)
    t.start()
    try:
        yield port
    finally:
        server.close()
        t.join(1)
        if t.is_alive():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(("127.0.0.1", port))
        t.join(1)
        assert not t.is_alive()
