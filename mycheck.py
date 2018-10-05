
import sys    
import json  
import socket


def check_connection(hostname):
    ip_address = hostname.split(':')[0]
    port = hostname.split(':')[1]
    try:
        socket.create_connection((ip_address, port))
        return True
    except OSError:
        pass
    return False


def check_connectivity_file(file_name):
    file_obj = open(file_name, "r")
    content = json.loads(file_obj.read())
    sites = content['checks']['ping']
    for name, hostname in sites.items():
        if check_connection(hostname):
            output = 'ok {}'
        else:
            output = 'No {}'
        print(output.format(name))

if __name__ == '__main__':
    FILE = sys.argv[1]
    check_connectivity_file(FILE)
