from models.barang import Barang
from models.jenis_barang import Makanan, Minuman


def test_tampilkan_info_makanan():
    info = Makanan("Nasi Goreng", 20000).tampilkan_info()
    assert "Makanan" in info
    assert "Nasi Goreng" in info
    assert "Rp20.000" in info


def test_tampilkan_info_minuman():
    info = Minuman("Es Teh", 5000).tampilkan_info()
    assert "Minuman" in info
    assert "Es Teh" in info
    assert "Rp5.000" in info


def test_makanan_dan_minuman_adalah_barang():
    assert isinstance(Makanan("Apel", 10000), Barang)
    assert isinstance(Minuman("Air", 3000), Barang)
