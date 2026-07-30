-- Create the user user_0d_1, without failing if it already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant user_0d_1 all privileges on the server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
