from brewtils import parameter
from brewtils.models import Parameter


@parameter(
    key="my_foo",
    display_name="Foo",
    optional=False,
    type="String",
    description="Foo With Defaults.",
    default="defaultFooFromModel",
)
@parameter(
    key="my_bar",
    display_name="Bar",
    optional=False,
    type="String",
    description="Bar With Defaults.",
    default="defaultBarFromModel",
)
class MyModelWithDefaults(object):
    pass


@parameter(
    key="my_choices_string",
    type="String",
    display_name="Choices!",
    optional=False,
    description="This has some choices",
    choices=["a", "b", "c"],
)
@parameter(
    key="my_list_of_strings",
    multi=True,
    display_name="My List of Strings",
    optional=False,
    type="String",
    description="Just testing a list of Strings.",
)
class MyListModel(object):
    pass


@parameter(
    key="my_nested_string",
    display_name="My Nested String",
    optional=False,
    type="String",
    description="Just Testing a String",
)
@parameter(
    key="my_nested_int",
    display_name="My Nested Int",
    optional=False,
    type="Integer",
    description="Just Testing an Int",
)
class MyNestedModel(object):
    pass


class MyModel(object):
    """Another way to declare model parameters

    This demonstrates the alternate method of declaring model parameters. Parameter
    objects (or dictionaries of Parameter kwargs) can be added to a ``parameters`` class
    attribute.

    """
    my_string = {
        "key": "my_string",
        "display_name": "My String",
        "description": "Just Testing a String",
        "type": "String",
        "optional": False,
    }
    my_string_with_choices = Parameter(
        key="my_string_with_choices",
        multi=False,
        optional=False,
        type="String",
        display_name="My String With Choices",
        description="Just Testing a String with choices",
        choices=["A", "B", "C"],
    )
    my_int = Parameter(
        key="my_int",
        multi=False,
        display_name="My Int",
        optional=False,
        type="Integer",
        description="Just Testing an Int",
    )
    my_float = {
        "key": "my_float",
        "display_name": "My Float",
        "description": "Just Testing a Float",
        "type": "Float",
        "optional": False,
    }
    my_bool = Parameter(
        key="my_bool",
        multi=False,
        display_name="My Bool",
        optional=False,
        type="Boolean",
        description="Just Testing a Boolean",
    )
    my_any = Parameter(
        key="my_any",
        multi=False,
        display_name="My Any",
        optional=False,
        type="Any",
        description="Just Testing an Any",
    )
    my_raw_dict = Parameter(
        key="my_raw_dict",
        multi=False,
        display_name="My Raw Dict",
        optional=False,
        type="Dictionary",
        description="Just Testing a Dictionary",
    )
    my_nested_model = Parameter(
        key="my_nested_model",
        multi=False,
        display_name="My Nested Model",
        optional=False,
        description="Just Testing a Nested Model",
        model=MyNestedModel,
    )
    my_list_of_strings = Parameter(
        key="my_list_of_strings",
        multi=True,
        display_name="My List of Strings",
        optional=False,
        type="String",
        description="Just testing a list of Strings.",
    )
    my_optional_string = Parameter(
        key="my_optional_string",
        display_name="My Optional",
        optional=True,
        type="String",
        description="Just testing an optional String.",
        default="test_opt",
    )
    my_nullable_string = Parameter(
        key="my_nullable_string",
        display_name="My Nullable String",
        optional=True,
        type="String",
        description="Just testing a nullable String.",
        nullable=True,
    )
    my_list_of_models = Parameter(
        key="my_list_of_models",
        multi=True,
        display_name="My List of Models",
        optional=False,
        type="Dictionary",
        description="Just Testing a list of Models",
        model=MyListModel,
    )

    parameters = [
        my_string,
        my_string_with_choices,
        my_int,
        my_float,
        my_bool,
        my_any,
        my_raw_dict,
        my_nested_model,
        my_list_of_strings,
        my_optional_string,
        my_nullable_string,
        my_list_of_models,
    ]
