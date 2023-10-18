-- creates a new db and a new user
-- should not fail if db or user exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create the new user
CREATE USER IF NOT EXISTS user_0d_2 identified by 'user_0d_2_pwd';
-- grant only select privilege to the user on hbtn_0d_2 db
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost ;