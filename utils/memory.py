
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class ChatMemory:


    def __init__(self):

        self.history_file = BASE_DIR / "data" / "history" / "chat_history.json"
        self.history_file.parent.mkdir(parents=True, exist_ok=True)

        if self.history_file.exists():
            try:
                with open(self.history_file, "r", encoding="utf-8") as file:
                    self.history = json.load(file)
            except Exception:
                self.history = []
        else:
            self.history = []

        self.last_uploaded_file = None
        self.last_uploaded_file_name = None
        self.last_uploaded_file_type = None
        self.last_image = None

        self.last_paper = None

        self.current_module = None
        self.current_language = "en"
        self.last_response = ""
        self.last_query = ""


    def add_message(self, role, message):
        self.history.append({"role": role, "message": message})
        self._save_history()


    def get_history(self):
        return self.history


    def clear_history(self):
        self.history.clear()
        self._save_history()


    def _save_history(self):
        with open(self.history_file, "w", encoding="utf-8") as file:
            json.dump(self.history, file, indent=4, ensure_ascii=False)


    def reset_uploaded_file(self):
        self.last_uploaded_file = None
        self.last_uploaded_file_name = None
        self.last_uploaded_file_type = None
        self.last_image = None


    def set_uploaded_file(self, uploaded_file, file_type=None):
        self.last_uploaded_file = uploaded_file
        self.last_uploaded_file_type = file_type

        if uploaded_file:
            self.last_uploaded_file_name = Path(uploaded_file).name


    def set_last_image(self, image):
        self.last_image = image


    def set_uploaded_file_name(self, file_name):
        self.last_uploaded_file_name = file_name


    def set_uploaded_file_type(self, file_type):
        self.last_uploaded_file_type = file_type


memory = ChatMemory()
