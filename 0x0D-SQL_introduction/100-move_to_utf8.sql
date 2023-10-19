-- converts htbn_0c_0 db to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- both the db and first table
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert first_table to utf8
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- convert name column to utf8
ALTER TABLE hbtn_0c_0.first_table MODIFY 'name' VARCHAR(256) TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;