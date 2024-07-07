from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem
from delete_worker_ui import Ui_Delete_Worker
from db import Database
import sys

db = Database('DataAnd.db')

class DeleteWorkerForm(QMainWindow):
    def __init__(self):
        super(DeleteWorkerForm, self).__init__()
        self.ui = Ui_Delete_Worker()
        self.ui.setupUi(self)

        self.connectionButtons()
        self.initialization()

    def connectionButtons(self):
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.show_data())
        self.ui.pushButton.clicked.connect(lambda: self.delete_data())

    def initialization(self):
        id_workers = db.get_all_elements('workers', 'id')
        print(id_workers)

        for item in id_workers:
            self.ui.comboBox.addItem(str(item))

    def show_data(self):
        id_user = self.ui.comboBox.currentText()
 
        self.ui.label.setText(str(db.get_element_worker_id(id_user, 'username')))
        self.ui.label_2.setText(str(db.get_element_worker_id(id_user, 'subname')))
        self.ui.label_3.setText(str(db.get_element_worker_id(id_user, 'job_title')))
        self.ui.label_4.setText(str(db.get_element_worker_id(id_user, 'salary')))
        self.ui.label_5.setText(str(db.get_element_worker_id(id_user, 'pasport')))

    def delete_data(self):
        db.delete_worker_id(self.ui.comboBox.currentText())
        self.ui.comboBox.clear()
        self.initialization()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DeleteWorkerForm()
    
    window.show()

    sys.exit(app.exec())