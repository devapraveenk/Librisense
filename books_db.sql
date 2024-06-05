-- Create the database
CREATE DATABASE bookdb;
USE bookdb;

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    book_name VARCHAR(255),
    book_author VARCHAR(255),
    book_availability BOOLEAN,
    book_count INT
);

INSERT INTO books (book_id, book_name, book_author, book_availability, book_count)
VALUES
(1, 'Python Crash Course', 'Eric Matthes', TRUE, 10),
(2, 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow', 'Aurélien Géron', TRUE, 8),
(3, 'Eloquent JavaScript', 'Marijn Haverbeke', TRUE, 15),
(4, 'SQL for Beginners: Learn SQL using MySQL and Database Management', 'Pete Houston', TRUE, 12),
(5, 'Network Security Essentials', 'William Stallings', TRUE, 7),
(6, 'Data Science for Beginners: A Comprehensive Introduction to Data Science', 'Nathan Lee', TRUE, 9),
(7, 'Clean Code: A Handbook of Agile Software Craftsmanship', 'Robert C. Martin', TRUE, 11),
(8, 'Computer Networking: A Top-Down Approach', 'James F. Kurose', TRUE, 6),
(9, 'Cloud Computing: Concepts, Technology & Architecture', 'Thomas Erl', TRUE, 10),
(10, 'Cybersecurity for Dummies', 'Joseph Steinberg', TRUE, 14),
(11, 'Automate the Boring Stuff with Python', 'Al Sweigart', TRUE, 13),
(12, 'Artificial Intelligence: A Modern Approach', 'Stuart Russell, Peter Norvig', TRUE, 5),
(13, 'Mastering Blockchain', 'Imran Bashir', TRUE, 7),
(14, 'The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win', 'Gene Kim, Kevin Behr, George Spafford', TRUE, 9),
(15, 'Software Architecture Patterns', 'Mark Richards', TRUE, 6);
