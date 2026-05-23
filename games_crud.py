import sqlite3


DB_NAME = "games.db"
conn = sqlite3.connect(DB_NAME)


def create_table():
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            genre TEXT,
            year INTEGER
        )
        """
    )
    conn.commit()


def add_game():
    name = input("Назва гри: ")
    genre = input("Жанр: ")
    year = input("Рік: ")

    conn.execute(
        "INSERT INTO games (name, genre, year) VALUES (?, ?, ?)",
        (name, genre, year),
    )
    conn.commit()

    print("Гру додано.")


def show_games():
    games = conn.execute("SELECT id, name, genre, year FROM games").fetchall()

    if not games:
        print("Ігор поки немає.")
        return

    for game in games:
        print(f"{game[0]}. {game[1]} | {game[2]} | {game[3]}")


def update_game():
    show_games()
    game_id = input("ID гри для зміни: ")
    name = input("Нова назва: ")
    genre = input("Новий жанр: ")
    year = input("Новий рік: ")

    conn.execute(
        "UPDATE games SET name = ?, genre = ?, year = ? WHERE id = ?",
        (name, genre, year, game_id),
    )
    conn.commit()

    print("Гру оновлено.")


def delete_game():
    show_games()
    game_id = input("ID гри для видалення: ")

    conn.execute("DELETE FROM games WHERE id = ?", (game_id,))
    conn.commit()

    print("Гру видалено.")


def menu():
    create_table()

    while True:
        print("\n--- Меню ---")
        print("1. Додати гру")
        print("2. Показати всі ігри")
        print("3. Змінити гру")
        print("4. Видалити гру")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_game()
        elif choice == "2":
            show_games()
        elif choice == "3":
            update_game()
        elif choice == "4":
            delete_game()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    menu()
    conn.close()
