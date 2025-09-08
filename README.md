# Flystep
A Simple Online Shopping Web App built with Django to fulfill PBP's Assignment Requirements.

The deployment for this project can be found [here](https://vincent-valentino-flystep.pbp.cs.ui.ac.id).

---

## Jawaban Tugas

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

### 2. Bagan lifecycle request dalam Django

![Bagan Lifecycle Request dalam Django](./bagan-soal2.png)

2. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak!

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

5. Mengapa model pada Django disebut sebagai *ORM*?
