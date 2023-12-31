# Tugas 2 :v:

:sparkles: Nama: Kilau Nisrina Akhyaari 

:label: NPM: 2206082051

:dvd: Kelas: PBP E

:iphone: Nama Aplikasi: :coat::jeans: [My Wardrobe](https://mywardrobe.adaptable.app/main/) :dress::scarf:


## 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step :card_index_dividers:
### **- Membuat sebuah proyek Django baru.** 
Pertama, untuk membuat proyek Django baru, saya membuat repositori lokal bernama MyWardrobe di laptop saya. Lalu, saya membuat _virtual environment_ pada direktori tersebut untuk mengatur _package_ dan _dependancies_. Kemudian, saya memasang _dependencies_ yang diperlukan dalam requirements.txt dalam _virtual environment_. Lalu, saya membuat proyek Django dengan cara memasukkan ` django-admin startproject MyWardrobe . ` pada terminal. Terakhir, saya mengkonfigurasi dan mengaktifkan server.

### **- Membuat aplikasi dengan nama main pada proyek tersebut.**
Untuk membuat aplikasi main, saya memasukkan perintah ` python manage.py startapp main ` ke terminal. Lalu, saya menambahkan `main` ke settings agar terdaftar ke proyek.

### **- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.**
Untuk mengakses aplikasi main melalui web, perlu dilakukan routing URL. Saya mengatur file urls.py yang berada di direktori proyek agar terhubung. Dalam kata lain, mengarahkan url-url yang secara umum terkait dengan seluruh proyek, bukan hanya satu aplikasi. Step ini penting untuk menghubungkan file urls pada aplikasi dan memungkinkan proyek modular dan terpisah antaraplikasi.

### **- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib name, amount, description.**
Pada file models.py saya membuat class Item yang berisi `name` bertipe **CharField**, `amount` bertipe **IntegerField**, `description` bertipe **TextField**, dan  `in_laundry` bertipe **BooleanField**. Lalu, saya migrasi modelnya untuk memastikan bahwa skema basis data tetap sejalan dengan definisi model-model aplikasi pada proyek dan membantu menjaga konsistensi data dalam aplikasi.

### **- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
Saya menghubungkan view dengan template dengan cara mengintegrasikan komponen MVT. Pada file `views.py` di main saya membuat fungsi `show_main` dan menambahkan context app, name, dan class untuk dipakai dalam template.
Lalu, karena sudah ada context yang berisi dictionary data yang diperlukan, saya mengubah file main.html saya untuk menggunakan variabel yang telah didefinisikan. 

### **- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
Saya membuat file urls.py dalam direktori main yang berisi komponen penting dalam pengaturan aplikasi Django. Saya mendefinisikan app_name menjadi `main` dan urlpatterns agar mengarah ke path `show_main`. Step ini memungkinkan URL proyek terarah ke tampilan yang sesuai dengan fitur-fitur di dalam aplikasi.

### **- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
Saya membuat app baru di Adaptable dengan menghubungkannya ke repositori GitHub My-Wardrobe. Saya memilih Python Template App dan PostgreSQL untuk template dan tipe basis data. Lalu, saya memastikan versi python sudah sesuai dengan yang ada di aplikasi dan di bagian start command saya memasukkan `python manage.py migrate && gunicorn MyWardrobe.wsgi` ntuk memastikan bahwa struktur basis data sesuai dengan definisi model-model aplikasi. Lalu saya mendeploy aplikasi saya agar aktif dan bisa diaskes di internet.


## 2.  Alur Permintaan dan Respon dalam Aplikasi :arrows_counterclockwise:
  
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

![Alur Permintaan dan Respon dalam Aplikasi Django](images/Pola_Django.jpg)

   **Penjelasan:** :memo:
   
   Permintaan HTTP dari klien/user pertama-tama akan mencapai file urls.py. File urls.py mengandung pengaturan untuk mengarahkan URL ke tampilan (views) yang sesuai. Pada tahap ini, Django mencocokkan URL yang diterima dari permintaan dengan pola URL yang telah didefinisikan dalam file urls.py.

   Setelah URL cocok dengan pola yang ada dalam berkas urls.py, permintaan akan diteruskan ke tampilan yang sesuai dalam berkas views.py.

   Lalu, jika diperlukan akses ke model-model yang didefinisikan dalam berkas models.py aplikasi. Jika tampilan membutuhkan data dari basis data, mereka akan memanggil query ke model-model ini.

   Ketika views melakukan query ke model-model ini, Django akan menghasilkan SQL yang sesuai dan mengirimkannya ke database. Database akan mengembalikan hasil dari query tersebut ke Django, yang kemudian akan membentuknya menjadi objek Python yang dapat digunakan dalam views.

   Setelah tampilan selesai memproses permintaan dan mendapatkan data yang dibutuhkan, selanjutnya views akan dirender menggunakan template HTML.

   Hasil proses yang disiapkan dalam template HTML akan dikirimkan sebagai respons HTTP kepada klien (pengguna). Respons ini berisi HTML yang akan ditampilkan di browser pengguna, bersama dengan semua elemen seperti gambar, teks, dan data lain yang telah diproses.

   Akhirnya, respons yang dihasilkan akan diterima oleh klien (pengguna), yang akan melihat dan berinteraksi dengan halaman web yang dihasilkan.
   
   
## 3.  Mengapa kita menggunakan virtual environment? :computer:
Menggunakan virtual environment adalah _best practice_ yang sangat disarankan dalam pengembangan aplikasi web berbasis Django dan pengembangan perangkat lunak Python pada umumnya. _Virtual environment_ dibuat di atas instalasi Python yang sudah ada, yang dikenal sebagai _virtual environment's base Python_, dan secara opsional dapat diisolasi dari paket-paket di lingkungan dasar, sehingga hanya paket-paket yang diinstal secara eksplisit di lingkungan virtual yang tersedia. 
    _Virtual environment_ seperti kamar pribadi di rumah. Kita bisa melakukan apa saja seperti membuat proyek, menginstal paket lama dari paket yang sudah ada, dan sebagainya. Aktivitas apa pun tidak akan memengaruhi atau mengganggu file atau proyek lain di komputer.

**Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
    Kita bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, sangat dianjurkan menggunakan virtual environment untuk menjaga kebersihan, isolasi, dan manajemen dependensi yang lebih baik dalam pengembangan proyek. Dengan virtual environment, kita bisa memastikan bahwa proyek memiliki lingkungan yang independen dan terisolasi dari proyek-proyek lain.


## 4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. :floppy_disk:
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


# Tugas :three:


## 1. Membuat input form untuk menambahkan objek model pada app sebelumnya. 
Untuk membuat form, agar aplikasi saya bisa digunakan untuk menginput Item berikut adalah step-stepnya:
* Membuat file `forms.py` di direktori main
Isi file tersebut adalah import ModelForm dari django.forms dan import Product dari main.models.
Lalu, saya membuat class ProductForm yang menerima parameter ModelForm, di dalamnya terdapat class Meta dengan `fields = "name", "amount", "description", dan "in laundry"`.
* Menambahkan import di file `views.py` yang berada di folder main.
Saya menambahkan import HttpResponseRedirect, ProductForm, dan reverse.
* Membuat fungsi `create_product` di dalam file `views.py` tersebut.
  Fungsi ini bertujuan agar bisa membuat formulir yang dapat menambahkan data produk ke dalam database secara otomatis ketika pengguna mengirimkan data melalui formulir.
* Mengubah fungsi `show_main` untuk mengambil semua object Product yang ada di database
  Caranya dengan menambahkan `'products': products` di dalam variable `context`.
* Mengimport fungsi `create_product` ke file `urls.py` di dalam folder main.
  Saya menambahkan import `create_product` dari `main.views`.
* Menambahkan path url yang sesuai
  Saya membuat path baru
  ```python
  path('create-product', create_product, name='create_product'),
  ```
* Membuat file HTML baru bernama `create_product.html` pada direktori main dalam folder templates.
  Saya membuat tabel untuk menunjukkan data yang tersimpan di database.
* Menambahkan kode di file `main.html` untuk menampilkan data product yang telah di input
  Untuk melakukan hal tersebut, saya menambahkan kode:
  ```html
  <table>
    <tr>
        <th>Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.description}}</td>
            <td>{{product.date_added}}</td>
        </tr>
    {% endfor %}
  </table>
  ```
Lalu, saya membuaat button untuk menambahkan product dan diarahkan ke url create_product.
```html
<a href="{% url 'main:create_product' %}">
    <button>
        Add New Product
    </button>
</a>
```

## 2. Menambahkan fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Saya menambahkan kode berikut dalam file `views.py` yang berada di main.
```python
def show_main(request):
    items = Product.objects.all()

    context = {
        'items': items
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
Dengan lima fungsi views ini, kita dapat melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID di aplikasi Django `MyWardrobe`.

## 3. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Routing URL memungkinkan aplikasi untuk menghubungkan URL tertentu dengan view yang sesuai. Ketika user mengakses URL tertentu, Django akan menggunakan routing URL untuk menentukan view yang harus dipanggil.
Pada file `urls.py` pada direktori main, saya menambahkan kode berikut:
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Pertanyaan :grey_question:
### 1. Apa perbedaan antara form POST dan form GET dalam Django?
**GET** biasanya digunakan untuk operasi yang aman dan _read-only_ di mana data dapat terlihat di URL dan dibagikan dengan mudah. GET menggabungkan data yang dikirimkan ke dalam string, lalu menggunakannya untuk membuat URL yang berisi alamat tujuan pengiriman data, serta _key_ dan _value_ data.
**POST** digunakan untuk operasi yang mengubah status server atau melibatkan data sensitif dan di mana data tidak boleh diekspos di URL. POST memiliki perlindungan CSRF Django yang memungkinkan kontrol lebih terhadap akses.

Post cocok digunakan untuk login form, karena biasanya untuk login perlu password. Password adalah hal yang sensitif, sehingga seharusnya tidak ditampilkan dalam url.
Sedangkan GET cocok untuk _web search form_, karena URL yang terkait dengan permintaan GET dapat dengan mudah di-_bookmark_, di-_share_, atau digunakan kembali.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

* **HTML (HyperText Markup Language)**
**HTML** adalah dasar pengembangan web dan digunakan untuk menentukan struktur halaman. HTML digunakan untuk menjelaskan bagaimana data ditampilkan. HTML digunakan browser web untuk menafsirkan dan menyusun teks, gambar, dan materi lainnya ke dalam halaman web yang _visible_ atau _audible_.

* **JSON (JavaScript Object Notation)**
**JSON** digunakan untuk menyimpan dan mengirimkan data. JSON adalah cara untuk merepresentasikan objek. JSON adalah format pertukaran data yang berbasis teks dan terdiri dari pasangan _key-value_. File JSON lebih mudah dibaca daripada XML, karena lebih ringkas. 

* **XML (eXtensible Markup Language)**
**XML** digunakan untuk merepresentasikan data dengan cara yang dapat dibaca mesin. XML adalah bahasa markup yang fleksibel dan memungkinkan definisi struktur data yang kompleks. XML menggunakan struktur _tag_ untuk mewakili item data.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON umumnya digunakan untuk _serialization_ dan mengirimkan data melalui koneksi jaringan seperti internet. Penggunaan JSON terutama untuk mengirimkan data antara server dan aplikasi web. JSON mendapatkan momentum dalam _API code programming_ dan layanan web karena membantu pertukaran data dan hasil layanan web yang cepat. JSON berbasis teks, ringan, dan memiliki format data yang _easy to parse_ sehingga tidak memerlukan kode tambahan untuk _parsing_/penguraian.

## POSTMAN :postbox:
**Postman Screenshot for HTML (main)**
![Postman HTML](PostmanSS/Postman_JSON_ID.png)

**Postman Screenshot for XML**
![Postman XML](PostmanSS/Postman_XML.png)

**Postman Screenshot for XML by ID**
![Postman XML by ID](PostmanSS/Postman_XML_ID.png)

**Postman Screenshot for JSON**
![Postman XML](PostmanSS/Postman_JSON.png)

**Postman Screenshot for JSON by ID**
![Postman JSON by ID](PostmanSS/Postman_JSON_ID.png)

:new_moon_with_face:


# Tugas :four:

## 1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
Fungsi `registrasi` memungkinkan user baru untuk membuat akun di aplikasi. Fungsi `login` memungkinkan user yang telah terdaftar untuk masuk ke dalam akun mereka. Fungsi `logout` memungkinkan pengguna untuk keluar dari akun mereka dan mengakhiri sesi mereka.

Pertama, pada file `views.py` dalam direktori `main` saya mengimport redirect, UserCreationForm, messages, authenticate, login, dan logout. 
`redirect`: Mengarahkan pengguna ke halaman lain dalam aplikasi web.
`UserCreationFor`m: Formulir bawaan Django untuk membuat akun pengguna.
`messages`: Modul untuk menampilkan pesan kepada pengguna dalam aplikasi web.
`authenticate`: Fungsi untuk mengotentikasi pengguna dalam Django.
`login`: Fungsi untuk masukkan pengguna dalam Django.
`logout`: Fungsi untuk keluarkan pengguna dari sesi dalam Django.

Lalu, saya menambahkan beberapa fungsi di dalam file `views.py` dalam direktori `main`, yaitu: 
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Setelah itu, di direktori `main` > `templates` saya membuat file html baru bernama `register.html` yang berisi form registrasi yang akan mengambil input dari user, mengirimkannya melalui metode POST, dan juga menampilkan pesan-pesan kepada user. Saya juga menghias page tersebut dengan menambahkan `style` di file html tersebut. 

Saya juga membuat file `login.html` dalam direktori `main` > `templates`. File ini berfungsi sebagai halaman login dalam sebuah aplikasi web. Halaman ini memuat  form login yang mengambil input username dan password dari user. Ketika formulir ini di-_submit_, data akan dikirimkan dengan metode POST. Halaman juga menampilkan pesan-pesan kepada user jika terdapat pesan-pesan yang perlu ditampilkan, seperti pesan kesalahan saat login gagal. Terakhir, halaman ini menyertakan tautan untuk menuju halaman registrasi jika user belum memiliki akun, dengan menggunakan tautan yang mengarah ke URL untuk halaman register.

Untuk logout, saya hanya menambahkan button `logout` pada `main.html`. Saya juga membuat halaman main terbatas penggunaannya dengan menambahkan `login_required` pada file `views.py` di direktori `main`.

Di file `urls.py` saya menambahkan import `register`, `login_user`, dan `logout_user`.
Saya juga menambahkan path-path yang sesuai pada urlpatterns;
```
path('register/', register, name='register'), 
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
```

## 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Untuk bagian ini, saya melakukan registrasi 2 kali dengan nama akun yang berbeda. Lalu, saya login dan menambahkan 3 _clothing item_ di aplikasi saya. Saya lalukan hal yang sama untuk akun kedua saya dengan data yang berbeda.

## 3. Menghubungkan model Item dengan User.
Pertama, pada file `models.py` di direktori `main`, saya meng-_import_ `User`. Dengan meng-_import_ `User`, aplikasi saya bisa digunakan untuk membuat, mengelola, dan mengautentikasi akun user. Saya juga menggunakannya sebagai referensi saat menampilkan data milik user.
Lalu, saya menambahkan kode
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
untuk menghubungkan objek dalam model saat ini dengan objek dalam model `User` dari Django. Opsi `on_delete=models.CASCADE` menentukan bahwa ketika objek User terkait dihapus, objek dalam model saat ini yang menggunakan _foreign key_ tersebut juga akan dihapus secara otomatis untuk menjaga konsistensi dalam database.

Setelah itu, dalam fungsi `create_product` dalam file `views.py` dalam main, saya memodifikasi fungsinya dengan menyisipkan
```
if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))
```
untuk memproses data dari form, menghubungkannya dengan user yang login saat ini, menyimpannya ke dalam database, dan mengarahkan user ke halaman main setelah berhasil tersimpan.
Dalam fungsi `show_main` saya mengubah _value_ context nama menjadi `request.user.username` untuk menyesuaikan user yang login. Tidak lupa, saya menambahkan `items = Item.objects.filter(user=request.user)` untuk hanya menampilkan data dari user spesifik yang sedang login.

Terakhir, saya melakukan migrasi untuk menyimpan perubahan data.

## 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
Pada file `models.py`, saya membuat relasi antara item dengan _foreign key_. Caranya dengan menambahkan kode
```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```
_ForeignKey_ digunakan untuk menyambungkan suatu objek dengan objek lain, dalam konteks ini menghubungkan setiap item dengan user yang membuatnya.

Untuk menampilkan siapa yang sedang login dalam aplikasi, saya memodifikasi fungsi `show_main` dengan cara mengubah _value_ context nama menjadi `request.user.username` untuk menyesuaikan user yang login.

Untuk menampilkan data _last login_ pada aplikasi, pertama-tama saya mengimport `datetime` di file `views.py` dalam `main`. 
Lalu, saya memodifikasi kode saya bagian `login_user` menjadi
```python
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
Bagian ini untuk memproses login user dalam aplikasi web yang melibatkan otentikasi, pengaturan sesi, mengirim cookie, dan mengarahkan user ke halaman yang sesuai.
Lalu, tidak lupa saya menambahkan `context` pada fungsi `show_main` dengan menambahkan 
```python
'last_login': request.COOKIES['last_login'],
```
Lalu, di bagian fungsi `logout_user` saya menambahkan baris kode
```python
response = HttpResponseRedirect(reverse('main:login'))
response.delete_cookie('last_login')
```
untuk menghapus data cookie pengguna yang baru saja logout.

Pada file `main.html` saya menggunakan context `last_login` dengan cara
```html
<h5>Last entered MyWardrobe: {{ last_login }}</h5>
```
untuk memberikan informasi user yang sedang login.

## Pertanyaan :grey_question: 
### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
**Django UserCreationForm** adalah kelas `form` bawaan yang disediakan oleh _user authentication system_ Django. Kelas ini digunakan untuk memfasilitasi pembuatan akun user baru dalam aplikasi Django. Form ini turunan kelas ModelForm, yang memungkinkan pengembang pembuatan formulir untuk registrasi user. **UserCreationForm** menyederhanakan proses pengumpulan dan validasi data pendaftaran user seperti nama user dan password. Sehingga, membuatnya lebih mudah untuk menerapkan fungsi registrasi user dalam proyek Django.

Kelebihan **UserCreationForm** adalah aspek _security_ dan _reliability_. Django memiliki _middleware_ pengelolaan kata sandi yang substansial dengan model `User`. Sistem password defaultnya saja sudah memberikan keamanan yang kuat tanpa upaya apa pun dari __developer__. 
Kelebihan lainnya adalah fitur yang mengharuskan _username_ yang dibuat user unik. Syarat keunikan ini diproses pada tingkat database, tetapi diverifikasi ulang oleh form yang disediakan Django.
Kekurangan kelas ini adalah tidak mudah untuk memodifikasi data fields seperti menghapus atau menambahkan data. _Framework UserCreationForm_ juga tidak mendukung perubahan. Model User generik dibuat di database aplikasi secara default selama pembuatan proyek Django baru. Ada banyak hal yang terikat dengan model user default sehingga mengubahnya dapat menimbulkan efek yang tidak terduga pada aplikasi, terutama jika menggunakan _thir party libraries_.

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
* Autentikasi memverifikasi bahwa si user adalah siapa yang diklaim sebagai "user", dan otorisasi menentukan apa yang bisa diakses oleh user yang diautentikasi.
* Dalam autentikasi, user di-_verifikasi_. Sedangkan proses autorisasi mem-_validasi_ user.
* Proses yang pertama dilakukan adalah autentikasi, lalu autorisasi.
* Autentikasi user biasanya mengidentifikasi nama, password, dan biometrik. Otorisasi user dilakukan melalui pemberian hak akses sesuai dengan peran/tingkatan user.

Secara keseluruhan, **Autentikasi** dan **Otorisasi** digunakan dalam untuk keamanan data agar memungkinkan perlindungan sistem data secara otomatis. Oleh karena itu, keduanya sangat penting, terutama di era _big data_ ini.


### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
**Cookies** adalah _text file_ dengan potongan data seperti nama user dan password. _Cookie_ digunakan untuk membantu komputer mengidentifikasi user. Data yang disimpan dalam cookie dibuat oleh server pada koneksi user. Data ini diberi label dengan ID yang unik untuk user dan komputer user. Ketika terjadi pertukaran _cookie_ antara komputer user dan server jaringan, server membaca ID dan mengetahui informasi apa yang khusus disajikan untuk si user. _Cookie_ membantu _developer_ memberi user pengalaman yang dipersonalisasi. Cookie memungkinkan situs web mengingat user serta data-data user seperti isi keranjang belanja, halaman yang disimpan, dan lainnya.

Django menggunakan _cookie_ yang berisi id sesi unik untuk mengidentifikasi setiap browser dan sesi terkaitnya. Data sesi disimpan dalam database situs secara default. Framework _session_ di Django memungkinkan user menyimpan dan mengambil data sesuai user situs. Pada _request_ berikutnya, browser mengirimkan _sessionid cookie_ ke server. Django kemudian menggunakan _cookie_ ini untuk mengambil data sesi dan membuatnya dapat diakses di tempat lain.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Secara default, _cookie_ tidak berbahaya dalam pengembangan web. Namun, jika data cookie diakses orang yang mempunyai niat jahat seperti _cyberattacker_,mereka bisa mengakses sesi _search_, mencuri informasi pribadi, atau menyalahgunakan data cookie pengguna. 
Suatu website mungkin saja menjual data dari cookie ke pihak ketiga atau bisa saja menggunakannya untuk _hack_ akun user.
Sebaiknya, kita tidak menerima cookie dari situs web yang _unsecure_. Kita juga bisa menolak penggunaan cookie. Sebagian besar website akan berfungsi dengan baik tanpa mengumpulkan informasi pribadi user melalui cookie. 

### Implementasi Bonus
Menambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu dan tombol fungsi untuk menghapus suatu objek dari inventori.

Saya memodifikasi table saya di main.html menjadi 
```html
<table>
        <tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Increase/Decrease</th> 
            <th>Description</th>
            <th>In Laundry?</th>
            <th>Delete</th> 
        </tr>
        {% for item in items %}
            <tr>
                <td>{{ item.name }}</td>
                <td>{{ item.amount }}</td>
                <td>
                    <!-- Increase and Decrease Buttons -->
                    <a href="{% url 'main:increase_amount' item.id %}">+</a>
                    <a href="{% url 'main:decrease_amount' item.id %}">-</a>
                </td>
                <td>{{ item.description }}</td>
                <td>{{ item.in_laundry }}</td>
                <!-- Delete Button -->
                <td><a href="{% url 'main:delete_item' item.id %}">Delete</a></td>
            </tr>
        {% endfor %}
    </table>
``` 

Lalu, saya menambahkan fungsi untuk melakukan increase/decrease amount dan delete item pada `views.py` saya di direktori main. Saya mengimport `get_object_or_404` dari django.shortcuts. 

```python
def increase_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_amount(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    if item.amount > 0:  
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id, user=request.user)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

Terakhir, saya mengkonfigurasi `urls.py` saya dalam direktori main agar fungsi-fungsi yang sudah saya buat bisa diintegrasikan. Saya mengimport `increase_amount, decrease_amount, delete_item` dari main.views dan menambahkan path-path berikut di dalam urlspatterns.

```python
    path('increase_amount/<int:item_id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:item_id>/', decrease_amount, name='decrease_amount'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
```

# Tugas :five:
## 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector CSS digunakan untuk memilih elemen HTML yang ingin diubah _style_-nya.
### Type/Element Selector
- Manfaat: Mengaplikasikan _style_ ke semua elemen dengan jenis tertentu.
- Digunakan ketika: Mengatur gaya default untuk elemen tertentu di seluruh halaman atau website. Misalnya, mengatur semua elemen `<p>` agar berwarna biru.
```html
p {
  color: blue;
}
```
### Class Selector
- Manfaat: Mengaplikasikan _style_ ke semua elemen yang memiliki kelas tertentu.
- Digunakan ketika: Mengatur _style_ khusus untuk sekelompok elemen tanpa mengubah elemen lain yang sejenis. Misalnya, beberapa elemen h1 akan berwarna merah hanya di kelas "login", sementara h1 lainnya tetap dengan warna default.
```html
.login {
  color: red;
}
```
### ID Selector
- Manfaat: Mengaplikasikan _style_ ke elemen yang memiliki ID tertentu.
- Digunakan ketika: Mengatur _style_ khusus untuk elemen dengan ID tertentu yang unik. Misalnya, mengatur elemen dengan id="test" agar mempunyai font yang bold.
```html
#test {
  font-weight: bold;
}
```
### Universal Selector
- Manfaat: Mengaplikasikan _style_ ke seluruh elemen di file html.
- Digunakan ketika: Mengatur _style_ yang akan dipakai di seluruh halaman html. Misalnya, semua font di halaman ingin diatur menjadi Verdana.
```html
* {
  font-family: Verdana;
}
```
### Grouping Selector
- Manfaat: Menggabungkan beberapa selector untuk menerapkan _style_ yang sama.
- Digunakan ketika: ingin memberi _style_ yang sama untuk beberapa elemen, agar tidak mengulang kode.
Misalnya, `<h1>`,`<h2>`, dan `<h3>` ingin menerapkan background color yang sama.
```html
h1, h2, h3 {
  background-color: white;
}
```
### Descendant Selector
- Manfaat: Mengaplikasikan _style_ berdasarkan hubungan keturunan elemen.
- Digunakan ketika: Mengatur _style_ untuk elemen yang berada di dalam elemen lain dan merupakan keturunan elemen tersebut. Misalnya, mengubah alignment teks elemen <h2> yang berada di dalam <footer>.
```html
footer h2 {
  text-align: center;
}
```
## 2. Jelaskan HTML5 Tag yang kamu ketahui.
* `<!DOCTYPE html>` : Mendefinisikan tipe dokumen dan versinya, defaultnya HTML5.
* `<a>` : Membuat hyperlink/anchor
* `<body>` : Mendefinisikan elemen "body"
* `<br>` : Break line, elemen setelahnya akan berada di baris berikutnya
* `<header>` : Menandakan konten header atau navigasi.
* `<img>` : Menandakan konten gambar
* `<link>` : Untuk memberi referensi sumber
* `<table>` : Menandakan tabel
* `<th>` : Menandakan header tabel
* `<td>` : Menandakan data pada tabel
* `<tr>` : Menandakan row tabel

## 3. Jelaskan perbedaan antara margin dan padding.
Dalam mendesign menggunakan CSS, margin dan padding adalah bagian dari **box model**.

![Box Model Layout](images/Box_Model_Illustration.png)

:green_square: **Padding** adalah ruang di antara konten dan border. Padding mendorong konten elemen agar menjauh dari batas elemennya. Padding tidak menyebabkan elemen lain bergeser karena hanya mempengaruhi ruang di dalam batas elemen. Warna padding menyesuaikan background color.

:purple_square: **Margin** adalah ruang di luar border. Margin mendorong elemen lain atau dinding kontainer agar menjauh dari elemen tersebut. Margin bisa menyebabkan elemen lain bergeser, karena margin mempengaruhi ruang di luar elemen. Warna margin selalu transparan.

## 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
**Bootstrap** adalah framework berbasis komponen. Bootstrap menyediakan sejumlah komponen desain yang telah jadi, seperti tombol, kartu, navigasi, modals, dan lain-lain, yang dapat digunakan langsung. Kustomisasi di Bootstrap memerlukan usaha yang banyak, karena banyak variabel yang perlu diubah untuk menyesuaikan keinginan.

**Tailwind** adalah framework berbasis utilitas. Tailwind memungkinkan pengembang untuk membuat desain dengan cepat melalui kelas utilitas kecil yang masing-masing mengendalikan satu aspek dari desain (seperti margin, padding, warna, dll). Kustomisasi dalam tailwind lebih mudah karena lebih fleksibel, tidak terikat gaya default dari framework.

:boot: Bootstrap lebih baik digunakan ketika:
- Menginginkan solusi cepat dengan komponen siap pakai.
- Pemula dalam design web.
- Proyek lebih berfokus pada backend, sehingga layout cukup menggunakan yang umum dan langsung bisa digunakan.

:wind_chime: Tailwind lebih baik digunakan ketika:
- Menginginkan fleksibilitas yang lebih.
- Ingin design yang unik dan tetap konsisten.
- Lebih nyaman dengan pendekatan utilitas dan ingin mengurangi jumlah CSS kustom.


### Kustomisasi

Saya menambahkan style-style menggunakan CSS dan beberapa komponen bootstrap. Saya mengkustomisasi halaman `create_product`, `add_item`, `login`, `main`, dan juga `register`.
Dalam `main.html` saya mengkustomisasi dengan menambahkan style berikut. 
```html
<style>
    body {
        font-family: Verdana, sans-serif;
        background-color: #DAB6C4;
        color: #4A7C59;
        text-align: center;
        margin: 20px;
    }

    h1 {
        font-family: Verdana, sans-serif;
        color: #A53860;
        text-align: center;
    }

    p {
        font-family: Verdana, sans-serif;
        color: #60435F;
    }

    table {
        font-family: Verdana, sans-serif;
        color: #60435F;
        margin: 20px;
    }

    table th {
        background-color: #A53860;
        color: #FFF0F5;
        font-weight: bold;
    }

    table th, table td {
        padding: 10px;
        border: 1px solid #A53860;
    }

    tbody tr:last-child {
        background-color: #F4C2C2;
    }

    button {
        font-family: Verdana, sans-serif;
        background-color: #60435F;
        color: #FFF0F5;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        border-radius: 5px;
        text-decoration: none;
        display: inline-block;
        margin: 5px;
    }

    button:hover {
        background-color: #A53860;
        color: #DAB6C4;
    }

    footer {
        font-family: Verdana, sans-serif;
        color: #4A7C59;
        background-color: #CAE7B9;
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 10px;
    }

    .btn-increase {
        background-color: #DE5D83;
        color: #FFFFFF; 
    }

    .btn-decrease {
        background-color: #C54B8C;
        color: #FFFFFF; 
    }

    .btn-delete {
        background-color: #DC143C;
        color: #FFFFFF;
    }

    .btn-increase:hover {
        background-color: #ACE1AF;
    }
    .btn-decrease:hover {
        background-color: #FADFAD
    }
    .btn-delete:hover {
        background-color: #C51E3A;
    }

    .btn-edit {
        background-color: #997A8D;
        color: #FFFFFF
    }
    .btn-edit:hover {
        background-color: #F2BDCD;
    }

    .navbar-brand {
        color: #A53860;
        font-weight: bold;
    }

</style>
```
Saya juga menambahkan navbar dan beberapa button dengan bootstrap.
:card_file_box:
```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            {{ app }}
        </a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" style="border: 1px solid #ddd;">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link" href="{% url 'main:create_product' %}">Create Product</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="{% url 'main:logout' %}">Logout</a>
              </li>
            </ul>
        </div>
    </div>
</nav>
```
:radio_button:
```html
<!-- Increase and Decrease Buttons with Bootstrap styling -->
<a href="{% url 'main:increase_amount' item.id %}" class="btn btn-sm btn-increase">+</a>
<a href="{% url 'main:decrease_amount' item.id %}" class="btn btn-sm btn-decrease">-</a>
```

Saya juga menambahkan fungsi `edit_item` yang berguna untuk mengedit Item yang sudah ada di MyWardrobe. Saya membuat fungsi ini dalam views.py dalam direktori main.
```python
def edit_item(request, id):
    item = Item.objects.get(pk = id)
    form = ProductForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "edit_item.html", context)
```
Saya juga menambahkan pathnya ke urlspattern dengan cara mengimport `edit_item` dan menambahkan path berikut:
`path('edit-item/<int:id>', edit_item, name='edit_item'),`


# Tugas :six:
*Step by Step*

Saya mengubah tabel saya agar mengimplementasikan cards. Lalu, untuk mengambil item saya menggunakan AJAX GET.
Berikut kode yang saya modifikasi:
`<table id="product_table"></table>` -> `<div id="item_cards"></div>`

Saya juga menambahkan _script_ pada `main.html` untuk menerapkan AJAX GET, untuk mengambil dan mengirim data ke server tanpa perlu memuat ulang satu halaman penuh seperti ini:
```javascript
<script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}")
            .then((res) => res.json());
    }
    
    async function refreshItems() {
        document.getElementById("item_cards").innerHTML = "";
        
        const items = await getItems();
        let htmlString = "";
        
        items.forEach((item) => {
            const increaseUrl = `{% url 'main:increase_amount' 999999 %}`.replace('999999', item.pk);
            const decreaseUrl = `{% url 'main:decrease_amount' 999999 %}`.replace('999999', item.pk);
            const deleteUrl = "{% url 'main:delete_item' 999999 %}".replace('999999', item.pk);
            const editUrl = "{% url 'main:edit_item' 999999 %}".replace('999999', item.pk);
            const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
            const formattedDate = new Date(item.fields.date_added).toLocaleDateString(undefined, dateOptions);

            
            htmlString += `
            <div class="card">
                <!-- You can add an image here if you have one -->
                <div class="card-body">
                    <h3 class="card-title">${item.fields.name}</h3>
                    <p class="card-text amount-display">Amount: ${item.fields.amount}</p>
                    <p class="card-text">${item.fields.description}</p>
                    <p class="card-text">In Laundry? ${item.fields.in_laundry}</p>
                    <button data-id="${item.pk}" class="btn btn-sm btn-increase">+</button>
                    <button data-id="${item.pk}" class="btn btn-sm btn-decrease">-</button>
                    <br>
                    <a href="${editUrl}" class="btn btn-sm btn-edit">Edit</a>
                    <a href="${deleteUrl}" class="btn btn-sm btn-delete">Delete</a>
                </div>
                <div class="card-footer text-muted">
                    Last Added: ${formattedDate}
                </div>
            </div>`;
        });
        
        document.getElementById("item_cards").innerHTML = htmlString;
    }    
</script>
```

Tidak lupa saya menambahkan path ke `urls.py` di main seperti ini:
```python
    path('get-item/', get_item_json, name='get_item_json'),
```

Implementasi AJAX Post saya terapkan untuk menambahkan item. pada `views.py` saya menambahkan fungsi ini:
```python
@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        in_laundry = request.POST.get("in_laundry") == "on"
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, in_laundry=in_laundry, user=user)
        new_item.save()

        data = {
            'id': new_item.pk,
            'name': new_item.name,
            'amount': new_item.amount,
            'description': new_item.description,
            'in_laundry': new_item.in_laundry
        }
        return JsonResponse(data)

    return HttpResponseNotFound()
```

Lalu pada front-end, pada `main.html` saya menambahkan _script_ berikut:
```javascript
function addItem() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#addItemForm'))
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to add item. Server responded with status: ' + response.status);
            }
        })
        .then(item => {
            const increaseUrl = `{% url 'main:increase_amount' 999999 %}`.replace('999999', item.id);
            const decreaseUrl = `{% url 'main:decrease_amount' 999999 %}`.replace('999999', item.id);
            const deleteUrl = "{% url 'main:delete_item' 999999 %}".replace('999999', item.id);
            const editUrl = "{% url 'main:edit_item' 999999 %}".replace('999999', item.id);
    
            const newCard = `
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${item.name}</h5>
                    <p class="card-text amount-display">Amount: ${item.amount}</p>
                    <p class="card-text">${item.description}</p>
                    <p class="card-text">In Laundry? ${item.in_laundry}</p>
                    <button data-id="${item.id}" class="btn btn-sm btn-increase">+</button>
                    <button data-id="${item.id}" class="btn btn-sm btn-decrease">-</button>
                    <br>
                    <a href="${editUrl}" class="btn btn-sm btn-edit">Edit</a>
                    <a href="${deleteUrl}" class="btn btn-sm btn-delete">Delete</a>
                </div>
            </div>`;
    
            document.getElementById("item_cards").insertAdjacentHTML('beforeend', newCard);
            // Close the modal
            $("#itemModal").modal('hide');
        })
        .catch(error => {
            console.error(error);
        });
    
        document.getElementById("addItemForm").reset();
        return false;
    }
    document.getElementById("button_add_item").onclick = addItem;
```
Tidak lupa saya menambahkan path ke `urls.py` di main seperti ini:
```python
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
```
Pengimplementasian AJAX Post ini mengirimkan POST request ke server dengan data dari addItemForm untuk menambahkan item baru. Respons server kemudian digunakan untuk menambahkan kartu baru untuk item tersebut ke halaman.

Semua implementasi fungsi-fungsi get dan post di atas menggunakan AJAX untuk berkomunikasi dengan server agar memungkinkan pengalaman pengguna yang dinamis dan lancar tanpa perlu memuat ulang halaman penuh.

Penerapan `collectstatic` saya lakukan dengan mengubah `settings.py` agar memuat kode berikut:
```py
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
Lalu, saya menjalankan `python manage.py collectstatic` pada terminal. 
`STATIC_URL` digunakan untuk menentukan bagaimana URL untuk file statis dibuat di template.
`STATIC_ROOT` digunakan untuk menentukan di mana semua file statis dikumpulkan ketika menjalankan perintah `collectstatic`. Hal ini sangat berguna untuk deployment.

## Pertanyaan :grey_question:
### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
*Synchronous Programming (Pemrograman Sinkron)*
Kode dijalankan langkah demi langkah. Satu tugas harus selesai sebelum tugas berikutnya dimulai. 
- Kelebihan: Mudah untuk dipahami dan didebug karena alur eksekusinya linear.
- Kekurangan: Bisa menjadi tidak efisien. Jika satu tugas membutuhkan waktu lama, maka seluruh program akan menunggu hingga tugas tersebut selesai.

*Asynchronous Programming (Pemrograman Asinkron)*
Beberapa tugas bisa dimulai dan dijalankan secara bersamaan tanpa menunggu tugas sebelumnya selesai.
- Kelebihan: Lebih efisien untuk operasi yang membutuhkan waktu lama, seperti I/O atau permintaan jaringan, karena program bisa melanjutkan pekerjaan lain sambil menunggu.
- Kekurangan: Lebih kompleks untuk dipahami dan didebug karena tugas-tugas bisa berjalan dalam urutan apa pun dan bisa menyelesaikan kapan saja.

_Synchronous Programming_ bagus untuk alur kerja yang sederhana dan linear, sedangkan _Asynchronous Programming_ ideal untuk tugas yang memerlukan banyak waktu atau untuk aplikasi yang perlu responsif dan cepat.

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma *event-driven programming* adalah pendekatan pemrograman di mana alur eksekusi program ditentukan oleh urutan kejadian (events) seperti input pengguna, sensor output, atau pesan dari program lain. Program event-driven dirancang untuk bereaksi terhadap kejadian tertentu.
Penerapan pada tugas saya:
```javascript
document.addEventListener('click', async function(e) {
    if (e.target && e.target.classList.contains('btn-increase')) {
        ...
    } else if (e.target && e.target.classList.contains('btn-decrease')) {
        ...
    }
});
```
Saya menggunakan _event-driven programming_ untuk menangani kejadian klik pada dokumen.

### 3. Jelaskan penerapan asynchronous programming pada AJAX.
Dalam konteks AJAX, asynchronous programming memungkinkan halaman web untuk meminta data dari server dan memperbarui bagian dari halaman tanpa harus memuat ulang halaman secara keseluruhan.
Penerapan _asynchronous programming_ dalam AJAX:
- Permintaan Asinkron: 
    Ketika sebuah permintaan AJAX dikirim, browser tidak perlu menunggu respons dari server untuk melanjutkan eksekusi kode lain. Ini berarti bahwa pengguna dapat terus berinteraksi dengan halaman sementara permintaan sedang diproses.
- Callback: 
    Setelah permintaan AJAX selesai (baik berhasil, gagal, atau timeout), sebuah fungsi callback dapat dipanggil. Fungsi ini mendefinisikan apa yang harus dilakukan setelah mendapatkan respons dari server. Dalam JavaScript modern, pendekatan seperti Promises dan async/await sering digunakan sebagai alternatif untuk callback tradisional, memberikan cara yang lebih bersih dan mudah dibaca untuk menangani operasi asinkron.
- Pembaruan Halaman: 
    Setelah mendapatkan respons dari server, halaman web dapat diperbarui secara dinamis tanpa perlu memuat ulang. Ini memungkinkan untuk pengalaman pengguna yang lebih cepat dan responsif.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
*Fetch API*
Fetch API adalah API asli yang ada di sebagian besar browser modern. Ini berarti Anda tidak perlu mengimpor library eksternal untuk menggunakannya. Fetch API menggunakan Promises, yang memungkinkan penanganan respons yang lebih bersih dan lebih mudah dibaca, terutama saat digunakan dengan async/await. Fetch API memberikan kontrol lebih atas permintaan, seperti memungkinkan manual pengaturan headers, mode, dan credentials. Beberapa pengembang mungkin merasa bahwa Fetch memiliki sintaks yang lebih intuitif dan modern dibandingkan dengan jQuery AJAX.

*jQuery AJAX*
Salah satu keuntungan utama menggunakan jQuery adalah kompatibilitas lintas browser. Meskipun browser modern mendukung Fetch API, browser lama mungkin tidak. jQuery menyediakan solusi AJAX yang bekerja di hampir semua browser. Untuk pengembang yang sudah terbiasa dengan jQuery, menggunakan AJAX melalui jQuery mungkin terasa lebih familiar. jQuery tidak hanya menyediakan AJAX, tetapi juga berbagai fitur lain yang memudahkan manipulasi DOM, animasi, dan lainnya. Menggunakan jQuery berarti menambahkan library eksternal ke proyek Anda, yang dapat meningkatkan ukuran total file yang harus diunduh oleh pengguna.
Untuk proyek-proyek baru yang tidak memerlukan dukungan browser lama, saya cenderung memilih Fetch API karena sifatnya yang native dan integrasinya yang baik dengan fitur JavaScript modern. Namun, keputusan akhir harus didasarkan pada kebutuhan spesifik proyek dan preferensi.
Jika sedang mengembangkan aplikasi web modern dan ingin mengurangi ketergantungan pada library eksternal, serta memanfaatkan fitur ES6+ seperti Promises dan async/await, maka Fetch API mungkin adalah pilihan yang lebih baik.
Namun, jika proyek sudah menggunakan jQuery atau memerlukan kompatibilitas lintas browser yang luas, terutama dengan browser lama, maka jQuery AJAX mungkin lebih sesuai.


