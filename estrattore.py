# importa il modulo
from tkinter import *
 
# costruisce una classe che gestisce la finestra
class Application(Frame):
        # metodo che scrive un messaggio a video
        def scrivi_messaggio(self):
                self.mess["text"] = "Ciao a tutti!",
     
        # metodo che pulisce il messaggio a video
        def cancella_messaggio(self):
                self.mess["text"] = "",
     
        # metodo costruttore che crea gli oggetti grafici
        def __init__(self, master=None):
                f = Frame(master)
                f.pack()
     
                # crea il bottone di uscita (di colore rosso)
                self.esci = Button(f)
                self.esci["text"] = "QUIT"
                self.esci["fg"] = "red"
                self.esci["command"] = f.quit
                self.esci.pack({"side": "left"})
 
                # crea il bottone che permette di scrivere il messaggio
                self.butt_mess = Button(f)
                self.butt_mess["text"] = "Scrivi", 
                self.butt_mess["command"] = self.scrivi_messaggio
                self.butt_mess.pack({"side": "left"})
         
                # crea il bottone che permette di pulire il messaggio
                self.butt_canc_mess = Button(f)
                self.butt_canc_mess["text"] = "Cancella",
                self.butt_canc_mess["command"] = self.cancella_messaggio
                self.butt_canc_mess.pack({"side": "left"})
         
                # crea l'oggetto grafico che contiene il messaggio
                self.mess = Message(f)
                self.mess["text"] = "",
         
                self.mess.pack({"side": "left"})
 
# corpo principale del programma
finestra = Tk()
app = Application(finestra)
finestra.mainloop()