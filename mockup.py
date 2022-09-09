import time
import tkinter as tk

def main():

    matches = ["Angela", "Pamela", "Samantha", "Amanda", "Tamara", "Dale", "Hank", "Bill", "Bobby", "Boomhauer"]

    window = tk.Tk()

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2,3], minsize=50)

    greeting = tk.Label(text="Mockup UI")

    #greeting.pack()
    greeting.grid(row=0,column=1)

    label1 = tk.Label(text="Enter Social Media Profile:")
    e = tk.Entry()


    label2 = tk.Label(text="Matches:")
    output = tk.Entry()

    def e_click():

        for i in range(0,10):
            output.insert(0,"  #" + str(i+1) + " match: " + matches[i])
        
        print("enter")
        return

    enter = tk.Button(
        text="Enter",
        command = e_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    label1.grid(row = 2, column = 0)
    e.grid(row=2,column=1)

    label2.grid(row = 2, column = 2)
    output.grid(row=2,column=3)

    enter.grid(row=3, column=1)

    window.mainloop()

    # usr = input("Enter Social Media Profile:")

    # print("Welcome " + usr + "! Finding you matches")
    # matches = ["Angela", "Pamela", "Samantha", "Amanda", "Tamara", "Dale", "Hank", "Bill", "Bobby", "Boomhauer"]
    # time.sleep(5)
    # print("Matches found!")
    # for i in range(0,10):
    #     print("#" + str(i+1) + " match: " + matches[i])
    # time.sleep(15)

if __name__ == "__main__": main()