class Mahasiswa:
    def __init__(self, nim, nama, python, web, cpp):
        self.nim = nim
        self.nama = nama
        self.python = python
        self.web = web
        self.cpp = cpp

    def hitung_rata_rata(self):
        return (self.python + self.web + self.cpp) / 3

    def layak_beasiswa(self):
        if self.python < 50 or self.web < 50 or self.cpp < 50:
            return False
        return self.hitung_rata_rata() >= 60
    
mahasiswas = []

# Input mahasiswa
while True:
    nim = input("\nMasukkan NIM (hanya angka, 0 untuk selesai): ")
    if nim == '0':
        break
    nama = input("Masukkan Nama Mahasiswa: ")
    python = float(input("Masukkan Nilai Python: "))
    web = float(input("Masukkan Nilai Web: "))
    cpp = float(input("Masukkan Nilai C++: "))

    mahasiswa = Mahasiswa(nim, nama, python, web, cpp)
    mahasiswas.append(mahasiswa)

# Proses peringkat beasiswa
layak = [mahasiswa for mahasiswa in mahasiswas if mahasiswa.layak_beasiswa()]
peringkat_mahasiswas = sorted(layak, key=lambda x: x.hitung_rata_rata(), reverse=True)[:3]

# Output peringkat
print("\nPeringkat Mahasiswa yang Layak Mendapat Beasiswa:")
for i, mahasiswa in enumerate(peringkat_mahasiswas):
    print(f"{i + 1}. NIM: {mahasiswa.nim}, Nama: {mahasiswa.nama}, Rata-rata: {mahasiswa.hitung_rata_rata()}")
