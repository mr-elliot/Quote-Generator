import psycopg2
from config import config
from web_scrapper import ScrapIt


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        ##################################################################################
        cur.execute("create table quote_db( quote varchar, author varchar)")
        conn.commit()

        # call scarper
        result = ScrapIt()

        for i in result:
            quot, auth = i.replace("'", "").split('--')
            st = f"insert into quote_db values('{quot}', '{auth}')"
            cur.execute(st)
            conn.commit()
        cur.execute("SELECT * FROM quote_db OFFSET floor(random() * (SELECT COUNT(*) FROM quote_db)) LIMIT 1")
        print(cur.fetchon())

        #################################################################################
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()




