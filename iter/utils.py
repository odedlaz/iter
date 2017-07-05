import os
from collections import namedtuple
from socket import gethostname
from docker import APIClient as Docker

Site = namedtuple('Site', ['name', 'url'])


server_name = os.getenv('SERVER_NAME')
assert server_name is not None
url_fmt = "http://{}:{{}}".format(server_name)

hostname = gethostname()
docker = Docker()


def get_sites():
    for c in docker.containers():
        cid = c.get('Id', None)

        if not cid:
            continue

        cinspect = docker.inspect_container(cid)
        chostname = cinspect.get('Config', {}).get('Hostname')

        if not chostname or chostname == hostname:
            continue

        for port_config in c['Ports']:

            if int(port_config['PrivatePort']) != 80:
                continue

            url = url_fmt.format(port_config['PublicPort'])
            yield Site(name=chostname, url=url)
