#python3 manage.py dumpdata --indent 4 library > library.json

CREATE DATABASE librarydb;
USE librarydb;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
SELECT User, Host, authentication_string FROM mysql.user;
GRANT ALL PRIVILEGES ON librarydb.* to root@localhost;
FLUSH PRIVILEGES;

#python3 manage.py migrate
#python3 manage.py loaddata library.json
