import pandas as pd
from faker import Faker
import random

fake = Faker()

events = [
    [101, "Dance Competition", "Cultural", "2025-08-15", "Main Auditorium"],
    [102, "Singing Competition", "Cultural", "2025-08-15", "Seminar Hall"],
    [103, "Battle of Bands", "Cultural", "2025-08-15", "Open Stage"],
    [104, "Fashion Show", "Cultural", "2025-08-16", "Main Auditorium"],
    [105, "Drama Competition", "Cultural", "2025-08-16", "Auditorium"],
    [106, "Photography Contest", "Cultural", "2025-08-16", "Gallery Hall"],
    [107, "Short Film Contest", "Cultural", "2025-08-17", "Seminar Hall"],
    [108, "Stand-Up Comedy", "Cultural", "2025-08-17", "Open Stage"],
    [109, "Celebrity Night", "Special Event", "2025-08-17", "Main Ground"],
    [110, "DJ Night", "Special Event", "2025-08-17", "Main Ground"]
]

events_df = pd.DataFrame(
    events,
    columns=[
        "Event_ID",
        "Event_Name",
        "Event_Category",
        "Event_Date",
        "Venue"
    ]
)

events_df.to_csv("Data/Events.csv", index=False)


departments = [
    "CSE",
    "IT",
    "ECE",
    "EEE",
    "MECH",
    "CIVIL",
    "AIDS"
]

registrations = []

for reg_id in range(1, 651):

    registrations.append([
        reg_id,
        fake.name(),
        fake.email(),
        random.choice(departments),
        random.randint(101,110),
        fake.date_between(
            start_date="-30d",
            end_date="today"
        )
    ])

registrations_df = pd.DataFrame(
    registrations,
    columns=[
        "Registration_ID",
        "Participant_Name",
        "Email",
        "Department",
        "Event_ID",
        "Registration_Date"
    ]
)

registrations_df.to_csv(
    "Data/Registrations.csv",
    index=False
)

attendance = []

for reg_id in range(1,651):

    status = random.choices(
        ["Present","Absent"],
        weights=[78,22]
    )[0]

    attendance.append([
        reg_id,
        reg_id,
        status,
        "2025-08-15"
    ])

attendance_df = pd.DataFrame(
    attendance,
    columns=[
        "Attendance_ID",
        "Registration_ID",
        "Attendance_Status",
        "Attendance_Date"
    ]
)

attendance_df.to_csv(
    "Data/Attendance.csv",
    index=False
)

volunteers = []

for volunteer_id in range(1,21):

    volunteers.append([
        volunteer_id,
        fake.name(),
        random.choice(departments),
        fake.phone_number()
    ])

volunteers_df = pd.DataFrame(
    volunteers,
    columns=[
        "Volunteer_ID",
        "Volunteer_Name",
        "Department",
        "Contact_Number"
    ]
)

volunteers_df.to_csv(
    "Data/Volunteers.csv",
    index=False
)

tasks = [
    "Registration Desk",
    "Crowd Management",
    "Stage Coordination",
    "Backstage Support",
    "Guest Hospitality",
    "Food Court Support",
    "Security Assistance",
    "Photography Support",
    "Participant Check-In",
    "Venue Setup"
]

task_assignments = []

for task_id in range(1,51):

    task_assignments.append([
        task_id,
        random.randint(1,20),
        random.choice(tasks),
        random.choices(
            ["Completed","In Progress","Pending"],
            weights=[70,20,10]
        )[0],
        "2025-08-15"
    ])

tasks_df = pd.DataFrame(
    task_assignments,
    columns=[
        "Task_ID",
        "Volunteer_ID",
        "Task_Name",
        "Task_Status",
        "Assigned_Date"
    ]
)

tasks_df.to_csv(
    "Data/Task_Assignments.csv",
    index=False
)

incident_types = [
    "Sound System Failure",
    "Microphone Issue",
    "Guest Arrival Delay",
    "Stage Setup Delay",
    "Crowd Congestion",
    "Registration Queue Delay",
    "Power Outage",
    "Food Stall Complaint",
    "Lost Participant ID",
    "Security Concern"
]

reported_by = [
    "Volunteer",
    "Technical Team",
    "Event Coordinator",
    "Faculty Coordinator"
]

incidents = []

for incident_id in range(1,41):

    incidents.append([
        incident_id,
        random.choice(incident_types),
        random.choice(
            ["High","Medium","Low"]
        ),
        random.choice(
            ["Open","Closed"]
        ),
        random.choice(reported_by),
        random.randint(5,60),
        "2025-08-15"
    ])

incidents_df = pd.DataFrame(
    incidents,
    columns=[
        "Incident_ID",
        "Incident_Type",
        "Priority",
        "Status",
        "Reported_By",
        "Resolution_Time",
        "Reported_Date"
    ]
)

incidents_df.to_csv(
    "Data/Incidents.csv",
    index=False
)

print("Data generation completed successfully!")

print(f"Events: {len(events_df)}")
print(f"Registrations: {len(registrations_df)}")
print(f"Attendance: {len(attendance_df)}")
print(f"Volunteers: {len(volunteers_df)}")
print(f"Tasks: {len(tasks_df)}")
print(f"Incidents: {len(incidents_df)}")