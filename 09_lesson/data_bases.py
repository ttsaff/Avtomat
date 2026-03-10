from sqlalchemy import create_engine, text

engine = create_engine("postgresql://serov:123456@localhost:5432/postgres", echo=True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM student"))
    rows = result.mappings().all()

print(rows[0]["user_id"])

for row in rows:
    print(row["user_id"])