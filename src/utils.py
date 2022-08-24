import settings


def width_percent(percentage):
    return (settings.WIDTH / 100) * percentage


def height_percent(percentage):
    return (settings.HEIGHT / 100) * percentage
