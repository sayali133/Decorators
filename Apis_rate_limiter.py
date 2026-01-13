#Real-World Version (Per User)
import time
from functools import wraps

def rate_limit(max_calls,window_seconds=60):
    user_calls = {}
    def decorator(func):
        @wraps(func)
        def wrapper(user_id, *args, **kwargs):
            current_time = time.time()
            user_calls.setdefault(user_id,[])


            user_calls[user_id] = [
                t for t in user_calls[user_id]
                if current_time - t < window_seconds
            ]

            if len(user_calls[user_id]) >= max_calls:
                print(f"User {user_id}: Rate limit exceeded")
                return

            user_calls[user_id].append(current_time)
            return func(user_id, *args, **kwargs)
        return wrapper
    return decorator

@rate_limit(3,10)
def api_call(user_id):
    print(f"Api accessed by user {user_id}")    

for i in range(5):
    api_call("sayali")
    time.sleep(1)
