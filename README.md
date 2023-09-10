# Tugas 2 :v:

:sparkles: Nama: Kilau Nisrina Akhyaari 

:dvd: Kelas: PBP E

:iphone: Nama Aplikasi: :coat::jeans: [My Wardrobe]([url](https://mywardrobe.adaptable.app)) :dress::scarf:


## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Membuat sebuah proyek Django baru.
    Pertama, untuk membuat proyek Django baru, saya membuat repositori lokal bernama MyWardrobe di laptop saya. Lalu, saya membuat _virtual environment_ pada direktori tersebut untuk mengatur _package_ dan _dependancies_. Kemudian, saya memasang _dependencies_ yang diperlukan dalam requirements.txt dalam _virtual environment_. Lalu, saya membuat proyek Django dengan cara memasukkan 'django-admin startproject MyWardrobe .' pada terminal. Terakhir, saya mengkonfigurasi dan mengaktifkan server.

- Membuat aplikasi dengan nama main pada proyek tersebut.
    Untuk membuat aplikasi main, saya memasukkan perintah 'python manage.py startapp main' ke terminal. Lalu, saya menambahkan **"main"** ke settings agar terdaftar ke proyek.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Untuk mengakses aplikasi main melalui web, perlu dilakukan routing URL. Saya mengatur file urls.py yang berada di direktori proyek agar terhubung. Dalam kata lain, mengarahkan url-url yang secara umum terkait dengan seluruh proyek, bukan hanya satu aplikasi. Step ini penting untuk menghubungkan file urls pada aplikasi dan memungkinkan proyek modular dan terpisah antaraplikasi.

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib name, amount, description.
    Pada file models.py saya membuat class Item yang berisi 'name' bertipe CharField, 'amount' bertipe IntegerField, 'description' bertipe TextField, dan 'color' bertipe TextField. Lalu, saya migrasi modelnya untuk memastikan bahwa skema basis data tetap sejalan dengan definisi model-model aplikasi pada proyek dan membantu menjaga konsistensi data dalam aplikasi.

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Saya menghubungkan view dengan template dengan cara mengintegrasikan komponen MVT. Pada file views.py di main saya membuat fungsi 'show_main' dan menambahkan context app, name, dan class untuk dipakai dalam template.
    Lalu, karena sudah ada context yang berisi dictionary data yang diperlukan, saya mengubah file main.html saya untuk menggunakan variabel yang telah didefinisikan. 

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Saya membuat file urls.py dalam direktori main yang berisi komponen penting dalam pengaturan aplikasi Django. Saya mendefinisikan app_name menjadi 'main' dan urlpatterns agar mengarah ke path show_main. Step ini memungkinkan URL proyek terarah ke tampilan yang sesuai dengan fitur-fitur di dalam aplikasi.

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Saya membuat app baru di Adaptable dengan menghubungkannya ke repositori GitHub My-Wardrobe. Saya memilih Python Template App dan PostgreSQL untuk template dan tipe basis data. Lalu, saya memastikan versi python sudah sesuai dengan yang ada di aplikasi dan di bagian start command saya memasukkan 'python manage.py migrate && gunicorn shopping_list.wsgi' ntuk memastikan bahwa struktur basis data sesuai dengan definisi model-model aplikasi. Lalu saya mendeploy aplikasi saya agar aktif dan bisa diaskes di internet.

## 2. Alur Permintaan dan Respon dalam Aplikasi 
   _Request_
       ↓
   _URLs_
       ↓
   _Views_ ↔ _Models_ ↔ _Database_
       ↓
   _Template_
       ↓
   _Response_
       ↓
   _Client_

   **Penjelasan:** 
   Permintaan HTTP dari klien/user pertama-tama akan mencapai file urls.py. File urls.py mengandung pengaturan untuk mengarahkan URL ke tampilan (views) yang sesuai. Pada tahap ini, Django mencocokkan URL yang diterima dari permintaan dengan pola URL yang telah didefinisikan dalam file urls.py.

   Setelah URL cocok dengan pola yang ada dalam berkas urls.py, permintaan akan diteruskan ke tampilan yang sesuai dalam berkas views.py.

   Lalu, jika diperlukan akses ke model-model yang didefinisikan dalam berkas models.py aplikasi. Jika tampilan membutuhkan data dari basis data, mereka akan memanggil query ke model-model ini.

   Ketika views melakukan query ke model-model ini, Django akan menghasilkan SQL yang sesuai dan mengirimkannya ke database. Database akan mengembalikan hasil dari query tersebut ke Django, yang kemudian akan membentuknya menjadi objek Python yang dapat digunakan dalam views.

   Setelah tampilan selesai memproses permintaan dan mendapatkan data yang dibutuhkan, selanjutnya views akan dirender menggunakan template HTML.

   Hasil proses yang disiapkan dalam template HTML akan dikirimkan sebagai respons HTTP kepada klien (pengguna). Respons ini berisi HTML yang akan ditampilkan di browser pengguna, bersama dengan semua elemen seperti gambar, teks, dan data lain yang telah diproses.

   Akhirnya, respons yang dihasilkan akan diterima oleh klien (pengguna), yang akan melihat dan berinteraksi dengan halaman web yang dihasilkan.
   
## 3. Mengapa kita menggunakan virtual environment?
Menggunakan virtual environment adalah _best practice_ yang sangat disarankan dalam pengembangan aplikasi web berbasis Django dan pengembangan perangkat lunak Python pada umumnya. _Virtual environment_ dibuat di atas instalasi Python yang sudah ada, yang dikenal sebagai _virtual environment's base Python_, dan secara opsional dapat diisolasi dari paket-paket di lingkungan dasar, sehingga hanya paket-paket yang diinstal secara eksplisit di lingkungan virtual yang tersedia. 
    _Virtual environment_ seperti kamar pribadi di rumah. Kita bisa melakukan apa saja seperti membuat proyek, menginstal paket lama dari paket yang sudah ada, dan sebagainya. Aktivitas apa pun tidak akan memengaruhi atau mengganggu file atau proyek lain di komputer.

**Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
    Kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, sangat dianjurkan menggunakan virtual environment untuk menjaga kebersihan, isolasi, dan manajemen dependensi yang lebih baik dalam pengembangan proyek. Dengan virtual environment, kita bisa memastikan bahwa proyek memiliki lingkungan yang independen dan terisolasi dari proyek-proyek lain.

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
1. **MVC** atau **Model View Controller** adalah pola arsitektur dalam membuat sebuah aplikasi dengan cara memisahkan kode menjadi tiga bagian yang terdiri dari:
        - _Model_: Kode dalam model biasanya mencerminkan hal-hal di dunia nyata. Kode ini dapat menyimpan draw data, atau akan menentukan komponen penting aplikasi.
        - _View_: Kode view berisi semua fungsi yang berinteraksi langsung dengan user atau user interface. Ini adalah kode yang membuat aplikasi terlihat bagus, dan menentukan cara user melihat dan berinteraksi dengannya.
        - _Controller_: Kode controller berperan sebagai penghubung antara model dan view, menerima masukan user dan memutuskan apa yang harus dilakukan dengannya. Ini adalah otak dari aplikasi, dan menyatukan model dan view.

2. **MVT** atau **Model View Template** adalah turunan dari MVC. Namun, controller diatur framework itu sendiri. 
        - _Model_: Berperan sebagai interface untuk data. Merupakan struktur logis di balik seluruh aplikasi web yang diwakili oleh database seperti MySql, PostgreSQL. 
        - _View_: Menjalankan logika bisnis dan berinteraksi dengan Model serta merender template. View menerima permintaan HTTP dan kemudian mengembalikan respons HTTP.
        - _Template_: Template bertindak sebagai lapisan presentasi dan pada dasarnya adalah kode HTML yang merender data. Konten dalam file-file ini dapat bersifat statis atau dinamis.

**MVVM** atau **Model View ViewModel** adalah pola arsitektur yang mengatasi semua kelemahan pola desain MVP dan MVC. MVVM menyarankan untuk memisahkan logika presentasi data (View atau user interface) dari bagian logika bisnis inti aplikasi.
        - _Model_: Mengatur abstraksi sumber data. Model dan ViewModel bekerja sama untuk mendapatkan dan menyimpan data.
        - _View_: Menginformasikan ViewModel tentang tindakan user. Lapisan ini mengamati ViewModel dan tidak mengandung logika aplikasi apa pun.
        - _ViewModel_: Ini memperlihatkan aliran data yang relevan dengan View. Selain itu, ViewModel berfungsi sebagai penghubung antara Model dan View.
        
**Perbedaan utama dari ketiganya adalah dari hubungan komponen-komponennya;**

* Dalam MVC, View dan Model sangat erat kaitannya. Controller dan View mempunyai hubungan satu ke banyak. Satu controller dapat memilih View berbeda berdasarkan operasi yang diperlukan. 
* Dalam MVT, bagian pengontrol dikelola oleh framework itu sendiri. Sehingga, hubungan antarkomponen longgar dan mudah untuk membuat modifikasi. 
* Dalam MVVM, pola arsitektur ini lebih event-driven karena menggunakan data binding sehingga memudahkan pemisahan logika bisnis inti dengan View. Beberapa View dapat dipetakan dengan satu ViewModel, hubungan satu-ke-banyak terjadi antara View dan ViewModel.

**Lalu, bagian-bagian yang bertindak sebagai pengontrol berbeda-beda komunikasinya;**

- MVC mempunyai controller yang mengatur model dan view, lalu view yang menjalankan bagaimana data user akan ditampilkan, namun, view tidak mempunyai pengetahuan tentang controller. 
- MVT mempunyai view untuk menerima request HTTP dan mengembalikan respons HTTP, template yang mengatur bagaimana data user akan ditampilkan. 
- Pada MVVM, View mempunyai referensi ke ViewModel, View berperan mengambil user input dan bertindak sebagai titik masuk aplikasi.

**Penggunaan dan unit testing ketiga pola arsitektur juga berbeda;**

+ MVC cocok untuk proyek skala kecil saja dan memiliki support yang terbatas untuk unit testing.
+ MVT cocok untuk proyek dengan berbagai tingkat kompleksitas. Django menggunakan pola MVT.
+ MVVM cocok untuk proyek berskala besar. Biasanya digunakan untuk aplikasi berbasis User Interface, terutama aplikasi seluler dan desktop yang memiliki tampilan yang kompleks. Ketersediaan unit testing tertinggi untuk pola arsitektur ini. 

Setiap pola arsitektur memiliki tujuan yang sama, yaitu memisahkan komponen-komponen utama dalam pengembangan perangkat lunak untuk membuat kode lebih terstruktur, mudah dipelihara, dan memungkinkan perubahan tanpa mengganggu bagian lain dari aplikasi.

:full_moon_with_face:
