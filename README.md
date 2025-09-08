# Flystep
A Simple Online Shopping Web App built with Django to fulfill PBP's Assignment Requirements.

The deployment for this project can be found [here](https://vincent-valentino-flystep.pbp.cs.ui.ac.id).

---

# Jawaban Tugas

## Tugas 1

### 1. Cara penyelesaian checklist
- Menentukan tema kecil, akhirnya menetapkan tema kecil pada pakaian dan sepatu dalam olahraga.
- Membuat sebuah directory baru, disini saya beri nama flystep, sama dengan nama project yang digunakan.
- Inisialisasi git di root project ini
- Inisialisasi virtual env menggunakan venv (di root project ini juga)
- Copy .gitignore dan requirements.txt dari project tutorial, karena isi kedua file ini seharusnya serupa, dan tidak terlalu penting (untuk pembelajaran).
- Membaca beberapa docs dari UI library yang menyediakan CDN untuk penggunaan langsung, memutuskan untuk memilih daisyui karena mudah.
- Start django project, pada root directory project ini, dengan nama yang sama dengan nama directory project ini.
- Start django app, dengan nama main sesuai keperluan soal dan konvensi.
- Menambahkan sebuah model sesuai keperluan soal ditambahkan stok, created, dan updated at (sering digunakan, ini utk future proof)
- Membuat sebuah template baru di dalam aplikasi main dan mencoba menggunakannya melalui penambahan fungsi render_main pada views.py dan inklusi path tersebut pada main.urls, dan registrasi pada flystep.urls.
- Register model pada main.admin, namun tidak berhasil, menemukan referensi dari stackoverflow, mengganti `admin.register(Product)` menjadi `admin.site.register(Product)`.
- Menambahkan produk melalui django admin (pada sqlite).
- Menambahkan context pada fungsi render_main dan menambahkan penggunaannya pada template main.html.
- Mengubah theme yang digunakan pada template main.html
- Menambahkan beberapa product melalui `python manage.py shell` di PWS.
- Walaupun app benar, sadar kesalahan pengerjaan jawaban tugas di readme ini (Harusnya ganjil 2026, malah kerjain ganjil 2025)
  ![Absolute Cinema](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4q50jB9MY5kkcSh7NUSn1tb8P0Te86aRU5A&s)
- Revisi Jawaban dalam Readme ini

### 2. Bagan lifecycle request dalam Django

![Bagan Lifecycle Request dalam Django](./assets/tugas1/bagan-soal2.png)

Django menganut arsitektur MTV (Model Template View). Intinya suatu request akan diroute oleh file `urls.py` ke view yang sesuai, kemudian view tersebut dapat melakukan CRUD (Create Read Update Delete) (opsional) melalui model, dan dapat mengambil template yang diperlukan dan mempopulasinya sesuai dengan konteks yang diberikan dan keperluan template (opsional) sehingga menghasilkan suatu http response yang akan diterima oleh user.

### 3. Peran settings.py dalam proyek Django
seperti namanya, [settings.py](./flystep/settings.py) berisi berbagai pengaturan yang bersangkutan dengan aplikasi kita seperti installed apps, middleware, pengaturan behaviour aplikasi (allowed hosts, debug mode, dsb), database, i18n, logging, dan banyak lainnya. Intinya file ini berguna dalam pengaturan perilaku aplikasi secara keseluruhan.

### 4. Cara kerja migrasi Django
Migrasi dalam konteks ini adalah sebuah cara untuk melakukan update kepada schema database kita mengikuti model yang ada. Tentunya setiap kali kita melakukan update pada model kita, migrasi perlu dilakukan untuk sync schema database dan model kita. Dalam Django sendiri untuk melakukan migrasi, kita dapat menjalankan `python manage.py makemigrations` untuk membuat file migrasi yang diperlukan (umumnya dalam bentuk file sql, isinya berbagai macam perintah seperti alter, create, delete, dsb) dan `python manage.py migrate` untuk mengaplikasi migrasi tersebut kepada relational database kita. 

### 5. Alasan penggunaan Django pada PBP
Saya dapat mengemukakan beberapa asumsi untuk hal ini, seperti penggunaan bahasa yang sama, yakni python pada DDP 1, sehingga ketika mahasiswa berhadapan dengan PBP, setidaknya mahasiswa tidak perlu mempelajari bahasanya lagi dari awal, namun hanya perlu mempelajari toolsnya. Selain itu, opsi lain seperti laravel, dan php yang digunakan sebelumnya ditinggalkan berdasarkan konsiderasi tren pasar dan alasan keamanan. Namun menurut saya, terdapat banyak javascript framework yang lebih suitable untuk pbp dengan alasan teknologi yang lebih modern dan tren pasar yang semakin meningkat, seperti Nextjs, SvelteKit, Astro.

### 6. Feedback untuk asisten dosen tutorial sebelumnya
Sudah cukup baik, walaupun secara online, asisten dosen selalu tersedia di voice channel di discord dan sangat mudah mendapatkan bantuan apabila diperlukan. Dalam pengerjaan tutorial sebenarnya terlalu banyak yang diberikan kepada mahasiswa, sehingga kami seperti tinggal melakukan copy and paste terhadap dokumennya mengingat constraint waktu. Namun setelah dibaca kembali, saya rasa website pbp ini sangat informatif dan sangat dapat digunakan terutama dalam pembelajaran ulang.

---

## Tugas 2
### Placeholder
- Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
- Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
---

Thank you for reading this far!


