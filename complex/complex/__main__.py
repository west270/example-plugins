from __future__ import absolute_import

import sys

from brewtils import RemotePlugin, get_bg_connection_parameters
from .client import ComplexClient
from .errors import StartupError

__version__ = '1.0.0.dev0'


def main():
    if len(sys.argv) < 4:
        raise StartupError("%d arguments provided (3 required:'instance', "
                           "'host' and 'port')" % (len(sys.argv)-1))

    plugin = RemotePlugin(ComplexClient(sys.argv[2], sys.argv[3]),
                          name='complex', version=__version__, max_instances=2,
                          instance_name=sys.argv[1],
                          **get_bg_connection_parameters(sys.argv[4:]))
    plugin.run()


if __name__ == '__main__':
    main()
