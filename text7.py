def make_step_counter():
    count = 0  # enclosing scope for 'increment'

    def increment():
        count += 1
        return count

    return increment

step = make_step_counter()
print(step())  # 1
print(step())  # 2