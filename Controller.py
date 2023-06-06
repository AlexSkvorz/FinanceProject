import sys
from PyQt5.QtWidgets import QApplication
from Model_Classes.FinanceDb import FinanceDb
from Model_Classes.Authorisation import AuthorisationWindow
from Model_Classes.Registration import RegistrationWindow
from Model_Classes.ForgotPassword import ForgotPasswordWindow
from Model_Classes.Finance import FinanceWindow
from Model_Classes.Edit import EditWindow
from Model_Classes.IncomesChart import IncomesWindow


class Controller:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.database = FinanceDb("finance.db")
        self.database.create_tables()
        self.authorisation_window = None
        self.registration_window = None
        self.forgot_password_window = None
        self.finance_window = None
        self.edit_dialog = None
        self.incomes_chart = None
        self.user_id = None
        self.info = None

        # Проверка через консоль юзеров
        self.database.check_tables()

    def run_authorisation_window(self):
        if not self.authorisation_window:
            self.authorisation_window = AuthorisationWindow(self.database)
            self.authorisation_window.show()
            self.authorisation_window.ui.registrationButton.clicked.connect(self.run_registration_window)
            self.authorisation_window.ui.forgotPasswordButton.clicked.connect(self.run_forgot_password_window)
            self.authorisation_window.auth_success.connect(self.on_authorisation_success)

    def run_registration_window(self):
        if not self.registration_window:
            self.registration_window = RegistrationWindow(self.database)
            self.registration_window.show()
        else:
            self.registration_window.show()
        self.registration_window.closed.connect(self.on_registration_window_closed)

    def run_forgot_password_window(self):
        if not self.forgot_password_window:
            self.forgot_password_window = ForgotPasswordWindow(self.database)
            self.forgot_password_window.show()
        else:
            self.forgot_password_window.show()
        self.forgot_password_window.closed.connect(self.on_forgot_password_window)

    def on_authorisation_success(self, user_id):
        self.user_id = user_id
        self.finance_window = FinanceWindow(self.database, user_id=self.user_id)
        self.finance_window.edit_success.connect(self.on_edit_dialog)
        self.finance_window.ui.openIncomesDiagrammButton.clicked.connect(lambda: self.run_incomes_chart(user_id, flag=True))
        self.finance_window.ui.openExpensesDiagrammButton.clicked.connect(lambda: self.run_incomes_chart(user_id, flag=False))
        self.finance_window.closed.connect(self.on_finance_window_closed)
        self.finance_window.show()
        self.authorisation_window.close()

    def run_incomes_chart(self, user_id, flag):
        self.incomes_chart = IncomesWindow(self.database, user_id, flag)
        self.incomes_chart.show()

    def on_edit_dialog(self, info):
        self.info = info
        self.edit_dialog = EditWindow(info=self.info)
        self.edit_dialog.show()
        self.edit_dialog.edit_right.connect(self.on_edit_right)

    def on_edit_right(self, complete_row):
        if self.finance_window.isVisible():
            self.finance_window.update_row(complete_row)

    def on_registration_window_closed(self):
        self.registration_window = None
        if not self.authorisation_window:
            self.switch_to_authorisation_window()
        if not self.registration_window:
            self.app.quit()

    def on_forgot_password_window(self):
        self.forgot_password_window = None
        if not self.authorisation_window:
            self.switch_to_authorisation_window()
        if not self.forgot_password_window:
            self.app.quit()

    def switch_to_authorisation_window(self):
        if self.registration_window:
            self.registration_window.hide()
        if self.authorisation_window:
            self.authorisation_window.show()

    def switch_to_registration_window(self):
        if self.authorisation_window:
            self.authorisation_window.hide()
        if self.registration_window:
            self.registration_window.show()

    def start(self):
        self.run_authorisation_window()
        sys.exit(self.app.exec())

    def on_finance_window_closed(self):
        self.app.quit()


if __name__ == "__main__":
    controller = Controller()
    controller.start()
