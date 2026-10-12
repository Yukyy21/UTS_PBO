from models.barang import Barang


class Makanan(Barang):
    """Barang kategori makanan."""

    def tampilkan_info(self) -> str:  # override
        return f"[Makanan] {self.nama} - Rp{self.get_harga():,}".replace(",", ".")


class Minuman(Barang):
    """Barang kategori minuman."""

    def tampilkan_info(self) -> str:  # override
        return f"[Minuman] {self.nama} - Rp{self.get_harga():,}".replace(",", ".")
