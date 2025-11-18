import data_store

def register():
    """Регистрация нового пользователя (FR-A1, FR-A2, FR-A3)"""
    print("\n--- Регистрация ---")
    username = input("Введите логин: ")
    if username in data_store.USERS_DB:
        print(f"Ошибка: Пользователь с логином '{username}' уже существует.")
        return

    email = input("Введите email: ")
    password = input("Введите пароль: ")
    # В реальном приложении пароль нужно хешировать (FR-A4), здесь упрощено
    data_store.USERS_DB[username] = {'password': password, 'email': email}
    print(f"Пользователь '{username}' успешно зарегистрирован!")

def login():
    """Авторизация пользователя (FR-A5, FR-A6, FR-A7, FR-A8)"""
    print("\n--- Авторизация ---")
    if data_store.CURRENT_USER:
        print(f"Вы уже вошли как {data_store.CURRENT_USER}.")
        return

    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    user_data = data_store.USERS_DB.get(username)

    if user_data and user_data['password'] == password:
        data_store.CURRENT_USER = username # Обновляем глобальное состояние
        print(f"Добро пожаловать, {data_store.CURRENT_USER}! Вы успешно вошли.")
    else:
        print("Ошибка входа: Неверный логин или пароль.")

def logout():
    """Выход из системы (FR-A9)"""
    if data_store.CURRENT_USER:
        print(f"Пользователь {data_store.CURRENT_USER} вышел из системы.")
        data_store.CURRENT_USER = None # Обнуляем глобальное состояние
    else:
        print("Вы не авторизованы.")

