import sys
import pyautogui
import os
from img2pdf import convert
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt


x,y = pyautogui.position()
print(x,y)

pos = [(0,0),(0,0)]

firstPosKey = [Qt.Key_F1, Qt.Key_Z]
lstPosKey = [Qt.Key_F2, Qt.Key_X]


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("untitled.ui")[0]



#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.convertStart_btn.clicked.connect(self.convertStart)

    def convertStart(self):
        print("convertStart")
        print(pos)
    
        left_top_x = pos[0][0]
        left_top_y = pos[0][1]
        right_bottom_x = pos[1][0]
        right_bottom_y = pos[1][1]
        distance_x = right_bottom_x - left_top_x
        distance_y = right_bottom_y - left_top_y

        

        print()
        src_dir = os.getcwd() + "\\dist"            
        if not os.path.exists(src_dir):
            os.makedirs(src_dir)
        
        total_pages = self.totalPage.text()
        
        for i in range(int(total_pages)):
            pyautogui.screenshot(region=(left_top_x, left_top_y, distance_x, distance_y)).save(src_dir + f"\\{i}.png")



        # src_dir = os.getcwd() + "\\dist"
        # tgt_dir = os.getcwd()

        # img_files = [os.path.join(src_dir, nm) for nm in os.listdir(src_dir)]
        # with open(tgt_dir + "\\test.pdf", "wb") as pdf_file:
        #     pdf_file.write(convert(img_files))

    
    

        

    def keyPressEvent(self, e):
        x,y = pyautogui.position()
        if e.key() in firstPosKey:
            print("firstPosKey")

            self.firstPos_label.setText(f'({x},{y})')
            pos[0] = (x,y)

            
            
        elif e.key() in lstPosKey:
            print("lstPosKey")

            self.lstPos_label.setText(f'({x},{y})')
            pos[1] = (x,y)


            

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()