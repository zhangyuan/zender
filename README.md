## Transformer

## Example

Given the SQL script in `models/my_first_model.sql`:

```sql
WITH source AS (
  SELECT id, name FROM {{ ref("users")}}
)
INSERT INTO {{ target("usernames")}}
select * from source
```

Then run the following Python script:

```python
from transformer import compile_models

def main():
  models = [
    "my_first_model.sql"
  ]
  compile_models(models)

if __name__ == "__main__":
  main()
```

The compiled SQL scripts will be in `target/compiled/my_first_model.sql`. The metadata data is created in `target/medadata.json` with the following content:

```json
{
    "lineage": {
        "source_code": "my_first_model.sql",
        "targets": [
            "usernames"
        ],
        "sources": [
            "users"
        ]
    }
}
```
