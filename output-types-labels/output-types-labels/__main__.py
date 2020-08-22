import sys

from brewtils import command, get_connection_info, system, Plugin, SystemClient

__version__ = "1.0.0.dev0"


@system
class OutputTypesLabelsClient:
    """ Simple Single Output Tests """

    @command(
        description="Expected single result of default type STRING with default label"
    )
    def nothing_defined(self):
        return "result"

    @command(
        output_type="JSON",
        description="Expected single result of type JSON with default label",
    )
    def single_output_type(self):
        return {"output": "result"}

    @command(
        output_types=["JSON"],
        description="Expected single result of type JSON with default label",
    )
    def single_output_types(self):
        return {"output": "result"}

    @command(
        output_labels=["Results"],
        description="Expected single result of Labeled Results with default type STRING",
    )
    def single_output_labels(self):
        return {"output": "result"}

    @command(
        output_type="JSON",
        output_labels=["Results"],
        description="Expected single result of Labeled Results of type JSON",
    )
    def single_output_label_and_type(self):
        return {"output": "result"}

    """ Simple Multi Output Tests """

    @command(
        output_types=["JSON", "JSON"],
        description="Expected two results of type JSON with default labels",
    )
    def multi_output_types(self):
        return {"output": "result"}, {"output": "result"}

    @command(
        output_labels=["Result1", "Result2"],
        description="Expected two results of default type STRING with labels",
    )
    def multi_output_lables(self):
        return {"output": "result"}, {"output": "result"}

    @command(
        output_types=["JSON", "JSON"],
        output_labels=["Result1", "Result2"],
        description="Expected two results of JSON type with labels",
    )
    def multi_output_labels_and_types(self):
        return {"output": "result"}, {"output": "result"}

    """ Mixed Testing"""

    @command(
        output_type="JSON",
        output_labels=["Result1", "Result2"],
        description="Expected first results of JSON and second of default type STRING with labels",
    )
    def single_output_type_and_multi_labels(self):
        return {"output": "result"}, {"output": "result"}

    @command(
        output_types=["JSON", "JSON"],
        output_labels=["Result1"],
        description="Expected two results of JSON type with first label populated and second label default",
    )
    def multi_output_type_and_single_labels(self):
        return {"output": "result"}, {"output": "result"}

    """ Missing Ouput Testing """

    @command(
        output_types=["JSON", "JSON"],
        output_labels=["Result1", "Result2"],
        description="Expected one results of JSON type with label, second output should be blank",
    )
    def multi_output_labels_and_types_missing_results(self):
        return {"output": "result"}

    """ Additional Results Test"""

    @command(
        output_types=["JSON", "JSON"],
        output_labels=["Result1", "Result2"],
        description="Expected two results of JSON type with labels, third output should be default type String "
        "and default Label",
    )
    def multi_output_labels_and_types_extra_results(self):
        return {"output": "result"}, {"output": "result"}, {"output": "result"}

    """ Single Output List Testing """

    @command(
        output_type="JSON",
        description="Expected single result of type JSON with default label",
    )
    def single_output_type_multi_results(self):
        return {"output": "result"}, {"output": "result"}

    @command(
        output_types=["JSON"],
        description="Expected single result of type JSON with default label",
    )
    def single_output_types_multi_results(self):
        return {"output": "result"}, {"output": "result"}

    @command(
        description="Expected single result of default type STRING with default label"
    )
    def nothing_defined_list(self):
        return {"output": "result"}, {"output": "result"}

    """ Weird Edge Case """

    @command(
        output_types=["JSON", "JSON"],
        output_labels=["Result1", "Result2"],
        description="NExpected one results of JSON type with label, second output should be blank",
    )
    def multi_output_labels_and_types_single_dict(self):
        return {"output": "result", "output2": "result2"}


def main():
    connection_params = get_connection_info(sys.argv[1:])
    Plugin(
        OutputTypesLabelsClient(),
        name="output-types-labels",
        version=__version__,
        **connection_params
    ).run()


if __name__ == "__main__":
    main()
