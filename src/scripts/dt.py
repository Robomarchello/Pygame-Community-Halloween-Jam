def get_dt(fps):
    if fps < 30:
        fps = 60

    return (1/fps)*60
