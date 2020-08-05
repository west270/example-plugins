import sys

from brewtils import command, get_connection_info, parameter, system, Plugin

__version__ = "1.0.0.dev0"


@system
class CustomDisplayClient(object):

    @command(form=[{"key": "parameters.message", "readonly": True}])
    @parameter(key="message", type="String", optional=False, nullable=False)
    def echo_message_custom_form_as_list(self, message="Can't change me! Hahaha!"):
        """form=[{"key": "parameters.message", "readonly": True}]"""
        return message

    @command(
        form={
            "type": "fieldset",
            "items": [{"key": "parameters.message", "readonly": True}],
        }
    )
    @parameter(key="message", type="String", optional=False, nullable=False)
    def echo_message_custom_form_as_dict(self, message="Can't change me! Hahaha!"):
        """form={"type": "fieldset", "items": [{"key": "parameters.message", "readonly": True}]}"""
        return message

    @command(form="./resources/say_form.json")
    @parameter(key="message", type="String", optional=False, nullable=False)
    @parameter(key="loud", type="Boolean")
    def echo_message_custom_form_from_file(self, message="Hello world!", loud=False):
        """form='./resources/say_form.json'"""
        return message + "!!!!!!!!!" if loud else message

    @command(
        schema={
            "message": {
                "type": "string",
                "readonly": True,
                "default": "Default in schema!",
            }
        }
    )
    @parameter(key="message", type="String", optional=False, nullable=False)
    def echo_message_custom_schema(self, message="Can't change me! Hahaha!"):
        """schema={"message":{'type': 'string','readonly': True,'default':'Default in schema!'}}"""
        return message

    @parameter(
        key="message",
        type="String",
        optional=False,
        nullable=False,
        form_input_type="textarea",
    )
    def echo_message_textarea(self, message):
        return message

    @parameter(
        key="messages",
        type="String",
        multi=True,
        optional=False,
        nullable=False,
        form_input_type="textarea",
    )
    def echo_message_list_textarea(self, messages):
        return messages

    @parameter(
        key="message",
        type="Dictionary",
        optional=False,
        nullable=False,
        form_input_type="textarea",
    )
    def echo_message_dictionary(self, message):
        return message

    @command(template="./resources/minimalist.html")
    def echo_minimalist(self, message):
        return message

    @command(template="./resources/d3.html")
    def echo_minimalist_d3(self, message):
        return message

    @command(command_type="INFO", output_type="JS", hidden=True)
    def _d3(self):
        """Return the minimized d3 library

        Side note: Correctly getting static files to survive the Python packaging
        process is... not fun. If you want to be able to package this plugin and push
        it up to PyPI you need to do some stuff to ensure that this method will be able
        to find 'd3.min.js' when it runs:

        - Add a conditional dependency importlib_resources for Python < 3.7 in setup.py
        - Ensure the 'resources' directory is a python package (has an __init__.py)
        - Use something like this implementation to import 'resources' and load the file
        - Ensure that every resource file you need is added to package_data and / or
          data_files and include_package_data is set correctly in setup.py, and that
          all the files are in MANIFEST.in (I know, this is terrible. If you know a
          better way to ensure this works in all cases PLEASE open a PR).

        If you don't care about all that you can just do something simpler like below.
        Just be aware that if you ever try to `pip install` your plugin you'll have a
        bad time:

            with open("custom_display/resources/d3.min.js") as f:
                return f.read()
        """
        try:
            import importlib.resources as pkg_resources  # PY >= 3.7
        except ImportError:
            import importlib_resources as pkg_resources  # PY < 3.7

        from . import resources

        return pkg_resources.read_text(resources, 'd3.min.js')


def main():
    Plugin(
        CustomDisplayClient(),
        name="custom-display",
        version=__version__,
        **get_connection_info(sys.argv[1:])
    ).run()


if __name__ == "__main__":
    main()
