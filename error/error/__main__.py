import json

from brewtils import command, Plugin

__version__ = "3.0.0.dev0"


class FooMessage(object):
    def __init__(self, message, more):
        self.message = message
        self.more = more


class ErrorClient:
    """A Client that always errors. There is no hope."""

    @command
    def string_error_message(self):
        """Error where the message is just a normal string."""
        raise ValueError("This is just a simple string.")

    @command
    def json_string_error_message(self):
        """Error where the message is a normal string but in JSON format."""
        raise ValueError(json.dumps({"foo": "bar"}))

    @command
    def no_error_message(self):
        """Error where the message is None"""
        raise ValueError()

    @command
    def list_error_message(self):
        """Error where the message is actually a JSON Serializable list."""
        raise ValueError(["foo", "bar", 1, True, None])

    @command
    def dictionary_error_message(self):
        """Error where the message is actually a JSON Serializable dictionary."""
        raise ValueError({"a": "foo", "b": "bar", "c": 1, "d": True, "e": None})

    @command
    def unknown_object_for_message(self):
        """Error where the message is an unknown object type."""
        raise ValueError(FooMessage("This is my message.", "more stuff"))

    @command(output_type="JSON")
    def error_string_output_type_json(self):
        """Error where the message is a string an the output type is JSON."""
        raise ValueError("This is a string")

    @command(output_type="JSON")
    def error_json_output_type_json(self):
        """Error where the message is JSON an the output type is JSON."""
        raise ValueError(json.dumps({"foo": "bar"}))


def main():
    plugin = Plugin(
        name="error",
        version=__version__,
        description="All commands end in errors. There is no hope.",
    )
    plugin.client = ErrorClient()
    plugin.run()


if __name__ == "__main__":
    main()
