import auth
import tasks
import reports # Импортируем новый модуль
import data_store 

def main_menu():
    while True:
        print(f"СУЗ (Текущий пользователь: {data_store.CURRENT_USER or 'Гость'})")
        print("1. Регистрация")
        print("2. Войти")
        print("3. Выйти")
        print("4. Создать задачу")
        print("5. Посмотреть/фильтровать задачи")
        print("6. Изменить статус задачи")
        print("7. Удалить задачу")
        print("8. Сгенерировать отчет")
        print("9. Выйти из программы")
        choice = input("Выберите пункт меню: ")

        if choice == '1': auth.register()
        elif choice == '2': auth.login()
        elif choice == '3': auth.logout()
        elif choice == '4': tasks.create_task()
        elif choice == '5': 
            query = input("Введите запрос для поиска (оставьте пустым для всех задач): ")
            tasks.view_tasks(query if query else None)
        elif choice == '6': tasks.update_task_status()
        elif choice == '7': tasks.delete_task()
        elif choice == '8': reports.generate_report() # Вызов из нового модуля reports
        elif choice == '9': break
        else: print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main_menu()
