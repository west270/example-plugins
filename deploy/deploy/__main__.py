import sys
from zipfile import ZipFile

from brewtils import command, get_connection_info, parameter, system, Plugin

__version__ = "1.0.0.dev0"


@system
class DeployClient(object):
    """Client that deploys other plugins"""
    @parameter(
        key="my_file",
        type="Base64",
        description="The zipped plugin to deploy",
        optional=False,
    )
    def deploy(self, my_file):
        """Deploys the given file to the plugin directory."""
        z = ZipFile(my_file)
        z.extractall('../')
        return "Done!"

    @parameter(
        key="my_path",
        type="String",
        description="The full file path for a file to deploy",
        optional=False,
        default="{event/src_path}"
    )
    def monitor(self, my_path):
        """
        Deploys the file found at the given path to the plugin directory.
            For best results, schedule a job using the 'file' trigger with this as its request.
        """
        z = ZipFile(my_path)
        z.extractall('../')
        return "Done!"

    @parameter(
        key="my_file",
        type="Base64",
        description="Any file",
        optional=False,
    )
    def echo(self, my_file):
        """Echoes the contents of the given file."""
        try:
            return my_file.read().decode('utf-8')
        except UnicodeError:
            my_file.seek(0)
            return my_file.read()


def main():
    p = Plugin(
        DeployClient(),
        name="deploy",
        version=__version__,
        **get_connection_info(sys.argv[1:])
    )
    p.run()


if __name__ == "__main__":
    main()
