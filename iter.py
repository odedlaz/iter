import os
from flask import Flask, render_template
from collections import namedtuple
from socket import gethostname
from docker import APIClient as Docker

Site = namedtuple('Site', ['name', 'url'])


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
            url = url_fmt.format(port_config['PublicPort'])
            yield Site(name=chostname, url=url)


app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', sites=get_sites())


if __name__ == '__main__':
    server_name = os.getenv('SERVER_NAME')
    assert server_name is not None
    url_fmt = "http://{}:{{}}".format(server_name)

    hostname = gethostname()
    docker = Docker()

    app.run(host="0.0.0.0", port=80, debug=False)
