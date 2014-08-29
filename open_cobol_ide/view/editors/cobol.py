"""
Contains the cobol code editor widget.

"""
from pyqode.cobol.widgets import CobolCodeEdit as CodeEditBase

from ...compiler import get_file_type
from  ...linter import CobolLinterMode
from ...settings import Settings


class CobolCodeEdit(CodeEditBase):
    """
    Cobol code editor. We specialise the pyqode.cobol code edit to add support
    for our settings system and for some custom properties (such as the
    file type).

    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.linter_mode = self.modes.append(CobolLinterMode())

    @property
    def file_type(self):
        return get_file_type(self.file.path)

    @file_type.setter
    def file_type(self, ftype):
        Settings().set_file_type(self.file.path, ftype)
