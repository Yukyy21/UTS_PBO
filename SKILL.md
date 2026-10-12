# SKILL: Sistem Kasir Toko — Pemrograman Berorientasi Objek (Python)

> Tugas kelompok (3 anggota) · Bahasa: Python 3 · Kolaborasi: Git & GitHub

Dokumen ini adalah panduan implementasi. Latar belakang dan analisis lengkap ada
di [`docs/analisis_kebutuhan.md`](docs/analisis_kebutuhan.md).

---

## 1. Ringkasan Kasus

Toko menjual barang dalam dua kategori: **makanan** dan **minuman**. Sistem
kasir dibuat untuk:

- menyimpan informasi barang (nama dan harga),
- mengelompokkan barang per kategori,
- menampilkan informasi barang sesuai jenisnya,
- mencatat daftar belanja pelanggan,
- menghitung total pembayaran secara otomatis,
- menampilkan struk transaksi.

---

## 2. Struktur Proyek

```
.
├── models/
│   ├── __init__.py          # file kosong
│   ├── barang.py            # [Anggota 1] Abstraction & Encapsulation
│   └── jenis_barang.py      # [Anggota 2] Inheritance & Overriding
├── kasir.py                 # [Anggota 3] Composition & Polymorphism
├── main.py                  # [Anggota 3] Program utama
├── tests/
│   ├── test_barang.py       # [Anggota 1]
│   ├── test_jenis_barang.py # [Anggota 2]
│   └── test_kasir.py        # [Anggota 3]
├── docs/
│   └── analisis_kebutuhan.md
├── .gitignore
├── README.md                # [Anggota 2]
└── SKILL.md                 # dokumen ini
```

---

## 3. Rancangan Kelas

```
            <<abstract>>
              Barang
        - nama
        - __harga
        + get_harga()
        + set_harga(nilai)
        + tampilkan_info()*        (abstrak)
              ▲
    ┌─────────┴─────────┐
  Makanan            Minuman
 (tampilkan_info)   (tampilkan_info)

   Kasir  ◆──── memiliki ────▶ banyak Barang   (Composition)
   - __daftar_belanja
   + tambah_barang()
   + hitung_total()
   + tampilkan_struk()            → polimorfisme
```

### Pemetaan 4 pilar PBO

| Konsep PBO | Dimana | Bukti di Kode |
|---|---|---|
| Abstraction | `models/barang.py` | `Barang(ABC)` + `@abstractmethod tampilkan_info()` |
| Encapsulation | `models/barang.py` | `self.__harga`, `get_harga()`, `set_harga()` + validasi |
| Inheritance | `models/jenis_barang.py` | `Makanan(Barang)`, `Minuman(Barang)` |
| Method Overriding | `models/jenis_barang.py` | `tampilkan_info()` berbeda tiap kategori |
| Composition | `kasir.py` | `self.__daftar_belanja` berisi objek `Barang` |
| Polymorphism | `kasir.py` | `tampilkan_struk()` memanggil `tampilkan_info()` tanpa cek tipe |

---

## 4. Kontrak antar anggota (disepakati di awal)

- `Barang` punya atribut `nama` (umum), harga privat `__harga`, method
  `get_harga()`, `set_harga(nilai)`, dan abstract `tampilkan_info() -> str`.
- Subclass menerima parameter urut: `nama, harga`.
- `tampilkan_info()` **mengembalikan string** (bukan print).
- `Kasir` hanya bergantung pada kontrak `Barang`, bukan subclass tertentu,
  dengan method `tambah_barang(barang)`, `hitung_total()`, dan
  `tampilkan_struk() -> str`.

---

## 5. Pembagian Tugas

| Anggota | Peran | File | Konsep | Branch |
|---|---|---|---|---|
| **Anggota 1** | Fondasi & dokumentasi analisis | `models/barang.py`, `models/__init__.py`, `tests/test_barang.py`, `docs/analisis_kebutuhan.md`, `.gitignore` | Abstraction & Encapsulation | `feature/abstraction-encapsulation` |
| **Anggota 2** | Jenis barang & dokumentasi | `models/jenis_barang.py`, `tests/test_jenis_barang.py`, `README.md` | Inheritance & Overriding | `feature/inheritance-overriding` |
| **Anggota 3** | Pengelola & program utama | `kasir.py`, `main.py`, `tests/test_kasir.py` | Composition & Polymorphism | `feature/kasir-main` |

### Urutan pengerjaan

1. **Hari 1:** Anggota 1 menyiapkan repo + kerangka + `barang.py`, lalu mengundang Anggota 2 & 3.
2. **Hari 2–3:** Anggota 2 dan 3 bekerja **paralel**.
3. **Hari 4:** Merge semua branch, jalankan `main.py` dan seluruh test.
4. **Hari 5:** Finalisasi README, rapikan, kumpulkan.

---

## 6. Alur Kerja Git (Feature Branch Workflow)

```bash
git checkout main
git pull origin main
git checkout -b feature/nama-branch-kamu

# kerjakan kode, lalu:
git add <file>
git commit -m "feat: <deskripsi>"
git push -u origin feature/nama-branch-kamu
```

Lalu buat **Pull Request**, minta 1 teman sebagai reviewer, dan merge setelah di-approve.

Format pesan commit: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.

---

## 7. Cara Menjalankan & Menguji

```bash
# Jalankan program utama (dari folder root proyek)
python main.py

# Jalankan test (butuh: pip install pytest)
python -m pytest -v
```

---

## 8. Checklist Pengumpulan

- [ ] Repo GitHub berisi seluruh struktur proyek.
- [ ] Setiap anggota punya **commit** dan **Pull Request** atas namanya.
- [ ] `python main.py` berjalan tanpa error.
- [ ] Empat konsep PBO terlihat jelas di kode.
- [ ] `README.md` memuat deskripsi, cara menjalankan, dan pembagian tugas.
- [ ] Analisis kebutuhan tersedia di `docs/`.
- [ ] Link repo dikumpulkan sesuai instruksi dosen.
