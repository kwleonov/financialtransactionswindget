# The decorators module.

def log(filename=""):
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
