from brewtils import Plugin, SystemClient, command, system

__version__ = "3.0.0.dev0"


@system
class ParentClient:
    """A Client communicates with a child in a seperate namespace"""

    def __init__(self):
        self.child_client = SystemClient(system_name="child", system_namespace="child")

    @command()
    def who_am_i(self):
        return "Parent"

    @command()
    def child_who_am_i(self):
        return self.child_client.who_am_i().output


def main():
    plugin = Plugin(
        name="parent",
        version=__version__,
        description="Issues commands to a different namespace",
    )
    plugin.client = ParentClient()
    plugin.run()


if __name__ == "__main__":
    main()
