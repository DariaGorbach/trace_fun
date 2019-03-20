
import sys

       
def tracefunk(frame, event, *args):
    func_name = frame.f_code.co_name
    if event == 'return':
        print("function: {}, local_vars: {}".format(func_name, ", ".join("{}".format(loc) for loc in frame.f_locals.keys)))
    return tracefunk


def stop(tracefunk):   
    sys.settrace(tracefunk)
    tracefunk()
    sys.settrace(None)
    