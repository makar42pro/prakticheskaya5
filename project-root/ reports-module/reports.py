import data_store

def _check_login_required():
    if not data_store.CURRENT_USER:
        print("Ошибка: Для доступа к отчетам необходимо войти в систему.")
        return False
    return True

def generate_report():
    if not _check_login_required(): return
    print("\n--- Генерация отчета и статистики ---")
    
    user_tasks = [t for t in data_store.TASKS_DB if t['owner'] == data_store.CURRENT_USER]
    total_tasks = len(user_tasks)
    
    if total_tasks == 0:
        print("Нет данных для отчета.")
        return
        
    status_counts = {}
    for task in user_tasks:
        status = task['status']
        status_counts[status] = status_counts.get(status, 0) + 1
        
    print(f"Общее количество задач: {total_tasks}")
    print("Распределение по статусам:")
    for status, count in status_counts.items():
        print(f" - {status}: {count}")
    
    print("\nФункция экспорта данных в CSV/PDF (FR-R3) не реализована.")

