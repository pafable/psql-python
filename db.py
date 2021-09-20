import psycopg2
from configparser import ConfigParser

# get db configs
def config(filename="config.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} is not found in the {filename}')

    return db

def connect():
    connection = None
    params = config()
    print('Connecting to postgresql database...')
    con = psycopg2.connect(**params)

    # create a cursor
    # crsr = con.cursor()


print(connect())