echo 'from utils import fetch_data, format_output
from config import APP_NAME, VERSION

def main():
    print(f"{APP_NAME} v{VERSION}")
    print("Загрузка постов...")
    posts = fetch_data("posts")
    print("Первые 5 постов:")
    print(format_output(posts))

if __name__ == "__main__":
    main()' > main.py
