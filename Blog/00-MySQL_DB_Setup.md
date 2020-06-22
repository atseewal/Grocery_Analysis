Database Setup Steps:
Hardware
Raspberry Pi
etch raspberian to sd card
Install mariadb
edit 50-server.cnf file
--0.0.0.0
create database
--CREATE DATABASE grocery;
create database tables
--source create_tables.sql;
create user
--CREATE USER 'analysisadmin'@'192.168.1.XXX' IDENTIFIED BY 'password1';
--use IP address that user will be connecting from or '%' for any IP address
Grant user permissions on tables in database
--GRANT ALL PRIVILEGES ON grocery.* TO 'analysisadmin'@'192.168.1.XXX';
download ufw
--sudo apt install ufw
create firewall rules to allow mysql client to connect to the database
--sudo ufw allow from 192.168.1.XXX to any port 3306