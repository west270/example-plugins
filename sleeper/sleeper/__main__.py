from __future__ import absolute_import

import sys

from brewtils import load_config
from brewtils.plugin import PluginBase
from .client import SleeperClient

__version__ = "1.0.0.dev0"


def main():
    plugin = PluginBase(SleeperClient(1), name='sleeper', version=__version__,
                        **load_config())
    plugin.run()


if __name__ == '__main__':
    main()
