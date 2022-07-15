import numpy as np

SCHEDULE_LENGTH_IN_DAYS = 14
DECISION_TIMES_PER_DAY = 2

def action_selection(user, current_state):
    schedule = np.zeros(shape=(SCHEDULE_LENGTH_IN_DAYS, DECISION_TIMES_PER_DAY))

    # TODO: need to decide on data structure of return response
    return dict(enumerate(schedule.flatten(), 1))
