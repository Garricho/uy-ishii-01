class Content:
    def __init__(self, content_id, title, text):
        self.id = content_id
        self.title = title
        self.text = text

    def __str__(self):
        return f"{self.id}. {self.title} — {self.text}"


class ContentManager:
    def __init__(self):
        self.contents = []
        self.next_id = 1

    def create(self, title, text):
        new_content = Content(self.next_id, title, text)
        self.contents.append(new_content)
        self.next_id += 1
        return new_content

    def read_all(self):
        return self.contents

    def read(self, content_id):
        for c in self.contents:
            if c.id == content_id:
                return c
        return None

    def update(self, content_id, new_title, new_text):
        content = self.read(content_id)
        if content:
            content.title = new_title
            content.text = new_text
            return True
        return False

    def delete(self, content_id):
        content = self.read(content_id)
        if content:
            self.contents.remove(content)
            return True
        return False


def main():
    manager = ContentManager()

    while True:
        print("\n--- CONTENT MANAGER ---")
        print("1. Create")
        print("2. Read all")
        print("3. Read one")
        print("4. Update")
        print("5. Delete")
        print("0. Exit")

        choice = input("Tanlang: ")

        if choice == "1":
            title = input("Sarlavha: ")
            text = input("Text: ")
            item = manager.create(title, text)
            print("Yaratildi:", item)

        elif choice == "2":
            for item in manager.read_all():
                print(item)

        elif choice == "3":
            cid = int(input("ID kiriting: "))
            item = manager.read(cid)
            print(item if item else "Topilmadi")

        elif choice == "4":
            cid = int(input("ID: "))
            title = input("Yangi sarlavha: ")
            text = input("Yangi text: ")
            print("Yangilandi" if manager.update(cid, title, text) else "Topilmadi")

        elif choice == "5":
            cid = int(input("ID: "))
            print("O'chirildi" if manager.delete(cid) else "Topilmadi")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()
