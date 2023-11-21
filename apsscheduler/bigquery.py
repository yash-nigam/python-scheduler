from apscheduler.schedulers.blocking import BackgroundScheduler
from google.cloud import bigquery
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

# Set up your Google Cloud credentials
# Make sure to replace 'your_project_id' with your actual Google Cloud project ID
client = bigquery.Client(project='your_project_id')


def execute_query_and_print_rows(query, table_name):
    query_job = client.query(query)
    results = query_job.result()
    total_rows = 0
    for row in results:
        total_rows += 1
    print(f'Table: {table_name}, Total Rows: {total_rows}')


def schedule_task(cron_schedule, query, table_name):
    job_defaults = {
        'coalesce': False,
        'max_instances': 10
    }

    jobstores = {
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }

    executors = {
        'default': ThreadPoolExecutor(20)
    }

    scheduler = BackgroundScheduler(
        jobstores=jobstores,
        executors=executors,
        job_defaults=job_defaults,
        timezone=utc)
    scheduler.add_job(
        execute_query_and_print_rows,
        'cron',
        args=[query, table_name],
        id=table_name,
        trigger=cron_schedule)
    print(f'Scheduled task for Table {table_name} with cron schedule: {cron_schedule}')
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()


# Schedule 1: Run every 4 hours for the 'employee' table
cron_schedule_1 = '*/2 * * * *'
query_1 = "SELECT count(*) FROM `development-317013.test.titanic`"
table_name_1 = 'titanic'
schedule_task(cron_schedule_1, query_1, table_name_1)

# Schedule 2: Run every day at 2 am for the 'student' table
# cron_schedule_2 = '0 2 * * *'
# query_2 = 'SELECT * FROM your_project_id.dataset_name.student'
# table_name_2 = 'student'
# schedule_task(cron_schedule_2, query_2, table_name_2)

# Schedule 3: Run every 4 hours for the 'department' table
# cron_schedule_3 = '0 */4 * * *'
# query_3 = 'SELECT * FROM your_project_id.dataset_name.department'
# table_name_3 = 'department'
# schedule_task(cron_schedule_3, query_3, table_name_3)
