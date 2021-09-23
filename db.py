import psycopg2
from configparser import ConfigParser

'''
python code to interact with postgresql database.
'''

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


def create_table(table_name: str) -> None:
    sql = f'CREATE TABLE IF NOT EXISTS public.{table_name} ' \
          f'(id integer NOT NULL, ' \
          f'name character varying COLLATE pg_catalog."default" NOT NULL, ' \
          f'ismod boolean); ' \
          f'ALTER TABLE public.{table_name} ' \
          f'OWNER to postgres;'

    params = config()
    print('Connecting to postgresql database...')
    con = psycopg2.connect(**params)

    # create a cursor
    cur = con.cursor()

    # Create a table
    print(f'Creating {table_name} table in db')
    cur.execute(sql)
    x = con.commit()

    # Close connection
    cur.close()
    con.close()

    return x

create_table('foobar')

def fetch_user_data() -> str:
    sql = '''SELECT * FROM users'''

    params = config()
    print('Connecting to postgresql database...')
    con = psycopg2.connect(**params)

    # create a cursor
    cur = con.cursor()
    cur.execute(sql)
    x = cur.fetchall()

    # Close connection
    cur.close()
    con.close()

    return x

for data in fetch_user_data():
    id, name, email, iscontractor, iscool = data
    print(f'[{id}]: {name} {email}, contractor: {iscontractor}, is cool? {iscool}')