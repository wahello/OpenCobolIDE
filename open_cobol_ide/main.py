"""
This is the application entry. This is where we create and run the
Application.
"""
from .app import Application


def main():
    """
    Application entry point.
    """
    app = Application()
    ret_code = app.run()
    return ret_code
