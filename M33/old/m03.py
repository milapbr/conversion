import sys
import Tkinter
import ttkcalendar
import tkSimpleDialog

class Calendar2(Calendar):
    def __init__(self, master=None, call_on_select=None, **kw):
        Calendar.__init__(self, master, **kw)
        self.set_selection_callbeck(call_on_select)

    def set_selection_callbeck(self, a_fun):
         self.call_on_select = a_fun

    def _pressed(self, evt):
        Calendar._pressed(self, evt)
        x = self.selection
        #print(x)
        if self.call_on_select:
            self.call_on_select(x)

class SecondFrame(Tkinter.Frame):

    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)
        self.l = Tkinter.Label(self, text="Selected date")
        self.l.pack()
        self.pack()

    def update_lable(self, x):
        self.l['text'] = x;

def test2():
    import sys
    root = Tkinter.Tk()
    root.title('Ttk Calendar')


    ttkcal = Calendar2(firstweekday=calendar.SUNDAY)
    ttkcal.pack(expand=1, fill='both')

    if 'win' not in sys.platform:
        style = ttk.Style()
        style.theme_use('clam')           


    sf = SecondFrame(Tkinter.Toplevel())

    ttkcal.set_selection_callbeck(sf.update_lable)        

    root.mainloop() 

if __name__ == "__main__":
    #main2()
    test2()