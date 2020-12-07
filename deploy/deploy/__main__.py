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
    @parameter(
        key="output_path",
        type="String",
        description="Where to extract the input file to. Default is the plugin directory.",
        optional=False,
        default="../"
    )
    def deploy(self, my_file, output_path):
        """Deploys the given file to the given directory."""
        z = ZipFile(my_file)
        z.extractall(output_path)
        return "Done!"

    @parameter(
        key="input_path",
        type="String",
        description="The input file path. Default uses FileTrigger parameter injection.",
        optional=False,
        default="{event/src_path}"
    )
    @parameter(
        key="output_path",
        type="String",
        description="Where to extract the input file to. Default is the plugin directory.",
        optional=False,
        default="../"
    )
    def monitor(self, input_path, output_path):
        """ Deploys the file found at the given path to the given directory.
            For best results, schedule a job using the 'file' trigger with this as its request."""
        z = ZipFile(input_path)
        z.extractall(output_path)
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
