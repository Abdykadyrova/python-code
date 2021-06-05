--создания базы данных для блога

TRUNCATE TABLE users;

CREATE TABLE users(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NULL,
    login VARCHAR(200) NULL,
    PASSWORD VARCHAR(300) NULL,
    is_admin BIT NULL,
    PRIMARY KEY(id)

)
COLLATE="utf8mb4_general_ci"
ENGINE=InnoDB;

INSERT INTO users(name,login,password,is_admin)
    VALUES
    ('Aiganysh','okines',1212,1),
    ('Aman','amanchik',2323,0),
    ('Aku','kjkh',5555,0),
    ('Emir','mmmm',6666,0);

INSERT INTO users(name, login, password, is_admin)
    VALUES
    ('Zalkar', 'zalkar', '123', 1),
    ('Meerim', 'meka', '123456', 0),
    ('Aiganysh', 'aika', '123456', 0),
    ('Bekbolot', 'beka', '9601', 0),
    ('Amantur', 'baby', '4513', 0),
    ('Emir', 'ema', '5354', 0),
    ('Bekzat', 'bekzat', '4502', 0),
    ('Iskender', 'iskender', '5656', 1);











--оновление записей
UPDATE users 
    SET
        name = 'aku'
        login = 'tan'
        password = '3449'
    WHERE id = 12;


UPDATE users    
    SET
        name = 'Hacker,
        login = 'hack',
        password = '1111'
    WHERE name = 'Anonymous';


INSERT INTO customers(customerNumber,customerName,country)
    VALUES
    (7777,'Aiganysh','Kyr')


UPDATE custmers 
    SET
    custName = 'hack'
    