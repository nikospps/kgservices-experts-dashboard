import paramiko
import json

#Available endpoint: group, fleet,asset, driver, event, route
def pam_ssh(endpoint):
    host = "87.98.132.245"
    port = 64118
    username = "root"
    password = "2/sA%JF*"

    command = "curl localhost:3000/api/" + endpoint + " -H 'Accept: application/json'"
    # command = "curl localhost:3000/api/fleet -H 'Accept: application/json'"
    # command = "curl localhost:3000/api/asset -H 'Accept: application/json'"
    # command = "curl localhost:3000/api/driver -H 'Accept: application/json'"
    # command = "curl localhost:3000/api/event -H 'Accept: application/json'"
    # command = "curl localhost:3000/api/route -H 'Accept: application/json'"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)

    stdin, stdout, stderr = ssh.exec_command(command)
    lines = json.loads(stdout.readlines()[0])
    return (lines['data'])
    # print(lines['data'])

