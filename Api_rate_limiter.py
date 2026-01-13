#Basic Rate Limiter (per time window)
import time
from functools import wraps #wraps:keeps original function metadata and preserves function name,docstring
def rate_limit(max_calls,window_seconds=60):
    def decorator(func): # receives the function being decorated
        calls = [] #stores timestamps of calls
        @wraps(func)
        def wrapper(*args,**kwargs):
            nonlocal calls #allows modifying calls from outer scope
            current_time = time.time()
            calls = [t for t in calls if current_time - t < window_seconds]


            if len(calls) >= max_calls:
                print("Rate limit exceeded.Try later")
                return

            calls.append(current_time)
            print("Calls count:", len(calls)) 
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(5,window_seconds=10)
def api_call():
    print(f"Api accessed at {time.strftime('%x')}")

for i in range(7):
    api_call()
    time.sleep(1)
