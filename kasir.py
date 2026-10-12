from models.barang import Barang


def rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class Kasir:
    """Mengelola transaksi penjualan.

    COMPOSITION : Kasir *memiliki* daftar belanja berisi objek Barang.
    POLYMORPHISM: tampilkan_struk() memanggil tampilkan_info() pada setiap
                  barang tanpa perlu memeriksa jenis konkretnya.
    """

    def __init__(self, nama_toko: str):
        self.__nama_toko = nama_toko
        self.__daftar_belanja: list[Barang] = []

    def tambah_barang(self, barang: Barang) -> None:
        if not isinstance(barang, Barang):
            raise TypeError("Hanya objek Barang yang dapat ditambahkan.")
        self.__daftar_belanja.append(barang)

    def hitung_total(self) -> int:
        return sum(barang.get_harga() for barang in self.__daftar_belanja)

    def tampilkan_struk(self) -> str:
        garis = "=" * 44
        baris = [garis, self.__nama_toko.center(44), garis]
        if not self.__daftar_belanja:
            baris.append("(belanjaan masih kosong)".center(44))
        else:
            for barang in self.__daftar_belanja:
                baris.append(barang.tampilkan_info())
        baris += ["-" * 44, f"{'TOTAL':<22}{rupiah(self.hitung_total()):>22}", garis]
        return "\n".join(baris)
