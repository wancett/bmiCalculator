import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=210)
boslukLabel = tkinter.Label(text="")
boslukLabel.pack()

boslukLabel1 = tkinter.Label(text="")
boslukLabel2 = tkinter.Label(text="")

#weight
weightLabel = tkinter.Label(text="Enter Your Weight (kg)")
weightLabel.pack()

def getentryWeight ():
    height = heightEntry.get()
    weight = weightEntry.get()

    if weight == "" or height == "":
        resultLabel.config(text="Enter Weight and Height !!")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            resultString = writeResult(bmi)
            resultLabel.config(text=resultString)
        except:
            resultLabel.config(text="Enter a valid Number")

weightEntry = tkinter.Entry(width=20)
weightEntry.pack()

#bosluk label

boslukLabel2.pack()

#height

heightLabel = tkinter.Label(text="Enter Your Height (cm)")
heightLabel.pack()


heightEntry = tkinter.Entry(width=20)
heightEntry.pack()


boslukLabel1.pack()

Button = tkinter.Button(text="Calculate",command=getentryWeight)
Button.pack()

resultLabel = tkinter.Label()
resultLabel.pack()

def writeResult (bmi):
    resultString = f"Your BMI is : {round(bmi, 2)}. You are "
    if bmi <= 16:
        resultString += "severely thin !"
    elif 16 < bmi <= 17:
        resultString += "moderately thin"
    elif 17 < bmi <= 17-18.5:
        resultString += "mild thin"
    elif 18.5 < bmi <= 25:
        resultString += "normal"
    elif 25 < bmi <= 30:
        resultString += "overweight"
    elif 30 < bmi <= 35:
        resultString += "obese class 1 !"
    elif 35 < bmi <= 40:
        resultString += "obese class 2 !!"
    else:
        resultString += "obese class 3 !!!"

    return resultString

window.mainloop()
