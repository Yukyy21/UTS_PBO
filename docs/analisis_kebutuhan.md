# ANALISIS KEBUTUHAN SISTEM KASIR TOKO

## Implementasi Pemrograman Berorientasi Objek (PBO)

---

## A. Studi Kasus

Dalam kegiatan jual beli sehari-hari, kasir memiliki peran penting dalam melayani pelanggan dan memastikan setiap transaksi berjalan dengan baik. Namun, pada toko yang masih menggunakan cara manual, proses penghitungan belanja biasanya dilakukan dengan mencatat harga barang satu per satu, kemudian menjumlahkannya menggunakan kalkulator. Cara ini membutuhkan waktu dan berisiko menimbulkan kesalahan ketika menghitung total pembayaran.

Untuk mengatasi permasalahan tersebut, dibuat sebuah program Sistem Kasir Toko menggunakan bahasa pemrograman Python dengan menerapkan konsep Pemrograman Berorientasi Objek (PBO). Program ini dirancang untuk membantu kasir mengelola barang yang dibeli pelanggan, mulai dari menyimpan informasi barang, menampilkan harga, mencatat daftar belanja, hingga menghitung total pembayaran secara otomatis.

Dengan adanya sistem ini, proses transaksi diharapkan menjadi lebih praktis, teratur, dan mengurangi kemungkinan terjadinya kesalahan perhitungan.

## B. Tujuan Sistem

Pembuatan Sistem Kasir Toko memiliki beberapa tujuan, yaitu:

- Membantu kasir melakukan transaksi penjualan dengan lebih mudah dan efisien.
- Meminimalkan kesalahan saat menghitung total harga barang yang dibeli pelanggan.
- Memudahkan pengelompokan barang berdasarkan kategori, seperti makanan dan minuman.
- Menerapkan konsep Pemrograman Berorientasi Objek untuk menyelesaikan permasalahan yang dapat ditemukan dalam kegiatan sehari-hari.
- Menghasilkan program dengan struktur yang jelas sehingga lebih mudah dipahami, diperbaiki, dan dikembangkan di kemudian hari.

## C. Analisis Kebutuhan Sistem

Sebelum program dibuat, perlu ditentukan kebutuhan yang harus dipenuhi agar sistem dapat berjalan sesuai dengan tujuan. Kebutuhan tersebut dibagi menjadi kebutuhan fungsional dan nonfungsional.

### 1. Kebutuhan Fungsional

Kebutuhan fungsional menjelaskan fitur dan kemampuan yang harus dimiliki oleh program. Pada Sistem Kasir Toko, kebutuhan tersebut meliputi:

- Program mampu menyimpan informasi dasar barang, berupa nama dan harga.
- Program dapat mengelompokkan barang ke dalam kategori tertentu, seperti makanan dan minuman.
- Program dapat menampilkan informasi barang beserta harga sesuai dengan jenisnya.
- Kasir dapat memasukkan barang yang dibeli pelanggan ke dalam daftar belanja.
- Program mampu menjumlahkan harga seluruh barang secara otomatis.
- Program dapat menampilkan daftar barang yang dibeli beserta total pembayaran pada akhir transaksi.

### 2. Kebutuhan Nonfungsional

Kebutuhan nonfungsional berkaitan dengan kualitas program, teknologi yang digunakan, serta kemudahan dalam pengoperasiannya. Adapun kebutuhan tersebut adalah:

- Program dikembangkan menggunakan bahasa pemrograman Python.
- Struktur program menerapkan prinsip Pemrograman Berorientasi Objek.
- Setiap kelas memiliki tugas dan tanggung jawab yang jelas agar kode lebih terorganisasi.
- Informasi harga barang dikelola melalui mekanisme enkapsulasi untuk membatasi akses langsung terhadap atribut.
- Kode program disusun dengan cara yang mudah dibaca, dipahami, dan dikembangkan kembali.
- Program dapat dijalankan melalui terminal atau Command Prompt pada perangkat yang telah memiliki Python.

## D. Pemetaan Kebutuhan ke Solusi PBO

Konsep PBO digunakan untuk menyusun program berdasarkan objek yang mewakili kebutuhan dalam sistem kasir. Setiap konsep memiliki fungsi tersendiri dalam membantu program bekerja secara terstruktur.

| Permasalahan atau Kebutuhan | Solusi dalam Program | Konsep PBO |
|---|---|---|
| Setiap barang memiliki informasi dasar, seperti nama dan harga, serta perlu menampilkan informasi tersebut. | Membuat kelas abstrak `Barang` sebagai dasar bagi seluruh jenis barang. Kelas ini menentukan atribut umum dan method `tampilkan_info()`. | Abstraksi (Abstraction) |
| Harga barang perlu dikelola agar tidak diubah secara langsung tanpa melalui mekanisme yang ditentukan. | Menyimpan harga dalam atribut privat `__harga` dan menyediakan method `get_harga()` serta `set_harga()` untuk mengakses dan mengubah nilainya. | Enkapsulasi (Encapsulation) |
| Barang yang dijual memiliki kategori berbeda, seperti makanan dan minuman. | Membuat kelas `Makanan` dan `Minuman` yang mewarisi kelas `Barang`. Kedua kelas dapat memberikan tampilan informasi sesuai kategorinya melalui method overriding. | Pewarisan (Inheritance) dan Method Overriding |
| Kasir perlu menyimpan banyak barang dalam satu transaksi dan menghitung seluruh harganya. | Membuat kelas `Kasir` yang mengelola kumpulan objek barang dalam daftar belanja dan menghitung total pembayaran. | Composition |
| Barang dari kategori berbeda perlu menampilkan informasi melalui pemanggilan method yang sama. | Kelas `Kasir` memanggil `tampilkan_info()` pada setiap objek tanpa harus memeriksa jenis barang satu per satu. | Polimorfisme (Polymorphism) |

Berdasarkan pemetaan tersebut, konsep PBO tidak hanya digunakan sebagai bagian dari penulisan kode, tetapi juga untuk menyelesaikan kebutuhan sistem secara lebih teratur. Pembagian tugas antarkelas membantu membuat program lebih mudah dikembangkan ketika nantinya terdapat kategori barang atau fitur baru.

## E. Penerapan Konsep PBO pada Program

### 1. Abstraksi dan Enkapsulasi (Abstraction and Encapsulation)

Abstraksi digunakan untuk membuat gambaran umum mengenai barang yang akan dikelola oleh sistem. Penerapannya dilakukan melalui kelas abstrak `Barang`, yang berfungsi sebagai dasar bagi kelas-kelas barang lainnya. Kelas ini mendefinisikan informasi umum yang dimiliki barang sekaligus menetapkan method `tampilkan_info()` sebagai method yang harus diimplementasikan oleh kelas turunannya.

Dalam Python, penerapan tersebut dapat menggunakan modul `abc`, dekorator `@abstractmethod`, dan kelas `ABC`. Dengan cara ini, setiap jenis barang memiliki kewajiban untuk menyediakan implementasi method yang sesuai.

Sementara itu, enkapsulasi diterapkan dengan menjadikan harga barang sebagai atribut privat bernama `__harga`. Atribut ini tidak ditujukan untuk diakses secara langsung dari luar kelas. Sebagai gantinya, program menyediakan method `get_harga()` untuk mengambil nilai harga dan `set_harga()` untuk memperbaruinya.

Melalui mekanisme tersebut, pengelolaan harga menjadi lebih terkontrol. Method `set_harga()` juga dapat dilengkapi dengan validasi, misalnya untuk memastikan harga tidak bernilai negatif. Dengan demikian, data barang dapat dijaga agar tetap sesuai dengan aturan yang ditetapkan oleh program.

### 2. Pewarisan dan Method Overriding (Inheritance and Method Overriding)

Pewarisan memungkinkan suatu kelas menggunakan atribut dan method yang telah didefinisikan pada kelas induknya. Dalam sistem ini, kelas `Makanan` dan `Minuman` merupakan turunan dari kelas `Barang`.

Kedua kelas tersebut dapat memanfaatkan constructor dan method dasar milik `Barang` melalui penggunaan `super()`. Hal ini membantu mengurangi pengulangan kode karena informasi umum barang cukup didefinisikan pada kelas induk.

Selain pewarisan, program juga menerapkan method overriding. Konsep ini digunakan ketika kelas `Makanan` dan `Minuman` memiliki implementasi masing-masing untuk method `tampilkan_info()`. Walaupun nama method yang digunakan sama, informasi yang ditampilkan dapat disesuaikan dengan karakteristik setiap kategori barang.

Sebagai contoh, informasi makanan dapat menampilkan keterangan kategori makanan, sedangkan informasi minuman menampilkan keterangan kategori minuman. Dengan begitu, setiap kelas dapat memiliki perilaku yang sesuai tanpa mengubah struktur dasar yang telah dibuat.

### 3. Kelas Pengelola (Composition and Polymorphism)

Kelas `Kasir` berfungsi sebagai bagian yang mengatur jalannya transaksi. Kelas ini menyimpan daftar barang yang dipilih pelanggan, menyediakan method untuk menambahkan barang, menghitung total harga, serta menampilkan struk pembelian.

Konsep composition diterapkan melalui hubungan antara kelas `Kasir` dan kumpulan objek barang yang dikelolanya. Objek-objek tersebut ditempatkan dalam sebuah list sehingga kasir dapat memproses beberapa barang dalam satu transaksi. Dalam rancangan ini, kelas `Kasir` bertanggung jawab mengelola daftar belanja yang menjadi bagian dari proses transaksi.

Di sisi lain, polymorphism diterapkan ketika kelas `Kasir` memanggil method `tampilkan_info()` pada setiap objek di dalam daftar belanja. Objek yang diproses dapat berupa `Makanan` maupun `Minuman`, tetapi keduanya tetap dapat menggunakan nama method yang sama.

Program tidak perlu memeriksa kategori setiap barang menggunakan rangkaian percabangan `if-else` hanya untuk menentukan cara menampilkan informasinya. Python akan menjalankan implementasi method sesuai dengan kelas dari objek yang sedang diproses.

Penerapan ini membuat pengelolaan berbagai jenis barang menjadi lebih fleksibel dan memudahkan penambahan kategori baru apabila dibutuhkan.

### 4. Program Utama

Program utama merupakan bagian yang menghubungkan seluruh kelas agar dapat digunakan dalam sebuah transaksi. Pada bagian ini, program membuat objek dari kelas `Makanan` dan `Minuman` dengan mengisi informasi yang diperlukan, seperti nama dan harga barang.

Setelah objek dibuat, barang-barang tersebut dimasukkan ke dalam daftar belanja melalui method `tambah_barang()` milik kelas `Kasir`. Selanjutnya, method `tampilkan_struk()` dipanggil untuk memperlihatkan seluruh barang yang dibeli beserta total pembayaran pelanggan.

Dengan alur tersebut, setiap kelas menjalankan tugasnya masing-masing. Kelas barang bertanggung jawab atas informasi dan tampilan barang, sedangkan kelas kasir mengelola transaksi serta perhitungan total harga. Pembagian tugas ini membantu menjaga agar kode program tetap terstruktur.

## F. Rancangan Kelas

Rancangan kelas dibuat untuk menentukan peran setiap bagian program sebelum seluruh kode diimplementasikan. Pembagian kelas pada Sistem Kasir Toko adalah sebagai berikut.

### Kelas `Barang`

Kelas ini merupakan kelas abstrak yang menjadi dasar bagi jenis barang lainnya. Kelas `Barang` menyimpan informasi umum berupa nama dan harga serta menetapkan method abstrak `tampilkan_info()` yang harus diterapkan oleh kelas turunannya.

### Kelas `Makanan`

Kelas `Makanan` merupakan turunan dari `Barang` yang digunakan untuk merepresentasikan produk kategori makanan. Kelas ini mewarisi atribut dan method dasar dari kelas induk serta dapat menyediakan tampilan informasi yang sesuai dengan kategorinya.

### Kelas `Minuman`

Kelas `Minuman` juga merupakan turunan dari `Barang`, tetapi digunakan untuk mengelola produk kategori minuman. Sama seperti kelas `Makanan`, kelas ini mengimplementasikan method `tampilkan_info()` sesuai kebutuhan.

### Kelas `Kasir`

Kelas `Kasir` bertugas mengelola daftar belanja pelanggan. Di dalamnya terdapat method untuk menambahkan barang, menghitung total pembayaran, dan menampilkan struk transaksi.

### Program Utama

Program utama digunakan untuk menjalankan seluruh proses, mulai dari membuat objek barang, menambahkan barang ke daftar belanja, hingga menampilkan hasil transaksi. Bagian ini menjadi penghubung antara objek-objek yang telah dirancang.

Dengan pembagian tersebut, setiap kelas memiliki fungsi yang lebih jelas. Apabila suatu saat diperlukan perubahan pada cara menampilkan informasi barang, misalnya, perubahan dapat dilakukan pada kelas terkait tanpa harus mengubah seluruh bagian program.

## G. Kebutuhan Perangkat

Untuk membuat dan menjalankan Sistem Kasir Toko, diperlukan beberapa perangkat pendukung sebagai berikut.

- **Perangkat keras:** laptop atau komputer yang mampu menjalankan Python dan aplikasi penyunting kode.
- **Sistem operasi:** Windows, Linux, macOS, atau sistem operasi lain yang mendukung penggunaan Python.
- **Perangkat lunak:** Python 3 sebagai bahasa pemrograman yang digunakan.
- **Editor kode:** aplikasi seperti Visual Studio Code, IDLE, atau Sublime Text untuk menulis dan mengelola kode program.
- **Terminal atau Command Prompt:** digunakan untuk menjalankan program serta melihat hasil transaksi yang ditampilkan.

Kebutuhan perangkat tersebut relatif sederhana sehingga program dapat dikembangkan dan diuji tanpa memerlukan perangkat khusus. Untuk rancangan yang menggunakan keluaran berbasis teks, program juga dapat dijalankan langsung melalui terminal.

## H. Kesimpulan

Berdasarkan analisis yang telah dilakukan, Sistem Kasir Toko merupakan salah satu contoh penerapan Pemrograman Berorientasi Objek untuk membantu menyelesaikan permasalahan dalam kegiatan penjualan. Sistem ini dirancang untuk memudahkan pengelolaan barang, pencatatan daftar belanja, perhitungan total pembayaran, dan penampilan struk transaksi secara otomatis.

Penerapan konsep abstraksi membantu membentuk kerangka dasar barang, sedangkan enkapsulasi digunakan untuk mengatur akses terhadap data harga. Pewarisan memungkinkan kelas `Makanan` dan `Minuman` menggunakan struktur dasar yang sama, sementara method overriding memberikan perilaku tampilan yang berbeda pada setiap kategori. Selanjutnya, composition membantu kelas `Kasir` mengelola kumpulan barang, dan polymorphism memungkinkan objek yang berbeda diproses melalui pemanggilan method yang sama.

Melalui rancangan tersebut, dapat dipahami bahwa PBO membantu menyusun program menjadi bagian-bagian yang memiliki tanggung jawab masing-masing. Struktur seperti ini membuat kode lebih mudah dibaca, diuji, dan dikembangkan kembali. Walaupun sistem yang dirancang masih sederhana, program ini dapat menjadi dasar untuk pengembangan sistem kasir yang lebih lengkap, misalnya dengan penambahan jumlah barang, stok persediaan, diskon, metode pembayaran, dan penyimpanan riwayat transaksi.
