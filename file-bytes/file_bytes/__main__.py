import gzip
import hashlib

from brewtils import Plugin, parameter, system

__version__ = "1.0.0.dev0"


@system
class FileBytesClient(object):
    """Plugin that tests file upload as bytes parameter"""

    @parameter(key="text_file", type="Bytes")
    def echo_plaintext(self, text_file):
        """Returns the contents of a plaintext file"""
        return text_file.decode()

    @parameter(key="text_file1", type="Bytes")
    @parameter(key="text_file2", type="Bytes")
    def echo_plaintext_multiple(self, text_file1, text_file2):
        """Returns the contents of two provided plaintext files"""
        return f"text_file1:\n{text_file1.decode()}\n\nsecond:\n{text_file2.decode()}"

    @parameter(key="gzipped_text_file", type="Bytes")
    def echo_gzipped(self, gzipped_text_file):
        """Returns the uncompressed contents of a gzipped plaintext file"""
        return gzip.decompress(gzipped_text_file).decode()

    @parameter(key="some_file", type="Bytes")
    def echo_md5sum(self, some_file):
        """Returns the md5sum of a provided file"""
        return hashlib.md5(some_file).hexdigest()

    def echo_md5sum_optional(self, file_upload):
        """Returns the md5sum of a provided file"""
        if file_upload:
            return hashlib.md5(file_upload).hexdigest()
        else:
            return "no file selected"


def main():
    p = Plugin(name="file-bytes", version=__version__)
    p.client = FileBytesClient()
    p.run()


if __name__ == "__main__":
    main()
