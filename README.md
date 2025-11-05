# Panduan
## Hal yang harus diketahui
1. Apps yang baru bisa berjalan adalah apps/maps/static/static_base (static_base)
2. Untuk mengakses halaman map di django nya, bisa diakses di localhost/static_map
3. Ada beberapa hal yang harus di setup

## Setup repository ini
1. Lakukan cloning seperti biasa
2. Buat venv di folder repository ini (yang ada manage.py)
3. Aktifkan venv
4. install package yang diperlukan
```
pip install -r requirements.txt
```
5. Buat file .env di folder repository (yang ada manage.py)
6. Silakan kontak pemilik repository untuk secret_keynya. Berikut adalah contoh bentuk .env
```python
SECRET_KEY = "YOUR-SECRET-KEY"
DEBUG=True
DATABASE_URL="postgres://user_postgis:pass_postgis@localhost:5432/main_postgis"
```

## Setup database postgresql (postgis)
1. Instalasi postgresql
```
sudo apt install postgresql
sudo apt-get install postgis postgresql-16-postgis-3
```
2. Masuk user postgre di ubuntu
```
sudo -i -u postgres #Masuk user postgres di Ubuntu
```
3. Masuk database postgres
```
psql -U postgres
```
4. Buat user, pass, dan database serta pengaturan permission (pembuatannya disesuaikan dengan DATABASE_URL di .env)
```
CREATE USER user_postgis WITH PASSWORD 'pass_postgis';
ALTER ROLE user_postgis SET client_encoding TO 'utf8';
ALTER ROLE user_postgis SET default_transaction_isolation TO 'read committed';
ALTER ROLE user_postgis SET timezone TO 'UTC';
CREATE DATABASE main_postgis OWNER user_postgis;
GRANT ALL PRIVILEGES ON DATABASE main_postgis TO user_postgis;
```
5. Masuk ke database yang telah dibuat
```
\c mydatabase_postgis
```
7. Instalasi postgis
```
CREATE EXTENSION postgis;
```

## Setup static_base (letaknya di apps/maps/static/static_base)
1. Kosongkan models/gis_models.py
2. Hapus append list dari model-model di models/__init__py
3. Hapus register model-model yang sudah dihapus pada models/gis_models.py dan models/__init__.py di admin.py
4. Sesuaikan nama env python di insert_shp_to_database.sh (dan mungkin step lainnya)
5. Silakan gunakan insert_shp_to_database.sh untuk menulis, register dan upload data shp
6. Contoh penggunaan insert_shp_to_database.sh -> source insert_shp_to_database.sh "[nama model di python]" "[nama_model_di_admin]" "[path_beserta_nama_ke_file_shp]"
```
source insert_shp_to_database.sh "AlurPelayaran" "Alur Pelayaran" "/home/fhs/datashp/01_ALUR_PELAYARAN.shp"
```
