from expense import add_expense
from income import add_income, calculate_balance, filter_by_date


if __name__ == "__main__":
    """Главная функция для запуска программы."""

    transactions = []
    """ Список для хранения всех транзакций"""

    while True:
        print("\nУчёт расходов и доходов")
        print("1. Добавить расход")
        print("2. Добавить доход")
        print("3. Рассчитать баланс")
        print("4. Фильтр операций по дате")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense(transactions)
        elif choice == '2':
            add_income(transactions)
        elif choice == '3':
            calculate_balance(transactions)
        elif choice == '4':
            filter_by_date(transactions)
        elif choice == '0':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите пункт меню от 0 до 4.")
