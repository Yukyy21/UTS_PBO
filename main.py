from kasir import Kasir
from models.jenis_barang import Makanan, Minuman


def main() -> None:
    kasir = Kasir("Toko Maju Jaya")

    # Kasir memasukkan barang yang dibeli pelanggan ke daftar belanja
    kasir.tambah_barang(Makanan("Nasi Goreng", 20000))
    kasir.tambah_barang(Makanan("Mie Ayam", 15000))
    kasir.tambah_barang(Minuman("Es Teh Manis", 5000))
    kasir.tambah_barang(Minuman("Kopi Susu", 12000))

    # Tampilkan struk beserta total pembayaran
    print(kasir.tampilkan_struk())


if __name__ == "__main__":
    main()
