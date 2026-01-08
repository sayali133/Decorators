"""
Role-based decorators 
Role-based decorators are used to enforce authorization rules before executing sensitive operations
such as deleting users, accessing admin dashboards, or performing financial transactions
"""
def role_required(required_role):
    def decorator(func):
        def wrapper(user_role):
            if user_role != required_role:
                raise PermissionError("Acess denied")
            return func()
        return wrapper
    return decorator


@role_required("admin")
def delete_user():
    print("user deleted")

delete_user("admin")
delete_user("user")
    