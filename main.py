from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(300, 100)
window.config(padx = 10, pady = 30)

weight_label = Label(text = "Enter Your Weight (kg)")
weight_label.pack()
weight_entry = Entry()
weight_entry.pack()

height_label = Label(text = "Enter Your Height (cm)")
height_entry = Entry()
height_label.pack()
height_entry.pack()


def button_calculated():
    weightget = weight_entry.get()
    heightget = height_entry.get()

    if not weightget or not heightget:
        result_label.config(text = "Enter both weight and height!")
        return

    try:
        weightget = int(weight_entry.get())
        heightget = int(height_entry.get())
        bmi = weightget / (heightget / 100) ** 2

        if bmi <= 18.4:
            result_label.config(text = "Underweight")


        elif 18.5 <= bmi <= 24.9:
            result_label.config(text = "Normal weight")

        elif 25.0 <= bmi <= 39.9:
            result_label.config(text = "Overweight")


        else:
            result_label.config(text = "Obese")

    except ValueError:
            result_label.config(text = "Please enter valid numbers!")


calculate_button = Button(text = "Calculate", command = button_calculated)
calculate_button.pack()

result_label = Label()
result_label.pack()




mainloop()