import subprocess as sp  # nosec
import sys
import shlex

APPS = sys.argv[1].split(",")


def _run(cmd):
    p = sp.run(  # nosec
        shlex.split(f"/usr/bin/time -f '%e;%M' {cmd}"),
        capture_output=True,
        text=True,
    )
    if p.returncode != 0:
        print(p.stderr, file=sys.stderr)
        return p.stderr.splitlines()[-1].strip()
    return p.stderr.strip()


pymem = int(_run("python -c 'pass'").split(";")[1])
print("Module;Time;RSS")
for app in APPS:
    time, mem = _run(f"python -m benchmarks._{app}").split(";")
    mem = int(mem) - pymem
    print(f"{app};{time};{mem}")
