from dataclasses import dataclass, field
from pathlib import Path

from lxml import etree as ET

from imxInsights.utils.helpers import hash_sha256


@dataclass(frozen=True)
class XmlFile:
    """
    Represents an XML file, providing methods for parsing and checking its existence.

    This class allows you to work with XML files by providing a convenient interface for
    parsing and checking the existence of an XML file. It can be used to load and parse
    an XML file, and to determine whether the file exists.

    Args:
        path (Path): The path to the XML file.
        root (ET.ElementTree, optional): An optional pre-parsed XML root element. Default is None.

    Attributes:
        path (Path): The path to the XML file.
        root (ET.ElementTree): The parsed XML root element. It is set to None initially and
            will be parsed when necessary using the `ET.parse` method.

    Raises:
        ValueError: If the provided `path` does not exist or is not a file.

    Note:
        When parsing XML files, this class uses an XMLParser with comments removed to ensure
        that comments are not parsed as nodes. However, please note that comments will be lost
        when implement saving the XML file.

    """

    path: Path
    root: ET.ElementTree = field(kw_only=True, hash=False, repr=False, default=None)
    file_hash: str = field(init=False, hash=False, default=None)
    tag: str = field(init=False, hash=False, default=None)

    def __post_init__(self) -> None:
        if self.root is not None:
            return

        if not self.exists:
            raise ValueError(f"Invalid path {self.path}")

        object.__setattr__(self, "file_hash", hash_sha256(self.path))

        parser = ET.XMLParser(remove_comments=True)
        root = ET.parse(self.path, parser)
        object.__setattr__(self, "tag", root.getroot().tag)

        super().__setattr__("root", root)

    @property
    def exists(self) -> bool:
        return self.path.exists() and self.path.is_file()
