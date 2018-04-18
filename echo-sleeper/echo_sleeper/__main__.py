from __future__ import absolute_import

import sys

from brewtils import RemotePlugin, get_bg_connection_parameters
from .client import EchoSleeperClient

__version__ = "1.0.0.dev0"


def main():
    connection_params = get_bg_connection_parameters(sys.argv[1:])

    plugin = RemotePlugin(EchoSleeperClient(connection_params),
                          name='echo-sleeper', version=__version__,
                          **connection_params)
    plugin.run()


if __name__ == '__main__':
    main()
