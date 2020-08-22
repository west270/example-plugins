from __future__ import absolute_import

from brewtils import Plugin

from .client import EchoSleeperClient

__version__ = "3.0.0.dev0"


def main():
    plugin = Plugin(
        name="echo-sleeper",
        version=__version__,
        description="A plugin that's annoying AND lazy",
    )
    plugin.client = EchoSleeperClient()
    plugin.run()


if __name__ == "__main__":
    main()
