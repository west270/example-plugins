import json
import sys

from brewtils import command, get_connection_info, system, Plugin, SystemClient

__version__ = "1.0.0.dev0"

@system
class ParentClient:
    """A Client communicates with a child in a seperate namespace"""

    def __init__(self, params):
        self.child_client = SystemClient(system_name="child", system_namespace="CHILD_NAMESPACE", **params)

    @command()
    def who_am_i(self):
        return "Parent"

    @command()
    def child_who_am_i(self):
        response = self.child_client.who_am_i()

        return response.output


def main():
    connection_params = get_connection_info(sys.argv[1:])
    Plugin(
        ParentClient(connection_params),
        name="parent",
        version=__version__,
        **connection_params
    ).run()


if __name__ == "__main__":
    main()
