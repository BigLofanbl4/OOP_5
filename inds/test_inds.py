import os
import unittest

from ind1 import People, validation


class TestPeople(unittest.TestCase):
    def setUp(self):
        """Инициализация тестовых данных перед каждым тестом."""
        self.people = People()
        self.test_file = "test_people.json"

    def tearDown(self):
        """Удаление тестовых файлов после выполнения теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_person(self):
        """Тестирование добавления человека в список."""
        self.people.add("Иванов", "Иван", "Овен", "01.01.2000")
        self.assertEqual(len(self.people.people), 1)
        self.assertEqual(self.people.people[0]["surname"], "Иванов")

    def test_save_and_load(self):
        """Тестирование сохранения и загрузки людей из файла."""
        self.people.add("Петров", "Петр", "Телец", "10.05.1990")
        self.people.save(self.test_file)

        loaded_people = People()
        loaded_people.load(self.test_file)

        self.assertEqual(len(loaded_people.people), 1)
        self.assertEqual(loaded_people.people[0]["name"], "Петр")

    def test_validation_success(self):
        """Тестирование успешной валидации данных."""
        valid_data = [
            {
                "surname": "Иванов",
                "name": "Иван",
                "zodiac": "Овен",
                "birthday": ["01", "01", "2000"],
            }
        ]
        self.assertTrue(validation(valid_data))

    def test_validation_failure(self):
        """Тестирование неудачной валидации данных."""
        invalid_data = [
            {
                "surname": "Иванов",
                "name": "Иван",
                "birthday": ["01", "01"],
            }  # Неполная дата
        ]
        self.assertFalse(validation(invalid_data))

    def test_select_by_surname(self):
        """Тестирование выборки людей по фамилии."""
        self.people.add("Сидоров", "Сидор", "Близнецы", "15.06.1985")
        self.people.add("Иванов", "Иван", "Овен", "01.01.2000")

        selected = self.people.select("Иванов")
        self.assertEqual(len(selected.people), 1)
        self.assertEqual(selected.people[0]["name"], "Иван")


if __name__ == "__main__":
    unittest.main()
