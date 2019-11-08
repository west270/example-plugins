import os
import sys

from brewtils import command, get_connection_info, parameter, system, Plugin

__version__ = "1.0.0.dev0"


@system
class DynamicClient(object):
    """Plugin that repeats very specific stuff."""

    STATIC_CHOICES = ["a", "b", "c"]

    STATIC_CHOICES_RENAMED = [
        {"value": "a", "text": "A"},
        {"value": "b", "text": "B"},
        {"value": "c", "text": "C"},
    ]

    STATIC_CHOICES_DICTIONARY = {
        "a": ["r", "s", "t"],
        "b": ["u", "v", "w"],
        "c": ["x", "y", "z"],
        None: [],  # Want 'null' value to be the union of all values
    }
    for value in STATIC_CHOICES_DICTIONARY.values():
        STATIC_CHOICES_DICTIONARY[None] = STATIC_CHOICES_DICTIONARY[None] + value

    INSTANCE_CHOICES_DICTIONARY = {
        "d1": ["100", "101", "111"],
        "d2": ["200", "202", "222"],
    }

    CHOICES_FILE = os.getenv("CHOICES_FILE", "http://example.com/api/choices.json")
    CHOICES_URL = os.getenv("CHOICES_URL", "http://example.com/api")

    @command
    def _get_attribute(self, attribute):
        return getattr(self, attribute)

    @command(command_type="INFO", output_type="JSON")
    def get_choices(self):
        return self.STATIC_CHOICES

    @command(command_type="INFO", output_type="JSON")
    def get_choices_renamed(self):
        return self.STATIC_CHOICES_RENAMED

    @command
    def get_choices_dictionary(self):
        return self.STATIC_CHOICES_DICTIONARY

    @parameter(key="key", type="String", choices=STATIC_CHOICES)
    @command(command_type="INFO", output_type="JSON")
    def get_choices_with_argument(self, key):
        return self.STATIC_CHOICES_DICTIONARY[key]

    @parameter(key="key", type="String")
    @command(command_type="INFO", output_type="JSON")
    def get_choices_with_instance_argument(self, key):
        return self.INSTANCE_CHOICES_DICTIONARY[key]

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices=STATIC_CHOICES,
    )
    def say_specific(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={"value": STATIC_CHOICES_RENAMED, "display": "select"},
    )
    def say_specific_renamed(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={
            "type": "static",
            "value": STATIC_CHOICES,
            "display": "typeahead",
            "strict": False,
        },
    )
    def say_specific_non_strict_typeahead(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={
            "type": "static",
            "value": STATIC_CHOICES,
            "display": "typeahead",
            "strict": True,
        },
    )
    def say_specific_strict_typeahead(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={"type": "url", "value": CHOICES_FILE},
    )
    def say_specific_from_url(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        nullable=True,
        choices={"type": "url", "value": CHOICES_FILE},
    )
    def say_specific_from_url_nullable(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={"type": "command", "value": "get_choices"},
    )
    def say_specific_from_command(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={
            "type": "command",
            "value": {
                "command": "get_choices",
                "system": "dynamic",
                "version": "1.0.0.dev",
                "instance_name": "default",
            },
        },
    )
    def say_specific_from_command_fully_specified(self, message):
        return message

    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        nullable=True,
        choices={"type": "command", "value": "get_choices"},
    )
    def say_specific_from_command_nullable(self, message):
        return message

    @parameter(
        key="index", type="String", choices=STATIC_CHOICES, default="a", is_kwarg=True
    )
    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={
            "type": "command",
            "display": "select",
            "strict": True,
            "value": "get_choices_with_argument(key=${index})",
        },
    )
    def say_specific_with_choices_argument(self, message, **_):
        return message

    @parameter(
        key="file", type="String", choices=STATIC_CHOICES, default="a", is_kwarg=True
    )
    @parameter(
        key="message",
        type="String",
        description="Say what we want",
        optional=False,
        choices={
            "type": "url",
            "display": "select",
            "strict": True,
            "value": CHOICES_URL+"?file=${file}",
        },
    )
    def say_specific_from_url_with_parameter(self, message, **_):
        return message

    @parameter(
        key="dict_key",
        type="String",
        nullable=True,
        is_kwarg=True,
        choices=list(STATIC_CHOICES_DICTIONARY),
    )
    @parameter(
        key="message",
        type="String",
        description="I depend on 'dict_key'",
        nullable=True,
        choices={
            "type": "static",
            "value": STATIC_CHOICES_DICTIONARY,
            "key_reference": "${dict_key}",
        },
    )
    def say_specific_dictionary_with_key_reference(self, message, **_):
        return message

    @parameter(
        key="message",
        type="String",
        description="I depend on the instance",
        nullable=True,
        choices={
            "type": "static",
            "value": INSTANCE_CHOICES_DICTIONARY,
            "key_reference": "${instance_name}",
        },
    )
    def say_specific_dictionary_with_instance_name_key(self, message):
        return message


def main():
    Plugin(
        DynamicClient(),
        name="dynamic",
        version=__version__,
        max_instances=2,
        **get_connection_info(sys.argv[1:])
    ).run()


if __name__ == "__main__":
    main()
