# The decorators module.

def log(filename=""):
    """The log decorator, which will automatically log the beginning and end of the function execution,
    as well as its results or errors that have occurred. The decorator must accept an optional argument filename,
    which determines where the logs will be written (to a file or to the console):
    - If filename is set, logs are written to the specified file.
    - If filename is not specified, the login is output to the console."""

    def logger(inner):
        def wrapper(*args, **kwargs):
            end_line = "\n"
            inner_name = inner.__name__
            log_result = ""
            try:
                result = inner(*args, **kwargs)
                log_result = "{0} {1}".format(inner_name, "ok")
                return result
            except Exception as e:
                log_result = "{0} {1}: {2}. Inputs: {3} {4}.".format(inner_name, "error", e, args, kwargs)
            finally:
                if filename == "":
                    print(log_result)
                else:
                    with open(filename, "a") as logfile:
                        logfile.write(log_result + end_line)
        return wrapper
    return logger
