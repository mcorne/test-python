try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")