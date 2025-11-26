class Note:
    def __init__(self, note_id, title, content):
        self._id = note_id
        self._title = title
        self._content = content

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str):
            raise ValueError("Le contenu doit être une chaîne de caractères.")
        self._content = value

    def to_dict(self):
        return {
            "id": self._id,
            "title": self._title,
            "content": self._content
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["content"])

    def __str__(self):
        return f"[{self._id}] {self._title}: {self._content}"
