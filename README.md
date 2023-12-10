# Zender

Render templates written in Jinja2, with extra metadata store.

## Installation

```bash
pip install zender
```

## Usage

By default, `zender` renders the templates from `./templates` folder to `./target` folder.

Firstly, Create the `./templates` folder and add a templates, e.g. `./templates/active_users.sql`:

```sql
WITH source AS (
  select id, username from users where status = {{ source('active') }}
)
INSERT INTO {{ target('active_users') }}
VALUES
SELECT id, username from source
```

The compiled file is created in `./target/compiled/active_users.sql` with the following content:

```sql
WITH source AS (
  select id, username from users where status = active
)
INSERT INTO active_users
SELECT id, username from source
```

And the metadata is saved into `target/metadata.json`:

```json
{
    "lineage": [
        {
            "source_code": "active_users.sql",
            "targets": [
                "active_users"
            ],
            "sources": [
                "active"
            ]
        }
    ]
}
```
