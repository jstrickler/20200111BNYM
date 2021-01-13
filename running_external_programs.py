from subprocess import run, PIPE, CalledProcessError

netstat_opts = "-an"

cmd = "netstat {}".format(netstat_opts)
cmd = f"netstat {netstat_opts}"

try:
    proc = run(cmd, stdout=PIPE)
    # if linux or Mac
    # run(cmd, shell=True)
except CalledProcessError as err:
    print(err.returncode)
else:
    remote_connections = []
    output_lines = proc.stdout.decode().splitlines()
    with open('nsout.txt', 'w') as ns_out:
        for line in output_lines:
            if 'ESTABLISHED' in line:
                fields = line.split()
                remote_connections.append(fields[2:4])
                ns_out.write('\t'.join(fields) + '\n')

for conn in remote_connections:
    print(conn)
