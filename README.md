# Sistem Kasir Toko — UTS PBO

Sistem kasir toko sederhana berbasis **Python** yang menerapkan 4 pilar
Pemrograman Berorientasi Objek (PBO): **Abstraction, Encapsulation,
Inheritance + Method Overriding, serta Polymorphism + Composition**.

Sistem menjual barang dalam dua kategori, **makanan** dan **minuman**. Setiap
barang menyimpan nama dan harga, ditampilkan sesuai kategorinya, lalu total
belanja dihitung otomatis saat struk dibuat.

## Struktur Proyek

```
.
├── models/
│   ├── __init__.py
│   ├── barang.py            # Barang (abstract): Abstraction & Encapsulation
│   └── jenis_barang.py      # Makanan, Minuman: Inheritance & Overriding
├── kasir.py                 # Kasir: Composition & Polymorphism
├── main.py                  # Program utama (demo)
├── tests/
│   ├── test_barang.py
│   ├── test_jenis_barang.py
│   └── test_kasir.py
├── docs/
│   └── analisis_kebutuhan.md
├── .gitignore
├── README.md
└── SKILL.md
```

## Rancangan Kelas

| Kelas | Peran | Konsep PBO |
|---|---|---|
| `Barang` (abstract) | Kerangka dasar semua barang; atribut `nama` dan `__harga`; method `get_harga()`, `set_harga()`, serta abstract `tampilkan_info()`. | Abstraction & Encapsulation |
| `Makanan` | Turunan `Barang` untuk kategori makanan; meng-override `tampilkan_info()`. | Inheritance & Method Overriding |
| `Minuman` | Turunan `Barang` untuk kategori minuman; meng-override `tampilkan_info()`. | Inheritance & Method Overriding |
| `Kasir` | Mengelola daftar belanja; `tambah_barang()`, `hitung_total()`, `tampilkan_struk()`. | Composition & Polymorphism |

## Cara Menjalankan

Butuh **Python 3**. Jalankan dari folder root proyek:

```bash
python main.py
```

Contoh keluaran:

```
============================================
              Toko Maju Jaya
============================================
[Makanan] Nasi Goreng - Rp20.000
[Makanan] Mie Ayam - Rp15.000
[Minuman] Es Teh Manis - Rp5.000
[Minuman] Kopi Susu - Rp12.000
--------------------------------------------
TOTAL                              Rp52.000
============================================
```

## Cara Menguji

```bash
pip install pytest
python -m pytest -v
```

> Gunakan `python -m pytest` (bukan sekadar `pytest`) agar root proyek masuk ke
> `sys.path` sehingga import `models`/`kasir` bekerja.

## Pembagian Tugas

| Anggota | Peran | File | Konsep PBO |
|---|---|---|---|
| Ahmad Bagus Indra Permadi | Fondasi & dokumentasi analisis | `models/barang.py`, `models/__init__.py`, `tests/test_barang.py`, `docs/analisis_kebutuhan.md`, `.gitignore` | Abstraction & Encapsulation |
| Ari Yoga Aditiya | Jenis barang & dokumentasi | `models/jenis_barang.py`, `tests/test_jenis_barang.py`, `README.md` | Inheritance & Method Overriding |
| Ahmad Rizky Nasrulloh | Pengelola & program utama | `kasir.py`, `main.py`, `tests/test_kasir.py` | Composition & Polymorphism |

## Pemetaan Konsep PBO → Kode

| Konsep PBO | Lokasi | Bukti di Kode |
|---|---|---|
| Abstraction | `models/barang.py` | `Barang(ABC)` + `@abstractmethod tampilkan_info()` |
| Encapsulation | `models/barang.py` | `self.__harga`, `get_harga()`, `set_harga()` dengan validasi |
| Inheritance | `models/jenis_barang.py` | `Makanan(Barang)`, `Minuman(Barang)` |
| Method Overriding | `models/jenis_barang.py` | `tampilkan_info()` berbeda tiap kategori |
| Composition | `kasir.py` | `self.__daftar_belanja` berisi objek `Barang` |
| Polymorphism | `kasir.py` | `tampilkan_struk()` memanggil `tampilkan_info()` tanpa tahu jenis konkret |

## Aturan Kolaborasi

- Semua perubahan lewat **Pull Request**, tidak push langsung ke `main`.
- 1 orang = 1 branch = file sendiri.
- Commit mengikuti format: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.
- Review silang antar anggota sebelum merge.
