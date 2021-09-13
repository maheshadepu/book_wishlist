
INSERT INTO wl_user (first_name, last_name, email) VALUES
('TestUser1', 'Doe', 'johndoe@gmail.com'),
('TestUser2', 'Jane', 'mary@gmail.com'),
('TestUser3', 'Parker', 'peter@gmail.com'),
('TestUser4', 'Jones', 'dan@gmail.com'),
('TestUser5', 'Wood', 'wood@gmail.com'),
('TestUser6', 'Hart', 'lane@gmail.com');


INSERT INTO book (isbn, title, author, date_of_publication) VALUES
('456-456', 'Shuggie Bain','Douglas Stuart', '2021-01-01' ),
('456-234', 'The Vanishing Half','Brit Bennett', '2021-02-01' ),
('456-235', 'The Invisible Life of Addie LaRue','V.E. Schwab', '2021-03-01' ),
('456-543', 'American Dirt','Jeanine Cummins', '2021-04-01' ),
('454-543', 'The Ballad of Songbirds and Snakes','Suzanne Collins', '2021-05-01' ),
('454-513', 'The Guest List','Lucy Foley', '2021-06-01' )
;


INSERT INTO wish_list (user_id, isbn) VALUES
(2, '456-456'),
(2, '456-234'),
(2, '456-235'),
(3, '456-456'),
(3, '454-543'),
(3, '454-513');
