from apscheduler.schedulers.background import BackgroundScheduler
from bot.messager import BotMessager

# jobs
scheduler = BackgroundScheduler()
messager = BotMessager()

scheduler.add_job(
    messager.post_job_offers_to_channel,
    day_of_week='mon-sun',
    hour=10
)
