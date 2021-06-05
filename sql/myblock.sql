
CREATE DATABASE itc_aika_myblog;
USE itc_aika_myblog;
-- ТАБЛИЦА ПОЛЬЗОВАТЕЛИ
-- ---------------------------------------
CREATE TABLE users(
 id INT NOT NULL AUTO_INCREMENT,
 name VARCHAR(200) NULL,
 login VARCHAR(200) NULL,
 password VARCHAR(300) NULL,
 is_admin BIT NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
-- ТАБЛИЦА КАТЕГОРИЯ СТАТЬЕЙ
-- ---------------------------------------
CREATE TABLE post_category(
 id INT NOT NULL AUTO_INCREMENT,
 name VARCHAR(200) NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
-- ТАБЛИЦА СТАТЬИ
-- ---------------------------------------
CREATE TABLE posts(
 id INT NOT NULL AUTO_INCREMENT,
 user_id INT NULL,
 title VARCHAR(200) NULL,
 content LONGTEXT NULL,
 short_content TEXT NULL,
 image_url TEXT NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
-- ТАБЛИЦА МЕНЮ САЙТА
-- ---------------------------------------
CREATE TABLE menu(
 id INT NOT NULL AUTO_INCREMENT,
 menu_name VARCHAR(200) NULL,
 menu_url VARCHAR(200) NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;


-- ---------------------------------------
-- ---------------------------------------
-- ТАБЛИЦА КАТЕГОРИЯ СТАТЬЕЙ
-- ---------------------------------------
CREATE TABLE post_category(
 id INT NOT NULL AUTO_INCREMENT,
 name VARCHAR(200) NULL,
 PRIMARY KEY(id)



)    
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;

INSERT INTO post_category(name)
    VALUES
    ('economica'),
    ('programming'),
    ('news'),
    ('hgyugtyf')

-- ---------------------------------------
-- ТАБЛИЦА СТАТЬИ
-- ---------------------------------------
CREATE TABLE posts(
 id INT NOT NULL AUTO_INCREMENT,
 user_id INT NULL,
 title VARCHAR(200) NULL,
 content LONGTEXT NULL,
 short_content TEXT NULL,
 image_url TEXT NULL,content LONGTEXT
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;

INSERT INTO posts(user_id,title,content,short_content,image_url)
    VALUES
    (3,'about politcs','jhjhasidhUHD','HdlyHWIUDH',""),
    (5,'about business','hbshbas','ahbhbh',""),
    (6,'about education','jdic','jhsdihcb',""),
-- ---------------------------------------
-- ТАБЛИЦА МЕНЮ САЙТА
-- ---------------------------------------
CREATE TABLE menu(
 id INT NOT NULL AUTO_INCREMENT,
 menu_name VARCHAR(200) NULL,
 menu_url VARCHAR(200) NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
INSERT INTO posts(menu_name,menu_url)
    VALUES
    ('главная','/'),
    ('статьи','/posts' ),
    ('программа','/posts'),
    ('fffg','/posts')
    
ALTER TABLE posts
ADD COLUMN post_category_id INT NULL;
-- ---------------------------------------















