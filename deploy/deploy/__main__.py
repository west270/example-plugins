from brewtils import Plugin, SystemClient, command, parameter, system

from . import resources

try:
    import importlib.resources as pkg_resources  # PY >= 3.7
except ImportError:
    import importlib_resources as pkg_resources  # PY < 3.7


__version__ = "1.0.0.dev0"


@parameter(key="foo", type="String", optional=False)
@parameter(key="bar", type="Bytes", optional=False)
class Model(object):
    pass


@system
class DeployClient(object):
    """Plugin that deploys other plugins"""

    # "Base" Commands
    @parameter(key="the_base64", type="Base64")
    def base64_command(self, the_base64):
        return the_base64

    @parameter(key="the_base64", type="Base64", optional=True, nullable=True)
    def base64_command_optional(self, the_base64):
        if the_base64:
            return the_base64
        else:
            return "no file selected"

    @parameter(key="the_bytes", type="Bytes")
    def bytes_command(self, the_bytes):
        return the_bytes

    @parameter(key="the_bytes", type="Bytes", multi=True)
    def bytes_multi_command(self, the_bytes):
        return the_bytes

    @parameter(key="bytes_model", model=Model)
    def bytes_model_command(self, bytes_model):
        return bytes_model

    # Invoker commands
    # Base64
    @command
    def base64_invoker_file(self):
        with pkg_resources.open_binary(resources, "favicon.ico") as f:
            return SystemClient().base64_command(the_base64=f).output

    # Bytes
    @command
    def bytes_invoker_literal(self):
        return SystemClient().bytes_command(the_bytes=b'im a byte').output

    @command
    def bytes_invoker_file(self):
        with pkg_resources.open_binary(resources, "favicon.ico") as f:
            return SystemClient().bytes_command(the_bytes=f).output

    @command
    def bytes_multi_invoker_literal(self):
        return SystemClient().bytes_multi_command(the_bytes=[b'abc', b'123']).output

    @command
    def bytes_model_invoker_literal(self):
        return SystemClient().bytes_model_command(
            bytes_model={"foo": "hi", "bar": b'im a byte'}
        ).output

    # Autoresolve
    @parameter(key="the_bytes", type="Bytes", type_info={"autoresolve": False})
    def bytes_no_resolve(self, the_bytes):
        return SystemClient().bytes_command(the_bytes=the_bytes).output

    @command
    def bytes_no_resolve_invoker(self):
        return SystemClient().bytes_no_resolve(the_bytes=b'im a byte').output


def main():
    p = Plugin(name="deploy", version=__version__)
    p.client = DeployClient()
    p.run()


if __name__ == "__main__":
    main()
