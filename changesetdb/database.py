class Database:
    def __init__(self, pool, schema):
        self.__pool = pool
        self.__schema = schema

    def create(self):
        '''Creates the necessary tables, and any constraints that should exist on upload'''
        schema = self.__schema
        with self.__pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute('''CREATE EXTENSION IF NOT EXISTS hstore;\n'''
                            '''CREATE EXTENSION IF NOT EXISTS postgis;''')

                cur.execute(f'''CREATE SCHEMA IF NOT EXISTS "{schema}"\n''')

                cur.execute(f'''CREATE TABLE "{schema}"."users" (\n'''
                            f'''    id bigint primary key,\n'''
                            f'''    name text)''')
                # TODO: Does uid 0 need to exist?

                cur.execute(f'''CREATE TABLE "{schema}"."changesets" (\n'''
                            f'''    id bigint not null, user_id bigint not null,\n'''
                            f'''    created_at timestamptz, closed_at timestamptz,\n'''
                            f'''    open boolean, num_changes integer,\n'''
                            f'''    min_lat numeric(10,7), max_lat numeric(10,7),\n'''
                            f'''    min_lon numeric(10,7), max_lon numeric(10,7),\n'''
                            f'''    tags hstore, geom Geometry(POLYGON,4326) );\n''')

                cur.execute(f'''CREATE TABLE "{schema}"."discussions" (\n'''
                            f'''    id bigint not null, user_id bigint not null,\n'''
                            f'''    date timestamptz not null, text text not null)''')
            conn.commit()

    def delete(self):
        schema = self.__schema
        with self.__pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f'''DROP TABLE IF EXISTS \n'''
                            f'''  "{schema}"."users", "{schema}"."changesets",\n'''
                            f'''  "{schema}"."discussions"\n'''
                            f'''  CASCADE''')

            conn.commit()
