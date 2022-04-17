"""
Sample training file for tkgui
"""
from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, columnspan=3, padx=10, pady=10)
f_num = 0
operation = ""


def enter_number(number: int) -> None:
    """
    Gets the current number from the user input and adds it to the rest of the
    numbers entered by the user

    parameters: number as int

    return: None
    """

    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear_button() -> None:
    """
    Deletes all of the numbers in the readout

    parameters: None

    return: None
    """
    e.delete(0, END)


def operation_button(op_type: str) -> None:
    """
    determines what operation will be used

    parameters: op_type as str

    return: None
    """

    global f_num
    global operation
    first_number = float(e.get())
    f_num = first_number
    e.delete(0, END)
    operation = op_type


def equal_button() -> None:
    """
    Performs the operations on the numbers entered by the user

    parameters: None

    return: None
    """

    if e.get() == "":
        e.insert(0, "You must choose an operation type")
    else:
        second_number = float(e.get())
        e.delete(0, END)
        if operation == "add":
            e.insert(0, f_num + second_number)
        elif operation == "subtract":
            e.insert(0, f_num - second_number)
        elif operation == "multiply":
            e.insert(0, f_num * second_number)
        elif operation == "divide":
            if second_number == 0:
                e.insert(0, "You cannot divide by 0")
            else:
                e.insert(0, f_num / second_number)


# define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: enter_number(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: enter_number(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: enter_number(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: enter_number(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: enter_number(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: enter_number(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: enter_number(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: enter_number(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: enter_number(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: enter_number(0))
button_decimal = Button(
    root, text=".", padx=41, pady=20, command=lambda: enter_number(".")
)
button_add = Button(
    root, text="+", padx=39, pady=20, command=lambda: operation_button("add")
)
button_equal = Button(root, text="=", padx=90, pady=20, command=equal_button)
button_clear = Button(root, text="C", padx=39, pady=20, command=clear_button)
button_minus = Button(
    root, text="-", padx=41, pady=20, command=lambda: operation_button("subtract")
)
button_multiply = Button(
    root, text="*", padx=40, pady=20, command=lambda: operation_button("multiply")
)
button_divide = Button(
    root, text="/", padx=40, pady=20, command=lambda: operation_button("divide")
)

# put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_decimal.grid(row=4, column=2)

button_minus.grid(row=5, column=0)
button_multiply.grid(row=5, column=1)
button_divide.grid(row=5, column=2)

button_clear.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()
