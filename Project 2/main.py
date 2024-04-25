from PyQt6.QtWidgets import *
from gui import *
from logic import *
        
def main() -> None:
    """
    Function to run app.
    """
    app = QApplication([])
    controller = Controller()
    controller.show()
    app.exec()

if __name__ == '__main__': 
    main()