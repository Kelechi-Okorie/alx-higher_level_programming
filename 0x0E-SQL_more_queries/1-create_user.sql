-- creates a new MYSQL user name user_0_1
-- should have all privileges on the server
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grant privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;