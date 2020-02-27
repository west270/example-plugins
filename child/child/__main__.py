import json
import sys

from brewtils import command, get_connection_info, system, Plugin

__version__ = "1.0.0.dev0"


@system
class ChildClient:
    """A Client communicates with a parent"""

    @command()
    def who_am_i(self):
        return "Child"


def main():
    Plugin(
        ChildClient(),
        name="child",
        version=__version__,
        **get_connection_info(sys.argv[1:])
    ).run()


if __name__ == "__main__":
    main()
