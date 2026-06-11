import sqlite3
import pandas as pd

conn = sqlite3.connect("event_operations.db")

tables = {
    "Events": "Data/Events.csv",
    "Registrations": "Data/Registrations.csv",
    "Attendance": "Data/Attendance.csv",
    "Volunteers": "Data/Volunteers.csv",
    "Task_Assignments": "Data/Task_Assignments.csv",
    "Incidents": "Data/Incidents.csv"
}

for table_name, file_path in tables.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        conn,
        if_exists="append",
        index=False
    )

    print(f"{table_name} imported successfully")

conn.close()

print("All data loaded successfully.")