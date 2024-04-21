import sqlite3

db_name = 'test-sqlite.db'


# This function will connect to the sqlite3 database and then execute the sql script string use the
# cursor.executescript() function.
def execute_sql_script(sql_script_string):
    # Connect to sqlite3 database.
    conn = sqlite3.connect(db_name)

    # Open the cursor.
    cursor = conn.cursor()

    # Run the sql script string.
    cursor.executescript(sql_script_string)

    # Commit the above operation.
    conn.commit()

    # Close the cursor object.
    cursor.close()

    # Close the connection object.
    conn.close()

    print('Execute sql script ' + sql_script_string + ' complete.')


# This function will read the sql script text from the external sql file and then run the sql script text.
def execute_external_sql_script_file(script_file_path):
    # Open the external sql file.
    file = open('Weapon', 'r')

    # Read out the sql script text in the file.
    sql_script_string = file.read()

    # Close the sql file object.
    file.close()

    # Execute the read out sql script string.
    execute_sql_script(sql_script_string)


if __name__ == '__main__':
    # Create a sql script string, it contains two insert sql statements and one create table sql statement.
    sql_script_string = '''

    insert into user_account values( null,'jerry','123456789','jerry@gmail.com' );

    insert into user_account values( null,'tom','123456789','tom@gmail.com' );

    create table user_info(

       id integer primary key autoincrement,

       age text,

       sex text

    )

    '''

    # Execute the sql script string directly.
    # execute_sql_script(sql_script_string)

    # Execute the sql script string read from the passed in sql file.
    execute_external_sql_script_file('./sql_script.sql')