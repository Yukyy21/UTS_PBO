import pytest

from models.barang import Barang
from models.jenis_barang import Makanan


def test_barang_abstrak_tidak_bisa_diinstansiasi():
    with pytest.raises(TypeError):
        Barang("Apel", 10000)


def test_get_dan_set_harga():
    apel = Makanan("Apel", 10000)
    assert apel.get_harga() == 10000
    apel.set_harga(12000)
    assert apel.get_harga() == 12000


def test_harga_negatif_ditolak():
    apel = Makanan("Apel", 10000)
    with pytest.raises(ValueError):
        apel.set_harga(-1)


def test_harga_negatif_saat_dibuat_ditolak():
    with pytest.raises(ValueError):
        Makanan("Apel", -1)


def test_nama_kosong_ditolak():
    with pytest.raises(ValueError):
        Makanan("", 10000)
