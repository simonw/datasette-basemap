from datasette import hookimpl
from datasette.database import Database
import pathlib

BASEMAP = pathlib.Path(__file__).parent / "data" / "basemap.db"


@hookimpl
def startup(datasette):
    datasette.add_database(Database(datasette, path=str(BASEMAP), is_mutable=False))
