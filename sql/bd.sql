


-- Типы данных
-- VARCHAR Текстовый тип
-- BYTE 1 же 0 деген санды алат (1 или 0)
-- TEXT 16 878 Количество макс. Символов
-- MEDIUMTEXT 64 6565 кол-сво символов
-- LONGTEXT 4GB размер текста
-- FLOAT болчок сан (дробное число)
-- DOUBLE ото чон болчок чан (оочень большое дробное число)
-- INT бутун сан (целое число)
-- BIGINT ото чон бутун сан (очень большое целое число) (можно разместить кол-во звезд внебе)




CREATE DATABASE itc_Khan;

USE itcbootcamp;

CREATE TABLE users(
    name VARCHAR(250) NULL,
    login VARCHAR(100) NULL,
    password VARCHAR(100) NULL,
    address TEXT NULL DEFAULT NULL,
    number VARCHAR(250) NULL
);

INSERT INTO users(name,login) VALUES('Zalkarbek','khan');
INSERT INTO users(name,login, password, address,number) VALUES('Aibek','sary','aibeksary','osh city','+996700710020');

SELECT name, login, password, address,number FROM country;
DROP TABLE products;

CREATE TABLE balance(
    bank_name VARCHAR(250) NULL,
    user_name VARCHAR(250) NULL,
    cash FLOAT NULL
);

INSERT INTO balance(bank_name,user_name,cash) VALUES('Demir Bank', 'Zalkarbek', 89400.99);

CREATE TABLE country(
    name VARCHAR(250) NULL,
    valuta VARCHAR(250) NULL,
    population FLOAT NULL
);
INSERT INTO country(name,valuta,population) VALUES('Кыргызстан', 'сом',7000000);
INSERT INTO country(name,valuta,population) VALUES('Таджикистан', 'сомони',14000000);
INSERT INTO country(name,valuta,population) VALUES('Узбекистан', 'сум',23000000);
INSERT INTO country(name,valuta,population) VALUES('Китай', 'Юань',15000000000);



CREATE TABLE bank(
    bank_name VARCHAR(250) NULL,
    bank_balance VARCHAR(250) NULL,
    bank_info TEXT NULL DEFAULT NULL,
    client_count FLOAT NULL
);

INSERT INTO bank(bank_name, bank_balance, bank_info,client_count) 
    VALUES
        ('Bakai bank',7000000,'good', 1400000),
        ('K bank',7000000,'bad',20000),
        ('M bank',7000000,'very good',3030333),
        ('Aiyl bank',7000000,'good',8383883);

CREATE TABLE bank(
    bank_name VARCHAR(250) NULL,
    bank_balance VARCHAR(250) NULL,
    bank_info TEXT NULL DEFAULT NULL,
    client_count FLOAT NULL
);

INSERT INTO bank(bank_name, bank_balance, bank_info,client_count) 
    VALUES
        ('bb bank',100000,'good', 1100000);
        ('K bank',7000000,'bad',20000),
        ('M bank',7000000,'very good',3030333),
        ('Aiyl bank',7000000,'good',8383883);





-- LAB 3030333
--создайтуе филм  таблицу у себя 
--поля   
      --- name Varchar(200)
      ---year dates
      ---status
      ---actors text
      ---money int        

CREATE TABLE films(
    name_film VARCHAR(200) NULL,
    year_date Varchar(200) NULL,
    status_film VARCHAR(200) NULL,
    actors TEXT NULL DEFAULT NULL,
    money FLOAT NULL
);

('live',12.12.12,'good','Anjela',)

INSERT INTO films(name_film,year_date,status_film,actors_text, money_int)
    VALUES


