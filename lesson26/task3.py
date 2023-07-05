# Завершаем функциональность класса Contacts. На этом этапе мы добавим в класс метод
# remove_contacts. Метод должен удалять контакт по уникальному id в списке contacts.
# Если словаря с указанным id в списке contacts не найдено, метод никаких действий над
# списком contacts не производит.
#
# Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде.
class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact['id'] == id:
                return contact

    def remove_contacts(self, id):
        for index, contact in enumerate(self.contacts):
            if contact['id'] == id:
                self.contacts.pop(index)


addressbook = Contacts()
addressbook.add_contacts('Oleksandr', '+380937316048', 'olexandr.samus.2004@gmail.com', True)
addressbook.add_contacts('Oleksandr', '+380937316048', 'olexandr.samus.2004@gmail.com', True)
addressbook.add_contacts('Oleksandr', '+380937316048', 'olexandr.samus.2004@gmail.com', True)
print(addressbook.get_contact_by_id(3))
addressbook.remove_contacts(3)
print(addressbook.list_contacts())