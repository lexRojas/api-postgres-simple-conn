
#import psycopg2
import psycopg2.extras

#---LOCAL DATABASE ----

# _hostname ='localhost'
# _username ='basedatos'
# _password ='basedatos'
# _database ='notario'

    #---HEROKU DATABASE ----

_hostname = 'sour-hawthorn.db.elephantsql.com'
_username = 'wficixke'
_password = 'pdeYA4t0t2psZcZL87t6zPjNpNQ5e0Jt'
_database = 'millerdb' 

DATABASE_URL = "postgresql://"+_username + ":"+ _password +"@"+ _hostname +":5432/" + _database

conn = psycopg2.connect(host=_hostname ,
                             user=_username,
                             password=_password,
                             database=_database)

cur = conn.cursor()


# with conn.cursor() as curs:
#   curs.execute('select * from public.tb_presupuesto limit 10')
#   result = curs.fetchall()
# print(result)

dict_cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
dict_cur.execute('select presupuesto, proyecto from public.tb_presupuesto limit 10')
rec = dict_cur.fetchall()
dict_cur.close()
print (rec)
