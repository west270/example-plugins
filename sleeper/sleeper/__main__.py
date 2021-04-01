import logging
import time

from brewtils import parameter, Plugin

__version__ = "3.0.0.dev0"


class SleeperClient:
    def __init__(self):
        self._logger = logging.getLogger("sleeper")

    @parameter(
        key="amount", type="Float", description="Amount of time to sleep (in seconds)"
    )
    def sleep(self, amount):
        self._logger.info("About to sleep for %d seconds" % amount)

        time.sleep(amount)

        self._logger.info("I'm Awake!")


def main():
    plugin = Plugin(
        name="sleeper", version=__version__, description="A really lazy plugin",
    )
    plugin.client = SleeperClient()
    plugin.run()


if __name__ == "__main__":
    main()
