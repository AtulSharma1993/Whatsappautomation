from apscheduler.schedulers.blocking import BlockingScheduler
from Whatsapp import send_text

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_text, 'interval', seconds=10)

sched.start()