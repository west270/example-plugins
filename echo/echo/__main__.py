from brewtils import command, parameter, system, Plugin

__version__ = "3.0.0.dev0"


@system
class EchoClient(object):
    """Client that echos things"""

    @parameter(
        key="message",
        type="String",
        description="The Message to be Echoed",
        optional=True,
        default="Hello, World!",
    )
    @parameter(
        key="loud",
        type="Boolean",
        description="Determines if Exclamation marks are added",
        optional=True,
        default=False,
    )
    def say(self, message, loud):
        """Echos!"""
        return message + "!!!!!!!!!" if loud else message

    @command(output_type="JSON")
    @parameter(
        key="message",
        type="String",
        description="The Message to be Echoed",
        optional=True,
        default='{"str": "value", "nums": [1, 17], "obj": {"nested": "sweet"}}',
    )
    def say_json(self, message):
        """Echos with JSON output_type"""
        return message

    @command(output_type="HTML")
    @parameter(
        key="message",
        type="String",
        description="The Message to be Echoed",
        optional=True,
        default="<h1>Hello, World</h1>",
    )
    def say_html(self, message):
        """Echos with HTML output_type"""
        return message


def main():
    plugin = Plugin(
        name="echo",
        version=__version__,
        description="Annoying plugin that just repeats stuff",
    )
    plugin.client = EchoClient()
    plugin.run()


if __name__ == "__main__":
    main()
