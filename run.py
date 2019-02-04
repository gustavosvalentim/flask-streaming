import os, sys

from rpiMediaStream.config_parser import Config


ROOTPATH = os.path.abspath(os.path.dirname(__file__))
CONFIGPATH = os.path.join(ROOTPATH, 'config.cfg')
config = Config(CONFIGPATH)

PORT = config.PORT

if config.TYPE.upper() == 'SERVER':
    from rpiMediaStream.server import app

if config.TYPE.upper() == 'CLIENT':
    from rpiMediaStream.client import app


app.run(host='0.0.0.0', port=int(PORT), debug=True)
