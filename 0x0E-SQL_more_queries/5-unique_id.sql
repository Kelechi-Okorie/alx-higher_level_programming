-- creates table unique_id
-- description (id INT DEFAULT 1, name VARCHAR(256))
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));