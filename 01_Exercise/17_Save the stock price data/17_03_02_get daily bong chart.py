import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

TR_REQ_TIME_INTERVAL = 0.2   # 이전 예제 코드에서 추가 :

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    def _create_kiwoom_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def _set_signal_slots(self):
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data) # 이전 예제 코드에서 추가 : tr data 받는

    def comm_connect(self):
        self.dynamicCall("CommConnect()")
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code == 0:
            print("connected")
        else:
            print("disconnected")

        self.login_event_loop.exit()

    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall("GetCodeListByMarket(QString)", market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        code_name = self.dynamicCall("GetMasterCodeName(QString)", code)
        return code_name


if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    print(kiwoom.get_master_code_name("000660"))
    code_list = kiwoom.get_code_list_by_market('10')
    for code in code_list:
        print(code, end=" ")


