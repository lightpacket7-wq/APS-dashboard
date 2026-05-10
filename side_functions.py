from sqlalchemy import create_engine, text
import pandas as pd

"""
To run: open Terminal in this folder and run "py -3.8 side_functions.py"
"""


DB_PATH = "APS_data_base2.db"
TABLE = "Disruption Time Measurement"


DATES = ["10:11:31 25-01-2026",
         "20:16:31 22-01-2026",
         "17:39:24 13-01-2026",
         "16:44:33 13-01-2026",
         "12:42:00 12-01-2026",
         "12:16:13 12-01-2026",
         "09:45:35 25-01-2026",
         "11:44:27 12-01-2026",
         "19:14:44 11-01-2026",
         "18:58:05 11-01-2026",
         "17:20:22 11-01-2026",
         "12:20:44 11-01-2026",
         "16:48:51 10-08-2025",
         "20:43:51 10-08-2025",
         "14:45:22 08-12-2025",
         "19:58:00 08-01-2026",
         "18:34:44 08-01-2026",
         "17:19:58 08-01-2026",
         "16:36:56 25-12-2025",
         "17:31:31 15-12-2025",
         "20:05:38 22-01-2026",
         "19:51:58 22-01-2026",
         "19:48:33 22-01-2026",
         "19:45:02 22-01-2026",
         "21:07:02 20-01-2026",
         "21:05:33 20-01-2026",
         "21:03:10 20-01-2026",
         "19:06:22 19-01-2026",
         "13:20:38 14-01-2026",
         "16:42:02 13-01-2026",
         "10:58:18 11-01-2026",
         "19:52:06 08-01-2026",
         "19:29:26 08-01-2026",
         "11:38:30 17-09-2025",
         "19:01:19 03-02-2026",
         "18:48:35 03-02-2026",
         "16:20:47 17-03-2026",
         "20:05:53 24-02-2026",
         "20:02:16 24-02-2026",
         "19:17:33 19-02-2026",
         "15:48:49 17-02-2026",
         "15:26:17 17-02-2026",
         "15:18:28 17-02-2026",
         "17:50:24 26-03-2026",
         "21:21:24 25-03-2026",
         "21:15:31 25-03-2026",
         "09:38:27 11-08-2025",
         "21:16:33 20-01-2026",
         "20:25:47 22-01-2026",
         "15:05:34 25-01-2026",
         "14:10:24 22-12-2025",
         "10:08:47 09-12-2025",
         "13:14:00 22-02-2026",
         "20:19:41 24-02-2026",
         "12:11:32 17-09-2025",
         "15:48:55 30-09-2025",
         "16:40:39 30-09-2025",
         "11:45:06 21-12-2025",
         "16:29:50 17-02-2026"]


def delete_by_row_ids(db_path, table_name, row_ids):
    """
    Delete rows from SQLite table by rowid.
    row_ids: list[int]
    """
    if not row_ids:
        raise ValueError("row_ids list is empty")

    engine = create_engine(f"sqlite:///{db_path}")

    placeholders = ",".join(str(int(i)) for i in row_ids)
    query = text(f'''
        DELETE FROM "{table_name}"
        WHERE rowid IN ({placeholders})
    ''')

    with engine.begin() as conn:
        result = conn.execute(query)

    print(f"Deleted {result.rowcount} rows.")

def delete_by_timestamp(db_path, table_name, timestamp_value):


    """
    Delete rows where Time Stamp equals the given value.
    timestamp_value must match DB format exactly.
    """
    engine = create_engine(f"sqlite:///{db_path}")

    query = text(f'''
        DELETE FROM "{table_name}"
        WHERE "Time Stamp" = :ts
    ''')

    with engine.begin() as conn:
        result = conn.execute(query, {"ts": timestamp_value})

    print(f"Deleted {result.rowcount} rows.")

def preview_delete_by_ids(db_path, table_name, row_ids):
    engine = create_engine(f"sqlite:///{db_path}")
    ids = ",".join(str(i) for i in row_ids)
    df = pd.read_sql(
        f'SELECT rowid, * FROM "{table_name}" WHERE rowid IN ({ids})',
        engine
    )
    return df


if __name__ == '__main__':
    # id_list = list(range(1, 21))

    # preview_delete_by_ids(DB_PATH, TABLE, row_ids=id_list)


    # delete_by_row_ids(DB_PATH, TABLE, row_ids=id_list)

    for date in DATES:
        delete_by_timestamp(DB_PATH, TABLE, timestamp_value=date)
    