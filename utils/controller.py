def get_user_info(users_data: list)->None:


    for user in users_data:
        print(f"Twój znajomy {user['name']}! Z miejscowości {user['location']} opublikował {user['posts']} postów")
