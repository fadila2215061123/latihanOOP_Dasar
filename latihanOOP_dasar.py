class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        self.krs = []

    def tambah_matkul(self, mata_kuliah):
        self.krs.append(mata_kuliah)
        print(f"{self.nama} telah menambahkan mata kuliah {mata_kuliah} ke dalam KRS.")

    def tampilkan_krs(self):
        print(f"KRS {self.nama} ({self.npm}): {', '.join(self.krs)}")

class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip
        self.mahasiswa_bimbingan = []

    def bimbing_mahasiswa(self, mahasiswa):
        self.mahasiswa_bimbingan.append(mahasiswa)
        print(f"{self.nama} memvalidasi krs {mahasiswa.nama}.")

    def tampilkan_mahasiswa_bimbingan(self):
        print(f"Daftar mahasiswa bimbingan {self.nama} ({self.nip}):")
        for mahasiswa in self.mahasiswa_bimbingan:
            print(f"- {mahasiswa.nama} ({mahasiswa.npm})")

# Contoh penggunaan kelas Mahasiswa dan Dosen
mahasiswa1 = Mahasiswa("Andi", "123456")
mahasiswa2 = Mahasiswa("Budi", "234567")
dosen1 = Dosen("Denny Budiman", "987654")

# Tambah mata kuliah ke KRS mahasiswa
mahasiswa1.tambah_matkul("PBO")
mahasiswa1.tambah_matkul("PWEB")
mahasiswa2.tambah_matkul("Jarkom")

# Tampilkan KRS mahasiswa
mahasiswa1.tampilkan_krs()
mahasiswa2.tampilkan_krs()

# Dosen membimbing mahasiswa
dosen1.bimbing_mahasiswa(mahasiswa1)
dosen1.bimbing_mahasiswa(mahasiswa2)

# Tampilkan daftar mahasiswa bimbingan dosen
dosen1.tampilkan_mahasiswa_bimbingan()