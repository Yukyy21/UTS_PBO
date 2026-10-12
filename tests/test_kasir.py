import pytest

from kasir import Kasir
from models.jenis_barang import Makanan, Minuman


def buat_kasir():
    kasir = Kasir("Toko Test")
    kasir.tambah_barang(Makanan("Nasi Goreng", 20000))
    kasir.tambah_barang(Minuman("Es Teh", 5000))
    return kasir


def test_hitung_total():
    assert buat_kasir().hitung_total() == 25000


def test_total_keranjang_kosong():
    assert Kasir("Toko Test").hitung_total() == 0


def test_struk_memuat_semua_barang_dan_total():
    struk = buat_kasir().tampilkan_struk()
    assert "Nasi Goreng" in struk
    assert "Es Teh" in struk
    assert "Rp25.000" in struk


def test_hanya_barang_yang_bisa_ditambahkan():
    kasir = Kasir("Toko Test")
    with pytest.raises(TypeError):
        kasir.tambah_barang("bukan barang")
