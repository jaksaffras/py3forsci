import os

cmd = "netstat -n"

os.system(cmd)
print('-' * 60)

with os.popen(cmd) as cmd_in:
    for raw_line in cmd_in:
        if "ESTABLISHED" in raw_line:
            line = raw_line.rstrip()
            proto, recq, sendq, local, foreign, state = line.split()
            foreign_ip_bytes = foreign.split('.')[:4]
            foreign_ip = '.'.join(foreign_ip_bytes)
            if foreign_ip.startswith('1'):
                os.system(f'ping -c 3 {foreign_ip}')
            print(f"{local:25s} {foreign}")

# x = os.popen(...)
