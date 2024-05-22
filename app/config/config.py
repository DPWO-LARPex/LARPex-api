# TODO

def build_db_url(driver, user, password, host, port, name):
    return f"{driver}://{user}:{password}@{host}:{port}/{name}"