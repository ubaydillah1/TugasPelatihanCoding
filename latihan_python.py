# Volume Balok
print("Volume Balok")
panjang_balok = float(input("Masukkan panjang balok = "))
lebar_balok = float(input("Masukkan lebar balok = "))
tinggi_balok = float(input("Masukkan tinggi balok = "))

volume_balok = panjang_balok * lebar_balok * tinggi_balok

print("Volume balok adalah =", round(volume_balok))
# End Volume Balok


# Volume Tabung
print("Volume Tabung")
jari_jari_tabung = int(input("Masukkan jari-jari tabung = "))
tinggi_tabung = int(input("Masukkan tinggi tabung: "))

volume_tabung = 3.14 * jari_jari_tabung * 2 * tinggi_tabung

print("Volume tabung adalah =", round(volume_tabung))
# End Volume Tabung


# Volume Bola
print("Volume Bola")
jari_jari_bola = float(input("Masukkan jari-jari bola = "))

volume_bola = 4 / 3 * 3.14 * jari_jari_bola**3

print("Volume bola adalah =", round(volume_bola))
# End Volume Bola