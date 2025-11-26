from app.services.note_manager import NoteManager

class ConsoleInterface:
    def __init__(self):
        self.manager = NoteManager()

    def display_menu(self):
        print("\n--- Gestionnaire de Notes ---")
        print("1. Ajouter une note")
        print("2. Voir toutes les notes")
        print("3. Modifier une note")
        print("4. Supprimer une note")
        print("5. Quitter")

    def get_user_input(self, prompt, type_func=str):
        while True:
            try:
                user_input = input(prompt)
                return type_func(user_input)
            except ValueError:
                print("Entrée invalide. Veuillez réessayer.")

    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_input("Choisissez une option : ")

            if choice == "1":
                self.add_note()
            elif choice == "2":
                self.list_notes()
            elif choice == "3":
                self.update_note()
            elif choice == "4":
                self.delete_note()
            elif choice == "5":
                print("Au revoir !")
                break
            else:
                print("Option invalide.")

    def add_note(self):
        print("\n--- Nouvelle Note ---")
        try:
            title = self.get_user_input("Titre : ")
            while not title.strip():
                print("Le titre ne peut pas être vide.")
                title = self.get_user_input("Titre : ")
                
            content = self.get_user_input("Contenu : ")
            self.manager.add_note(title, content)
            print("Note ajoutée avec succès !")
        except ValueError as e:
            print(f"Erreur : {e}")

    def list_notes(self):
        print("\n--- Liste des Notes ---")
        notes = self.manager.get_all_notes()
        if not notes:
            print("Aucune note enregistrée.")
        else:
            for note in notes:
                print(note)

    def update_note(self):
        print("\n--- Modifier une Note ---")
        self.list_notes()
        try:
            note_id = self.get_user_input("ID de la note à modifier : ", int)
            note = self.manager.get_note_by_id(note_id)
            
            if not note:
                print("Note introuvable.")
                return

            print(f"Modification de : {note.title}")
            new_title = input(f"Nouveau titre (laisser vide pour garder '{note.title}') : ")
            new_content = input(f"Nouveau contenu (laisser vide pour garder le contenu actuel) : ")

            # On passe None si la chaîne est vide pour ne pas écraser avec du vide si l'utilisateur ne veut pas changer
            title_to_update = new_title if new_title.strip() else None
            content_to_update = new_content if new_content.strip() else None

            if self.manager.update_note(note_id, title_to_update, content_to_update):
                print("Note modifiée avec succès !")
            else:
                print("Erreur lors de la modification.")
                
        except ValueError:
            print("ID invalide.")

    def delete_note(self):
        print("\n--- Supprimer une Note ---")
        self.list_notes()
        try:
            note_id = self.get_user_input("ID de la note à supprimer : ", int)
            if self.manager.delete_note(note_id):
                print("Note supprimée avec succès !")
            else:
                print("Note introuvable.")
        except ValueError:
            print("ID invalide.")
