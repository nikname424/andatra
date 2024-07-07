from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QStandardItemModel, QStandardItem
from db import Database
from tables_ui import Ui_Tables
from add_worker_ui import Ui_Add_Worker
from delete_worker_ui import Ui_Delete_Worker
from not_permission_ui import Ui_NotPermisson
from change_worker_ui import Ui_ChangeWorker
import subprocess
import sys

db = Database('DataAnd.db')

class AddWorkerForm(QMainWindow):
    def __init__(self):
        super(AddWorkerForm, self).__init__()
        self.ui = Ui_Add_Worker()
        self.ui.setupUi(self)

        self.connectionButtons()
    
    def connectionButtons(self):
        self.ui.add_btn.clicked.connect(lambda: self.write_data())        

    def write_data(self):
        def is_number(num):
            try:
                float(num)
                return True
            except:
                return False
        username = self.ui.name_input.text()
        surname = self.ui.surname_input.text()
        job_title = self.ui.job_title_input.text()
        salary = self.ui.salary_input.text()
        pasport = self.ui.pasport_input.text()
        try:
            db.add_worker(username, surname, job_title, float(salary), pasport) if username != '' and surname != '' and job_title != '' and salary != '' and is_number(salary) and pasport !='' else None
            
        except:
            pass

        finally:
            self.ui.name_input.clear()
            self.ui.surname_input.clear()
            self.ui.job_title_input.clear()
            self.ui.salary_input.clear()
            self.ui.pasport_input.clear()

class ChangeWorkerForm(QMainWindow):
    def __init__(self):
        super(ChangeWorkerForm, self).__init__()
        self.ui = Ui_ChangeWorker()
        self.ui.setupUi(self)

        self.initialization()
        self.connectionButtons()

    def initialization(self):
        id_workers = db.get_all_elements('workers', 'id')
        print(id_workers)

        for item in id_workers:
            self.ui.comboBox.addItem(str(item))

        self.show_data()

    def connectionButtons(self):
        self.ui.pushButton.clicked.connect(lambda: self.save_data())
        self.ui.comboBox.currentIndexChanged.connect(lambda: self.show_data())
    
    def show_data(self):
        id_user = self.ui.comboBox.currentText()
 
        self.ui.lineEdit.setText(str(db.get_element_worker_id(id_user, 'username')))
        self.ui.lineEdit_2.setText(str(db.get_element_worker_id(id_user, 'subname')))
        self.ui.lineEdit_3.setText(str(db.get_element_worker_id(id_user, 'job_title')))
        self.ui.lineEdit_4.setText(str(db.get_element_worker_id(id_user, 'salary')))
        self.ui.lineEdit_5.setText(str(db.get_element_worker_id(id_user, 'pasport')))
        self.ui.lineEdit_6.setText(str(db.get_element_worker_id(id_user, 'secret_key')))
        self.ui.lineEdit_7.setText(str(db.get_element_worker_id(id_user, 'user_id')))

    def save_data(self):
        name = self.ui.lineEdit.text()
        surname = self.ui.lineEdit_2.text()
        job_title = self.ui.lineEdit_3.text()
        salary = self.ui.lineEdit_4.text()
        pasport = self.ui.lineEdit_5.text()
        secret_key = self.ui.lineEdit_6.text()
        user_id = self.ui.lineEdit_7.text()

        id = self.ui.comboBox.currentText()

        db.update_worker(id, name, surname, job_title, salary, pasport, secret_key, user_id)

class TableWindow(QMainWindow):
    def __init__(self):
        super(TableWindow, self).__init__()
        self.ui = Ui_Tables()
        self.ui.setupUi(self)

        self.initialization()
        self.connectionButtons()

    def initialization(self):
        self.view_data('cards', self.ui.tableView_2)
        self.view_data('crypto', self.ui.tableView_3)
        self.view_data('investors', self.ui.tableView)
        self.view_data('workers', self.ui.tableView_4)   

    def connectionButtons(self):
        self.ui.pushButton.clicked.connect(lambda: AddWorkerForm().show()) if db.get_role() == 'ROLE_OWNER' else self.ui.pushButton.clicked.connect(lambda: NotPermission().show())
        self.ui.pushButton_2.clicked.connect(lambda: subprocess.Popen(["py", "delete_data_worker.py"])) if db.get_role() == 'ROLE_OWNER' else self.ui.pushButton_2.clicked.connect(lambda: NotPermission().show())
        self.ui.pushButton_3.clicked.connect(lambda: ChangeWorkerForm().show()) if db.get_role() == 'ROLE_OWNER' else self.ui.pushButton_3.clicked.connect(lambda: NotPermission().show())
        
    def view_data(self, table_name, element):
        data, headers = db.get_table(table_name)
        model = QStandardItemModel(0, len(headers), self)
        model.setHorizontalHeaderLabels(headers)

        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        element.setModel(model)

class NotPermission(QMainWindow):
    def __init__(self):
        super(NotPermission, self).__init__()
        self.ui = Ui_NotPermisson()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(lambda: self.close())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TableWindow()
    
    window.show()

    sys.exit(app.exec())
