import tkinter 

def calculating(): 
    height = float(hentry.get())
    weight= float(wentry.get())
    bmi= weight/height**2
    result.config(text= f"BMI = {bmi}")
    
    if bmi <= 18.24:
        result.config(text="Underweight")
    elif bmi >= 18.5:
        result.config(text= "Normal")
    elif bmi >= 24.99:
        result.config(text= "Pre-obesity")
    elif bmi == 25:
        result.config(text="Overweight")
    elif bmi== 30:
        result.config(text="Obesity")
    
    
    
    
root = tkinter.Tk()
root.geometry("400x400")
root.title("BMI CALCULATOR")

instructions_label = tkinter.Label(root, text="Enter your height in meters:")
instructions_label.pack(pady=10)
hentry = tkinter.Entry(root)
hentry.pack(pady=10)
instructions_label = tkinter.Label(root, text="Enter your weight in kilograms:")
instructions_label.pack(pady=10)

wentry = tkinter.Entry(root)
wentry.pack(pady=10)

button = tkinter.Button(root,text="Calculate BMI", command=calculating)
button.pack(pady=10)

result= tkinter.Label(root, text="")
result.pack(pady=10)

root.mainloop()