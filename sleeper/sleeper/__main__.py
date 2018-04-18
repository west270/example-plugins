import sys
import time

from brewtils import (parameter, system, RemotePlugin, \
                      get_bg_connection_parameters)

__version__ = "1.0.0.dev0"


@system
class SleeperClient:

    @parameter(key="amount", type="Float", description="Amount of time to sleep (in seconds)")
    def sleep(self, amount):
        print("About to sleep for %d" % amount)
        time.sleep(amount)
        print("I'm Awake!")


def main():
    plugin = RemotePlugin(SleeperClient(), name='sleeper', version=__version__,
                          **get_bg_connection_parameters(sys.argv[1:]))
    plugin.run()


if __name__ == '__main__':
    main()
