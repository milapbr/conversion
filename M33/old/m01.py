import Tkinter
import ttkcalendar

import tkSimpleDialog

class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""
    def __init__(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()
        #self.result = self.calendar.selection

    def apply(self):
        self.result = self.calendar.selection

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
    import sys
    root = Tkinter.Tk()
    root.title('Ttk Calendar')
    ttkcal = Calendar(firstweekday=calendar.SUNDAY)
    ttkcal.pack(expand=1, fill='both')

    if 'win' not in sys.platform:
        style = ttk.Style()
        style.theme_use('clam')

    root.mainloop()

    x = ttkcal.selection    
    print 'x is: ', x  
def main2():
    i=-40
    root = Tkinter.Tk()
    root.wm_title("CalendarDialog Demo")
    cd = CalendarDialog(root)
    #button.pack()
    root.update()
    print cd.result
    i=+1
    print i

    root.mainloop()
if __name__ == "__main__":
    #main2()
    test2()