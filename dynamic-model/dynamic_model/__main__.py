from brewtils import Plugin, command, parameter, system
from brewtils.models import Parameter

__version__ = "3.0.0.dev0"


class SameLevelModel(object):
    """Model that has two Parameters, one of which depends on the other"""

    faz = Parameter(
        key="faz",
        type="Integer",
        default=4,
        optional=False,
        choices="choices_cmd(param=${baz})",
    )
    baz = Parameter(
        key="baz",
        type="Integer",
        default=4,
        optional=False,
        choices=[4, 5, 6],
    )

    parameters = [faz, baz]


class DeeperModel(object):
    """The one where the non-nested parameter depends on the nested one"""

    class NestedModel(object):
        faz = Parameter(key="faz", type="Integer", choices=[1, 2, 3], default=1)
        baz = Parameter(key="baz", type="Integer", choices=[4, 5, 6], default=4)

        parameters = [faz, baz]

    foo = Parameter(
        key="foo",
        type="Integer",
        default=1,
        optional=False,
        choices="choices_cmd(param=${bar.faz})",
    )
    bar = Parameter(
        key="bar",
        type="Dictionary",
        default={},
        optional=False,
        parameters=[NestedModel],
    )

    parameters = [foo, bar]


class ShallowerModel(object):
    """The one where the nested parameter depends on the non-nested one"""

    class NestedModel(object):
        faz = Parameter(
            key="faz",
            type="Integer",
            default=1,
            optional=False,
            choices=[1, 2, 3],
        )
        baz = Parameter(
            key="baz",
            type="Integer",
            default=-1,
            optional=False,
            choices=None,  # choices will be set later
        )

        parameters = [faz, baz]

    foo = Parameter(
        key="foo",
        type="String",
        default=4,
        optional=False,
        choices=[4, 5, 6],
    )
    bar = Parameter(
        key="bar",
        type="Dictionary",
        default={},
        optional=False,
        parameters=[NestedModel],
        # parameters=_generate_nested_params(ChildModel),
    )

    # New and exciting
    # bar.parameters[0].baz.choices = _format_choices("choices_cmd(param=${foo})")

    bar.parameters[0].baz.choices = "choices_cmd(param=${foo})"

    # for param in bar.parameters:
    #     if param.key == "baz":
    #         param.choices = _format_choices("choices_cmd(param=${foo})")

    parameters = [foo, bar]


@system
class DynamicClient(object):
    """Plugin that repeats very specific stuff."""

    @command
    def choices_cmd(self, param):
        return [param]

    @parameter(key="the_model", model=SameLevelModel)
    def same_level(self, the_model):
        """Works in UI, request validation does not work"""
        pass

    @parameter(key="the_model", model=DeeperModel)
    def deeper(self, the_model):
        """Works in UI with brewtils grammar change, request validation does not work"""
        pass

    @parameter(key="the_model", model=ShallowerModel)
    def shallower(self, the_model):
        """Does not even come close to working"""
        pass


def main():
    plugin = Plugin(
        name="dynamic-model",
        version=__version__,
        description="Demonstrates interaction between dynamic choices and models",
    )
    plugin.client = DynamicClient()
    plugin.run()


if __name__ == "__main__":
    main()
