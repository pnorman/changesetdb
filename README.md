# ChangesetDB

ChangesetDB is a program that takes the weekly changeset metadata dump from https://planet.openstreetmap.org/ and loads it into a PostgreSQL database for querying.

## Requirements

- Python 3.9+
- PostgreSQL 10+
- PostGIS 3.1+

## Setup

```sh
python3 -m venv venv
. venv/bin/activate
pip install --editable .
changesetdb --help
```


ChangesetDB requires a PostgreSQL database with PostGIS and hstore. It will attempt to install these extensions if they are not found.

```sh
createdb changesets
```

## Usage
The first time you use ChangesetDB, you will need to run the `create` task to create the necessary tables.

```sh
changesetdb create --help
```

## Contributing

All code should pass flake8 style checks
```sh
pip install flake8
flake8 changesetdb
```

## License

Copyright © 2023 Paul Norman <osm@paulnorman.ca>

The code is licensed terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
