import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtCore import Qt, QTimer

class RotatingSquare(QGraphicsRectItem):
    def __init__(self):
        super(RotatingSquare, self).__init__(0, 0, 100, 100)
        self.setBrush(Qt.red)
        self.setTransformOriginPoint(50, 50)
        self.setRotation(0)

    def rotate(self):
        current_rotation = self.rotation()
        self.setRotation(current_rotation + 1)

class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.square = RotatingSquare()
        self.scene.addItem(self.square)

        self.square.setPos(50, 150)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.square.rotate)
        self.timer.start(30)

    def rotate_square(self):
        self.timer.start(30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())