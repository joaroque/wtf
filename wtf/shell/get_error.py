def get_error(error_log_file):
    with open(error_log_file, "r") as f:
        error = f.read()
        if not error:
            raise ValueError("Empty error log")

        open(error_log_file, "w").close()
    return error
