from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry

master = Tk()
canvas = Canvas(master, height=450, width=750)
canvas.pack()

frame_ust = Frame(master, bg='#add8e6')
frame_ust.place(relx=0.1, rely=0.1, relwidth=0.75, relheight=0.1)

frame_alt_sol = Frame(master, bg='#add8e6')
frame_alt_sol.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

frame_alt_sag = Frame(master, bg='#8470ff')
frame_alt_sag.place(relx=0.34, rely=0.21, relwidth=0.51, relheight=0.5)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6', text="Hatirlatma tipi:", font="Verdana 12 bold")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("")

hatirlatma_tipi_acilir_menu = OptionMenu(frame_ust, hatirlatma_tipi_opsiyon, "dogum gunu", "alisveris", "odeme", "yapilacaklar")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarihi_etiket = Label(frame_ust, bg='#add8e6', text="Hatirlatma tarihi", font="Verdana 12 bold")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarihi_secici = DateEntry(frame_ust, width=12, background="orange", foreground="black", borderwidth=1, locale="de_DE")
hatirlatma_tarihi_secici._top_cal.overrideredirect(False)
hatirlatma_tarihi_secici.pack(padx=10, pady=10, side=RIGHT)

Label(frame_alt_sol, bg='#add8e6', text="Hatirlatma yontemi :", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)

var = IntVar()

R1 = Radiobutton(frame_alt_sol, text="Sisteme kaydet", variable=var, value=1, bg="#add8e6", font="Verdana 8")
R1.pack(anchor=NW, pady=5, padx=15)

var1 = IntVar()
c1 = Checkbutton(frame_alt_sol, text="Ayni gun", variable=var1, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 8")
c1.pack(anchor=NW, pady=2, padx=25)

var2 = IntVar()
c2 = Checkbutton(frame_alt_sol, text="Bir gun once", variable=var2, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 8")
c2.pack(anchor=NW, pady=2, padx=25)

var3 = IntVar()
c3 = Checkbutton(frame_alt_sol, text="Bir hafta once", variable=var3, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 8")
c3.pack(anchor=NW, pady=2, padx=25)

var4 = IntVar()
c4 = Checkbutton(frame_alt_sol, text="Bir ay once", variable=var4, onvalue=1, offvalue=0, bg="#add8e6", font="Verdana 8")
c4.pack(anchor=NW, pady=5, padx=25)

def gonder():
    son_mesaj = ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Mesajiniz sisteme kaydedilmistir.\n"
                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() != '' else "Genel"
                tarih = hatirlatma_tarihi_secici.get()
                mesaj = metin_alani.get("1.0", "end-1c")

                with open("hatirlatmalar.txt", "w") as dosya:
                    dosya.write('{} kategorisinde, {} tarihinde, {} notuyla hatirlatma.'.format(tip, tarih, mesaj))
                
            messagebox.showinfo("Basarili Islem", son_mesaj)
        else:
            son_mesaj = "Gerekli alanlari doldurdugunuzdan emin olun!!"
            messagebox.showwarning("Yetersiz Bilgi", son_mesaj)
    except Exception as e:
        son_mesaj = "Islem basarisiz oldu. Hata: " + str(e)
        messagebox.showerror("Basarisiz Bilgi", son_mesaj)
    finally:
        master.destroy()

Label(frame_alt_sag, bg='#add8e6', text="Hatirlatma mesaji:", font="Verdana 10 bold").pack(padx=10, pady=10, anchor=NW)

metin_alani = Text(frame_alt_sag, height=9, width=50)
metin_alani.tag_configure("style", foreground='#bfbfbf', font=('Verdana', 7, 'bold'))
metin_alani.pack()

karsilama_metni = 'Mesajini buraya yaz...'
metin_alani.insert(END, karsilama_metni, 'style')

gonder_butonu = Button(frame_alt_sag, text='Gonder', command=gonder)
gonder_butonu.pack(anchor=S)

master.mainloop()
