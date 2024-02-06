class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self): # calculate 메서드 추가
        num1 = float(self.view.le1.text()) # 첫 번째 라인 에디트에 입력된 숫자를 읽어옴
        num2 = float(self.view.le2.text()) # 두 번째 라인 에디트에 입력된 숫자를 읽어옴
        operator = self.view.cb.currentText()

        if operator == '+': # 연산자가 '+' 이면 덧셈 결과를 문자열로 리턴
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        else:
            return "Calculation Error"

    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)
    
    def sum(self, a, b): # 예외 처리 기능 추가
        return str(a + b)
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        try:
            if(b==0):
                raise Exception("Divisor Error")
        except Exception as e:
            return e
        return a/b
    
    def pow(self, a, b):
        if (a==0):
            return 0
        else:
            return pow(a, b)