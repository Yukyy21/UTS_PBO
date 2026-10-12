from abc import ABC, abstractmethod


class Barang(ABC):
    """Kelas abstrak dasar seluruh jenis barang (ABSTRACTION).

    Nama bersifat umum, sedangkan harga dikelola secara privat
    (ENCAPSULATION) melalui get_harga() dan set_harga() yang tervalidasi.
    """

    def __init__(self, nama: str, harga: int):
        if not nama:
            raise ValueError("Nama barang tidak boleh kosong.")
        self.nama = nama
        self.__harga = 0
        self.set_harga(harga)

    def get_harga(self) -> int:
        return self.__harga

    def set_harga(self, nilai: int) -> None:
        if nilai < 0:
            raise ValueError("Harga tidak boleh negatif.")
        self.__harga = nilai

    @abstractmethod
    def tampilkan_info(self) -> str:
        """Keterangan barang yang berbeda tiap kategori (OVERRIDING)."""
