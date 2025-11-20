import data_store

def register():
    print("\n--- Регистрация ---")
    username = input("Введите логин: ")
    if username in data_store.USERS_DB:
        print(f"Ошибка: Пользователь с логином '{username}' уже существует.")
        return

    email = input("Введите email: ")
    password = input("Введите пароль: ")
    data_store.USERS_DB[username] = {'password': password, 'email': email}
    print(f"Пользователь '{username}' успешно зарегистрирован!")

def login():
    print("\n--- Авторизация ---")
    if data_store.CURRENT_USER:
        print(f"Вы уже вошли как {data_store.CURRENT_USER}.")
        return

    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    user_data = data_store.USERS_DB.get(username)

    if user_data and user_data['password'] == password:
        data_store.CURRENT_USER = username 
        print(f"Добро пожаловать, {data_store.CURRENT_USER}! Вы успешно вошли.")
    else:
        print("Ошибка входа: Неверный логин или пароль.")

def logout():
    if data_store.CURRENT_USER:
        print(f"Пользователь {data_store.CURRENT_USER} вышел из системы.")
        data_store.CURRENT_USER = None
    else:
        print("Вы не авторизованы.")

