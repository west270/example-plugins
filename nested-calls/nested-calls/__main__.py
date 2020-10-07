from brewtils import Plugin, command, system, SystemClient

__version__ = "1.0.0.dev0"


@system
class NestedCallClient:
    """A client that calls nested commands as System Clients"""

    nestedCallsClient = None

    def post_init(self):
        self.nestedCallsClient = SystemClient(system_name="nested-calls")

    @command(description="Start Commands at Level One")
    def level_1(self):
        """Starts Commands at Level One"""

        return self.nestedCallsClient.level_2()

    @command(description="Start Commands at Level Two")
    def level_2(self):
        """Starts Commands at Level One"""

        return self.nestedCallsClient.level_3()

    @command(description="Start Commands at Level Three")
    def level_3(self):
        """Starts Commands at Level Three"""

        return self.nestedCallsClient.level_4()

    @command(description="Start Commands at Level Four")
    def level_4(self):
        """Starts Commands at Level Four"""

        return self.nestedCallsClient.level_5()

    @command(description="Start Commands at Level Five")
    def level_5(self):
        """Starts Commands at Level Five"""

        return "Success"


def main():
    plugin = Plugin(
        name="nested-calls",
        version=__version__,
        description="A plugin that's calls commands in itself as System Clients",
    )
    plugin.client = NestedCallClient()
    plugin.client.post_init()
    plugin.run()


if __name__ == "__main__":
    main()
