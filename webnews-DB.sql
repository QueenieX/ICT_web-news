CREATE DATABASE newsclassification;
USE newsclassification;

CREATE TABLE Categories 
(
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(50) NOT NULL
);

INSERT INTO Categories
(CategoryID, CategoryName) VALUES 
(1,'Sports'), (2, 'Technology'), (3, 'Politics'), (4, 'Entertainment'), (5, 'Business');

CREATE TABLE Users 
(
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(255),
    SearchHistory TEXT,
    Gender VARCHAR(255),
    Age INT,
    Preference1 INT,
    Preference2 INT,
    FOREIGN KEY (Preference1) REFERENCES Categories(CategoryID),
    FOREIGN KEY (Preference2) REFERENCES Categories(CategoryID)
);

CREATE TABLE NewsArticles 
(
    ArticleID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    CategoryID INT NOT NULL,
    Date DATE NOT NULL,
    URL VARCHAR(255) NOT NULL,
    Content VARCHAR(5000) NOT NULL,
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

CREATE INDEX idx_CategoryName
ON Categories (CategoryName);




show tables;
DESCRIBE newsarticles;
DESC categories;
select * from categories;
select * from newsarticles;