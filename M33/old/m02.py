import sys
import Tkinter
import ttkcalendar
import tkSimpleDialog

class Calendar(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def __init__(self, master):
        self.Calendar = ttkcalendar.Calendar(master)
        self.Calendar.pack(expand=1, fill='both')
        #self.result = self.calendar.selection

    def apply(self):
        self.result = self.calendar.selection
        #x = ttkcal.selection

# Demo code:
def main():
    root = Tkinter.Tk()
    root.wm_title("CalendarDialog Demo")
    def onclick():
        cd = CalendarDialog(root)
        # print cd.result
        print cd.result
    button = Tkinter.Button(root, text="Click me to see a calendar!", command=onclick)
    button.pack()
    root.update()
    root.mainloop()

def test2():
    
    root = Tkinter.Tk()
    root.title('Ttk Calendar')
    ttkcal = Calendar(root)
    #ttkcal.pack(expand=1, fill='both')
    root.mainloop()

    x = ttkcal.selection    
    print 'x is: ', x  

if __name__ == "__main__":
    #main2()
    test2()