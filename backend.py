from threading import Thread
from pages.GooberDash.Backend.time_trials_sql import (
    update_leaderboard as GooberDash_update_time_trials_leaderboard,
)

t1 = Thread(target=GooberDash_update_time_trials_leaderboard())

t1.start()
t1.join()
