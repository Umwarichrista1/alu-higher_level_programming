-- Create the database hbtn_0d_2, without failing if it already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2, without failing if it already exists
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED WITH mysql_native_password BY 'user_0d_2_pwd';

-- Grant user_0d_2 only SELECT privilege on hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply privilege changes immediately
FLUSH PRIVILEGES;
