import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "todos.json")


def load_todos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def print_todos(todos):
    if not todos:
        print("할일이 없습니다.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
        print(f"[{status}] {i}. {todo['text']}")


def main():
    todos = load_todos()

    menu = """
1. 할일 목록 보기
2. 할일 추가
3. 완료 처리
4. 삭제
5. 종료
"""

    while True:
        print(menu)
        choice = input("선택> ").strip()

        if choice == "1":
            print_todos(todos)
        elif choice == "2":
            text = input("할일 내용> ").strip()
            if text:
                todos.append({"text": text, "done": False})
                save_todos(todos)
                print("추가되었습니다.")
        elif choice == "3":
            print_todos(todos)
            idx = input("완료할 번호> ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(todos):
                todos[int(idx) - 1]["done"] = True
                save_todos(todos)
                print("완료 처리되었습니다.")
            else:
                print("잘못된 번호입니다.")
        elif choice == "4":
            print_todos(todos)
            idx = input("삭제할 번호> ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(todos):
                removed = todos.pop(int(idx) - 1)
                save_todos(todos)
                print(f"삭제되었습니다: {removed['text']}")
            else:
                print("잘못된 번호입니다.")
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")


if __name__ == "__main__":
    main()
