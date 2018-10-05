"""
Program that checks connectivity to sites
"""
import sys     # dependency used to get arguments
import json    # dependency used to convert text to json
import socket  # dependency used to create connection to tcp services


def check_connection(hostname):
    """
    Connect to a TCP service listening on the internet address
    """
    ip_address = hostname.split(':')[0]
    port = hostname.split(':')[1]
    try:
        socket.create_connection((ip_address, port))
        return True
    except OSError:
        pass
    return False


def check_connectivity_file(file_name):
    """
    Open file and get hostname to test connectivity
    """
    file_obj = open(file_name, "r")
    content = json.loads(file_obj.read())
    sites = content['checks']['ping']
    for name, hostname in sites.items():
        if check_connection(hostname):
            output = 'ok : {}'
        else:
            output = 'No : {}'
        print(output.format(name))

if __name__ == '__main__':
    FILE = sys.argv[1]
    check_connectivity_file(FILE)
