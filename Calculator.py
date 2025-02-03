import tkinter as calculator
import math
calculation = ""
history = []

def add_to_calcualtion(symbol):
    global calculation
    calculation = calculation + str(symbol)
    resault_text.delete(1.0 , "end")
    resault_text.insert(1.0, calculation)

def evaluate_calculation():
    global calculation , history
    try:
        result = str(eval(calculation))
        history.append(calculation + " = " + result + "\n")
        calculation = result
        resault_text.delete(1.0, "end")
        resault_text.insert(1.0, calculation)
    except:
        clear_field()
        resault_text.insert(1.0,"ERROR")

def clear_field():
    global calculation
    calculation = ""
    resault_text.delete(1.0 , "end")

def delete_last_character():
    global calculation
    calculation = calculation[:-1]
    resault_text.delete(1.0, "end")
    resault_text.insert(1.0, calculation)


def open_scientific_mode():
    scientific_window = calculator.Toplevel(frame)
    scientific_window.title("Scientific Mode")



    

frame = calculator.Tk()
frame.geometry("400x300")

resault_text = calculator.Text(frame,height=2 , width=24 , font=("Arial",24))
resault_text.grid(columnspan=7)


btn1 = calculator.Button(frame , text="1" , command=lambda: add_to_calcualtion(1) , width=5,font=("Arial" , 14) )
btn1.grid(row=2 , column=1)
btn2 = calculator.Button(frame , text="2" , command=lambda: add_to_calcualtion(2) , width=5,font=("Arial" , 14) )
btn2.grid(row=2 , column=2)
btn3 = calculator.Button(frame , text="3" , command=lambda: add_to_calcualtion(3) , width=5,font=("Arial" , 14) )
btn3.grid(row=2 , column=3)
btn4 = calculator.Button(frame , text="4" , command=lambda: add_to_calcualtion(4) , width=5,font=("Arial" , 14) )
btn4.grid(row=3 , column=1)
btn5 = calculator.Button(frame , text="5" , command=lambda: add_to_calcualtion(5) , width=5,font=("Arial" , 14) )
btn5.grid(row=3 , column=2)
btn6 = calculator.Button(frame , text="6" , command=lambda: add_to_calcualtion(6) , width=5,font=("Arial" , 14) )
btn6.grid(row=3 , column=3)
btn7 = calculator.Button(frame , text="7" , command=lambda: add_to_calcualtion(7) , width=5,font=("Arial" , 14) )
btn7.grid(row=4 , column=1)
btn8 = calculator.Button(frame , text="8" , command=lambda: add_to_calcualtion(8) , width=5,font=("Arial" , 14) )
btn8.grid(row=4 , column=2)
btn9 = calculator.Button(frame , text="9" , command=lambda: add_to_calcualtion(9) , width=5,font=("Arial" , 14) )
btn9.grid(row=4 , column=3)
btn0 = calculator.Button(frame , text="0" , command=lambda: add_to_calcualtion(0) , width=5,font=("Arial" , 14) )
btn0.grid(row=5 , column=2)
btn_open = calculator.Button(frame , text="(" , command=lambda: add_to_calcualtion("(") , width=5,font=("Arial" , 14) )
btn_open.grid(row=5 , column=1)
btn_close = calculator.Button(frame , text=")" , command=lambda: add_to_calcualtion(")") , width=5,font=("Arial" , 14) )
btn_close.grid(row=5 , column=3)
btn_division = calculator.Button(frame , text="÷" , command=lambda: add_to_calcualtion("/") , width=5,font=("Arial" , 14) )
btn_division.grid(row=2 , column=4)
btn_multiplication = calculator.Button(frame , text="×" , command=lambda: add_to_calcualtion("*") , width=5,font=("Arial" , 14) )
btn_multiplication.grid(row=3 , column=4)
btn_minus = calculator.Button(frame , text="-" , command=lambda: add_to_calcualtion("-") , width=5,font=("Arial" , 14) )
btn_minus.grid(row=4 , column=4)
btn_plus = calculator.Button(frame , text="+" , command=lambda: add_to_calcualtion("+") , width=5,font=("Arial" , 14) )
btn_plus.grid(row=5 , column=4)
btn_resault = calculator.Button(frame, text=" = ", command=evaluate_calculation, width=6, font=("Arial", 14 ),fg="red")
btn_resault.grid(row=6 , column=1)
btn_clear = calculator.Button(frame, text="C", command=clear_field, width=6, font=("Arial", 14),fg="blue")
btn_clear.grid(row=6 , column=3)
btn_delete = calculator.Button(frame, text="Del", command=delete_last_character, width=6, font=("Arial", 14), fg="green")
btn_delete.grid(row=6, column=2)




def open_scientific_mode():
    scientific_window = calculator.Toplevel(frame)
    scientific_window.title("Scientific Mode")
    
    btn_sin = calculator.Button(scientific_window, text="sin", command=lambda: add_to_calcualtion("math.sin("), width=5, font=("Arial", 14))
    btn_sin.grid(row=0, column=0)
    btn_cos = calculator.Button(scientific_window, text="cos", command=lambda: add_to_calcualtion("math.cos("), width=5, font=("Arial", 14))
    btn_cos.grid(row=0, column=1)
    btn_tan = calculator.Button(scientific_window, text="tan", command=lambda: add_to_calcualtion("math.tan("), width=5, font=("Arial", 14))
    btn_tan.grid(row=0, column=2)
    btn_log = calculator.Button(scientific_window, text="log", command=lambda: add_to_calcualtion("math.log("), width=5, font=("Arial", 14))
    btn_log.grid(row=0, column=3)
    btn_square = calculator.Button(scientific_window , text="x²" , command=lambda: add_to_calcualtion("**") , width=5,font=("Arial" , 14) )
    btn_square.grid(row=1 , column=0)
    btn_square_root = calculator.Button(scientific_window , text="√" , command=lambda: add_to_calcualtion("math.sqrt(") , width=5,font=("Arial" , 14) )
    btn_square_root.grid(row=1 , column=1)
    btn_pi = calculator.Button(scientific_window , text="π" , command=lambda: add_to_calcualtion("math.pi(") , width=5,font=("Arial" , 14) )
    btn_pi.grid(row=1 , column=2)
    btn_inverse = calculator.Button(scientific_window , text="1/x" , command=lambda: add_to_calcualtion("1/") , width=5,font=("Arial" , 14) )
    btn_inverse.grid(row=1 , column=3)

    
def show_history():
    history_window = calculator.Toplevel(frame)
    history_window.title("Calculation History")

    history_text = calculator.Text(history_window, height=20, width=30, font=("Arial", 12))
    history_text.pack()

    for item in history:
        history_text.insert("end", item + "")


menu_bar = calculator.Menu(frame)
frame.config(menu=menu_bar)

mode_menu = calculator.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Mode", menu=mode_menu)
mode_menu.add_command(label="Scientific Mode", command=open_scientific_mode)
mode_menu.add_command(label="History", command=show_history)

frame.mainloop()


