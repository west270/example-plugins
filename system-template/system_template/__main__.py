import pathlib

from brewtils import Plugin, parameter

__version__ = "3.0.0.dev0"


template_path = str(pathlib.Path(__file__).parent) + "/resources/template.html"


class SystemTemplateClient(object):
    @parameter(
        key="message",
        type="String",
        description="The Message to be Echoed",
        optional=True,
        default="Hello, World!",
    )
    def placeholder_command(self, message, loud):
        """The template won't display if there aren't any commands..."""
        return message


def main():
    plugin = Plugin(
        name="system-template",
        version=__version__,
        description="Plugin that demonstrates system templates",
        template=template_path,
    )
    plugin.client = SystemTemplateClient()
    plugin.run()


if __name__ == "__main__":
    main()
