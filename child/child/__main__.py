from brewtils import Plugin, command, system

__version__ = "3.0.0.dev0"


@system
class ChildClient:

    @command()
    def who_am_i(self):
        return "Child"


def main():
    Plugin(
        ChildClient(),
        name="child",
        version=__version__,
        namespace="child",
    ).run()


if __name__ == "__main__":
    main()
