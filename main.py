from utils import fetch_data, format_output
from config import APP_NAME, VERSION
from utils import get_timestamp

def main():
    try:
        print(f"Run at {get_timestamp()}")
        print(f"{APP_NAME} v{VERSION}")
        print("Загрузка постов...")
        posts = fetch_data("posts")
        print("Первые 5 постов:")
        print(format_output(posts))
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()
