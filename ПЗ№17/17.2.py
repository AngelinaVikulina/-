# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9. Скорость первого автомобиля Vi км/ч, второго — V2 км/ч, расстояние
# между ними S км. Определить расстояние между ними через T часов, если автомобили
# первоначально движутся навстречу друг другу. Данное расстояние равно модулю разности
# начального расстояния и общего пути, проделанного автомобилями; общий путь = время •
# суммарная скорость.
import tkinter as tk

def calculate_distance():
    v1 = float(entry_v1.get())
    v2 = float(entry_v2.get())
    s = float(entry_s.get())
    t = float(entry_t.get())

    initial_distance = abs(s)
    total_distance = t * (v1 + v2)
    final_distance = abs(initial_distance - total_distance)

    result_label.config(text=f"Distance between the cars after {t} hours: {final_distance} km")


root = tk.Tk()
root.title("Car Distance Calculator")


label_v1 = tk.Label(root, text="Speed of Car 1 (km/h):")
label_v1.pack()
entry_v1 = tk.Entry(root)
entry_v1.pack()

label_v2 = tk.Label(root, text="Speed of Car 2 (km/h):")
label_v2.pack()
entry_v2 = tk.Entry(root)
entry_v2.pack()

label_s = tk.Label(root, text="Initial Distance (km):")
label_s.pack()
entry_s = tk.Entry(root)
entry_s.pack()

label_t = tk.Label(root, text="Time (hours):")
label_t.pack()
entry_t = tk.Entry(root)
entry_t.pack()

calculate_button = tk.Button(root, text="Calculate Distance", command=calculate_distance)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
