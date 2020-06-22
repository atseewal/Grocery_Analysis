--Create the database
CREATE DATABASE grocery;

--Create user
CREATE USER 'analysisadmin'@'192.168.1.XXX' IDENTIFIED BY 'password1';

--Grant analysisadmin rights to grocery db
GRANT ALL PRIVILEGES ON grocery.* TO 'analysisadmin'@'192.168.1.XXX';
FLUSH PRIVILEGES;
