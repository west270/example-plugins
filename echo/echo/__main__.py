import sys

from brewtils import (command, parameter, system, RemotePlugin, \
                      get_bg_connection_parameters)

__version__ = '1.0.0.dev0'


@system
class EchoClient(object):
    """Client that echos things"""

    @parameter(key="message", description="The Message to be Echoed", optional=True, type="String", default="Hello, World!")
    @parameter(key="loud", description="Determines if Exclamation marks are added", optional=True, type="Boolean", default=False)
    def say(self, message="Hello, World!", loud=False):
        if loud:
            message += "!!!!!!!!!"

        return message

    @command(output_type='JSON')
    @parameter(key="message", description="The Message to be Echoed", optional=True, type="String",
                  default='{"str": "value", "nums": [1, 2, 17], "obj": {"nested": "awesome"}}')
    def say_json(self, message="Hello, World!"):
        """Echos with JSON output_type"""
        return message


def main():
    plugin = RemotePlugin(EchoClient(), name='echo', version=__version__,
                          **get_bg_connection_parameters(sys.argv[1:]))
    plugin.run()


if __name__ == '__main__':
    main()
