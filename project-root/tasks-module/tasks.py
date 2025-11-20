import data_store

def create_task():
    if not _check_login_required():
        return
    global data_store.TASK_ID_COUNTER

    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    status = "Новая"  # начальный статус
    task = {
        'id': data_store.TASK_ID_COUNTER,
        'owner': data_store.CURRENT_USER,
        'title': title,
        'description': description,
        'status': status
    }
    data_store.TASKS_DB.append(task)
    data_store.TASK_ID_COUNTER += 1
    print(f"Задача '{title}' успешно создана с ID {task['id']}.")

def view_tasks(query=None):
    if not _check_login_required():
        return
    user_tasks = [t for t in data_store.TASKS_DB if t['owner'] == data_store.CURRENT_USER]
    if query:
        user_tasks = [t for t in user_tasks if query.lower() in t['title'].lower() or query.lower() in t['description'].lower()]

    if not user_tasks:
        print("Нет задач для отображения.")
        return
    
    print("\n--- Список задач ---")
    for t in user_tasks:
        print(f"ID: {t['id']}\nЗаголовок: {t['title']}\nОписание: {t['description']}\nСтатус: {t['status']}\n")
        
def update_task_status():
    if not _check_login_required():
        return
    task_id = int(input("Введите ID задачи для изменения статуса: "))
    task = _find_task_by_id(task_id)
    if not task:
        print("Задача не найдена.")
        return
    if task['owner'] != data_store.CURRENT_USER:
        print("Доступ запрещен.")
        return
    
    print("Выберите новый статус:")
    print("1. Новая")
    print("2. В процессе")
    print("3. Завершена")
    choice = input("Ваш выбор: ")
    status_map = {'1': 'Новая', '2': 'В процессе', '3': 'Завершена'}
    new_status = status_map.get(choice)
    if new_status:
        task['status'] = new_status
        print("Статус задачи обновлен.")
    else:
        print("Некорректный выбор.")

def delete_task():
    if not _check_login_required():
        return
    task_id = int(input("Введите ID задачи для удаления: "))
    task = _find_task_by_id(task_id)
    if not task:
        print("Задача не найдена.")
        return
    if task['owner'] != data_store.CURRENT_USER:
        print("Доступ запрещен.")
        return
    data_store.TASKS_DB.remove(task)
    print("Задача удалена.")

def _find_task_by_id(task_id):
    for t in data_store.TASKS_DB:
        if t['id'] == task_id:
            return t
    return None

def _check_login_required():
    if not data_store.CURRENT_USER:
        print("Ошибка: Для выполнения операции необходимо войти в систему.")
        return False
    return True
