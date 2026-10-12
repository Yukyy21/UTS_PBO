# Mengimpor modul pytest untuk kebutuhan unit testing dan pengujian exception
import pytest

# Mengimpor kelas Kasir dari modul kasir
from kasir import Kasir
# Mengimpor subclass Makanan dan Minuman dari modul models.jenis_barang
from models.jenis_barang import Makanan, Minuman


# Fungsi helper/pembantu untuk menginisialisasi objek Kasir dengan data sampel barang
def buat_kasir():
    # Membuat objek/instansiasi Kasir baru dengan nama toko "Toko Test"
    kasir = Kasir("Toko Test")
    # Menambahkan objek Makanan ("Nasi Goreng" seharga Rp20.000) ke dalam daftar belanja kasir
    kasir.tambah_barang(Makanan("Nasi Goreng", 20000))
    # Menambahkan objek Minuman ("Es Teh" seharga Rp5.000) ke dalam daftar belanja kasir
    kasir.tambah_barang(Minuman("Es Teh", 5000))
    # Mengembalikan objek kasir yang telah terisi barang untuk digunakan dalam pengujian
    return kasir


# Menguji apakah metode hitung_total() menghitung akumulasi harga barang dengan benar
def test_hitung_total():
    # Memastikan total harga dari Nasi Goreng (20000) + Es Teh (5000) sama dengan 25000
    assert buat_kasir().hitung_total() == 25000


# Menguji apakah hitung_total() mengembalikan 0 jika belum ada barang yang ditambahkan
def test_total_keranjang_kosong():
    # Memastikan objek Kasir baru yang keranjangnya kosong memiliki total belanja 0
    assert Kasir("Toko Test").hitung_total() == 0


# Menguji apakah teks struk memuat semua nama barang serta format total harga yang sesuai
def test_struk_memuat_semua_barang_dan_total():
    # Mengambil string struk belanja dari kasir yang sudah berisi data barang
    struk = buat_kasir().tampilkan_struk()
    # Memastikan string "Nasi Goreng" tercetak di dalam struk
    assert "Nasi Goreng" in struk
    # Memastikan string "Es Teh" tercetak di dalam struk
    assert "Es Teh" in struk
    # Memastikan format harga "Rp25.000" tercetak di dalam struk
    assert "Rp25.000" in struk


# Menguji validasi tipe data: memastikan kasir menolak input yang bukan turunan kelas Barang
def test_hanya_barang_yang_bisa_ditambahkan():
    # Membuat objek Kasir baru
    kasir = Kasir("Toko Test")
    # Memastikan bahwa sistem menangkap dan mengekspektasikan error bertipe TypeError
    with pytest.raises(TypeError):
        # Mencoba menambahkan string biasa (bukan objek Barang), yang harus memicu TypeError
        kasir.tambah_barang("bukan barang")
