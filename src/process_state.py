import numpy as np

STATE_DIMENSION = 4

def normalize_brushing_duration(duration):
    return (duration - 172) / 118

def process_state(state_data):
    current_state = np.ones(STATE_DIMENSION)
    # time of day
    current_state[0] = state_data['time_of_day']
    # prior day total brushing duration
    current_state[1] = normalize_brushing_duration(state_data['prior_day_brush_duration'])
    # app engagement indicator
    current_state[2] = state_data['app_engagement']

    return current_state
