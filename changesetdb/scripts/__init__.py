import click
import psycopg_pool
from changesetdb.database import Database


@click.group()
def cli():
    pass


@cli.command()
@click.option('-d', '--dbname')
@click.option('-h', '--host')
@click.option('-p', '--port')
@click.option('-U', '--username')
@click.option('--schema', default="public", show_default=True)
def create(dbname, host, port, username, schema):
    '''Create database tables'''
    click.echo("Creating tables")
    pool = psycopg_pool.NullConnectionPool(kwargs={"dbname": dbname,
                                                   "host": host,
                                                   "port": port,
                                                   "user": username})
    db = Database(pool, schema)
    db.create()


@cli.command()
@click.option('-d', '--dbname')
@click.option('-h', '--host')
@click.option('-p', '--port')
@click.option('-U', '--username')
@click.option('--schema', default="public", show_default=True)
def delete(dbname, host, port, username, schema):
    '''delete database tables'''
    click.echo("delete tables")
    pool = psycopg_pool.NullConnectionPool(kwargs={"dbname": dbname,
                                                   "host": host,
                                                   "port": port,
                                                   "user": username})
    db = Database(pool, schema)
    db.delete()
