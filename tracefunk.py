
import sys

       
def tracefunk(frame, event, *args):
    func.__name__ = frame.f_code.co_name
    if event == 'return':
        print("function: {}, local_vars: {}".format(func_name, ", ".join("{}".format(loc) for loc in frame.f_locals.keys)))
    return tracefunk


def stop(func):   
    sys.settrace(tracefunk)
    func()
    sys.settrace(None)
    
