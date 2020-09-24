try:
    raise Exception(1, 2)
except Exception, e: # should be Exception as e
    print(e.args)
