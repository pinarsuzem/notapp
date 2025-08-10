import tkinter as tk
from tkinter import filedialog, messagebox


def not_kaydet():
    dosya_yolu = filedialog.asksaveasfilename(defaultextension=".txt",
                                              filetypes=[("Metin Dosyası", "*.txt")])
    if dosya_yolu:
        try:
            with open(dosya_yolu, "w", encoding="utf-8") as dosya:
                dosya.write(text_area.get("1.0", tk.END))
            messagebox.showinfo("Başarılı", "Not başarıyla kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilemedi: {e}")

def not_ac():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("Metin Dosyası", "*.txt")])
    if dosya_yolu:
        try:
            with open(dosya_yolu, "r", encoding="utf-8") as dosya:
                icerik = dosya.read()
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, icerik)
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya açılamadı: {e}")


pencere = tk.Tk()
pencere.title("Not Defteri")
pencere.geometry("600x400")

menu_bar = tk.Menu(pencere)
pencere.config(menu=menu_bar)

dosya_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Dosya", menu=dosya_menu)
dosya_menu.add_command(label="Aç", command=not_ac)
dosya_menu.add_command(label="Kaydet", command=not_kaydet)
dosya_menu.add_separator()
dosya_menu.add_command(label="Çıkış", command=pencere.quit)

# Metin alanı
text_area = tk.Text(pencere, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")

pencere.mainloop()