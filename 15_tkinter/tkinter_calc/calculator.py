import tkinter as tk


class Calculator(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.resizable(False, False)
        self.master.wm_title("Calculator")
        self.pack()
        self.var = tk.StringVar()
        self.create_screen()
        self.photos = list()
        self.create_buttons()
        self.current_var = None
        self.cache_var = None
        self.cache_operation = None

    def set_nums(self, num):
        if not self.current_var:
            self.current_var = num
            self.var.set(num)
        elif self.current_var == '-':
            num = f'-{num}'
            self.current_var = num
            self.var.set(num)
        else:
            num = f'{self.current_var}{num}'
            self.current_var = num
            self.var.set(num)

    def equal_operation(self):
        operations = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                      '*': lambda x, y: x * y, '/': lambda x, y: x / y}

        if all([self.cache_operation, self.cache_var, self.current_var]):
            cache_var = float(self.cache_var) if '.' in self.cache_var else int(self.cache_var)
            current_var = float(self.current_var) if '.' in self.current_var else int(self.current_var)
            f = operations[self.cache_operation]
            try:
                num = f(cache_var, current_var)
            except ZeroDivisionError:
                self.var.set('Error')
                self.cache_var = None
                self.current_var = None
                self.cache_operation = None
            else:
                if isinstance(num, float):
                    if all([i == '0' for i in str(num).split('.')[1]]):
                        num = int(num)
                self.var.set(str(round(num, 8)))
                self.cache_var = str(round(num, 8))
                self.current_var = None
                self.cache_operation = None
        else:
            self.var.set(self.cache_var)
            self.current_var = None

    def operation(self, operation):
        if all([self.cache_var, self.current_var]):
            self.cache_operation = operation
        elif self.current_var:
            self.cache_var = self.current_var
            self.current_var = None
            self.cache_operation = operation
        elif self.cache_var:
            self.cache_operation = operation

    def set_symbol(self):
        if not self.current_var and not self.cache_var:
            symbol = self.var.get()[0]
            if symbol != '-':
                self.var.set('-0')
                self.current_var = '-'
            else:
                self.var.set('0')
                self.current_var = None
        elif self.current_var:
            symbol = self.var.get()[0]
            if symbol != '-':
                self.var.set(f'-{self.var.get()}')
                self.current_var = f'-{self.current_var}'
            else:
                self.var.set(self.var.get()[1:])
                self.current_var = self.current_var[1:]
        elif self.cache_var:
            symbol = self.var.get()[0]
            if symbol != '-':
                self.var.set(f'-{self.var.get()}')
                self.cache_var = f'-{self.cache_var}'
            else:
                self.var.set(self.var.get()[1:])
                self.cache_var = self.cache_var[1:]

    def get_percent(self):
        if self.current_var == '-':
            pass
        elif self.current_var:
            variable = float(self.current_var) if '.' in self.current_var else int(self.current_var)
            answer = str(round(variable / 100, 8))
            answer = answer if 'e' not in answer else self.current_var
            self.current_var = answer
            self.var.set(answer)
        elif self.cache_var:
            variable = float(self.cache_var) if '.' in self.cache_var else int(self.cache_var)
            answer = str(round(variable / 100, 8))
            answer = answer if 'e' not in answer else self.cache_var
            self.cache_var = answer
            self.var.set(answer)

    def delete_var(self):
        if self.current_var:
            self.current_var = None
            self.var.set('0')
        elif self.cache_var:
            self.cache_var = None
            self.var.set('0')

    def create_screen(self):
        top_frame = tk.Frame(self, bd=10)
        top_frame.pack(side='top')

        screen = tk.Label(top_frame, textvariable=self.var, anchor='e', font=("Courier", 30), width=10, height=1)
        self.var.set(0)
        screen.pack()

    def create_buttons(self):
        funcs_dict = {0: lambda: self.delete_var(), 1: lambda: self.set_symbol(),
                      2: lambda: self.get_percent(), 3: lambda: self.operation('/'),
                      4: lambda: self.set_nums('7'), 5: lambda: self.set_nums('8'),
                      6: lambda: self.set_nums('9'), 7: lambda: self.operation('*'),
                      8: lambda: self.set_nums('4'), 9: lambda: self.set_nums('5'),
                      10: lambda: self.set_nums('6'), 11: lambda: self.operation('-'),
                      12: lambda: self.set_nums('1'), 13: lambda: self.set_nums('2'),
                      14: lambda: self.set_nums('3'), 15: lambda: self.operation('+'),
                      16: lambda: self.set_nums('0'), 17: lambda: 'pass',
                      18: lambda: self.set_nums('.'), 19: lambda: self.equal_operation()}

        bottom_frame = tk.Frame(self)
        bottom_frame.pack(side='bottom')
        self.photos = [tk.PhotoImage(file=f'calc_images/image{i}.png') for i in range(1, 21)]
        count = 0
        for r in range(5):
            for c in range(4):
                tk.Button(bottom_frame, image=self.photos[count],
                          command=funcs_dict[count]).grid(row=r, column=c)
                count += 1


root = tk.Tk()
app = Calculator(root)

root.mainloop()
