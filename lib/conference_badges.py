def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {i+1}!" for i, name in enumerate(names)]

def printer(names):
    [print(badge) for badge in batch_badge_creator(names)]
    [print(assignment) for assignment in assign_rooms(names)]
