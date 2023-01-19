# CM-KP-2022
Aplikasi Monitoring CCTV Multivendor Berbasis Web

Yang diperlukan:
1. Python Latest Stable
2. Library Flask
3. Library Mysqldb
4. Xampp
5. Library Mysqldb.connector
6. Library OpenCV
7. Library Pandas

bisa diinstall dengan menjalankan pip install -r requirements.txt (pastikan python sudah terinstall terlebih dahulu)

How to Run?
1. Put all item in one Folder
2. Install XAMPP, run MySQL & Apache
3. Using browser go to localhost/phpmyadmin
4. Create new user with all permission
User : pep2
Password : l0gin@kses

or you can use your own sql account, just change it in auth.py, database_cctv.py and list_user.py files.

4. Make new database with name db-app-cctv then copy content in db-app-cctv.mysql file, paste and run in phpmyadmin SQL code section
5. Run main.py

Make sure you use same network with the cctv
testt