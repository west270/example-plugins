from __future__ import absolute_import

import sys

from brewtils import get_connection_info, Plugin
from .client import ComplexClient
from .errors import StartupError

__version__ = '1.0.0.dev0'


def main():
    if len(sys.argv) < 4:
        raise StartupError("%d arguments provided (3 required:'instance', "
                           "'host' and 'port')" % (len(sys.argv)-1))

    Plugin(
        ComplexClient(sys.argv[2], sys.argv[3]),
        name='complex',
        version=__version__,
        instance_name=sys.argv[1],
        max_instances=2,
        **get_connection_info(sys.argv[4:])
    ).run()


if __name__ == '__main__':
    main()
