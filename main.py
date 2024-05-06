from logic import *


def main() -> None:
    """
    Creates the main application instance, sets up the voting window, and starts the event loop.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
