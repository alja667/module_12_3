import unittest
import  runnner_2

class TournamentTest(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.obj1 = runnner_2.Runner("Усэйн", 10)
        self.obj2 = runnner_2.Runner("Андрей", 9)
        self.obj3 = runnner_2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):

        for key, value in cls.all_results.items():
            print(f'{key}: {value}')

    def test_1(self):
        name_1 = runnner_2.Tournament(90, self.obj1, self.obj3)
        all_results = name_1.start()
        self.assertTrue(all_results[2], self.obj3)
        if all_results[2] != "Ник":
            print(f'Ошибка! Последним должен быть Ник')
        else:
            print(f"Ошибки нет! Последний Ник")


    def test_2(self):
        name_2 = runnner_2.Tournament(90, self.obj2, self.obj3)
        all_results = name_2.start()
        self.assertTrue(all_results[2], self.obj3)
        if all_results[2] != "Ник":
            print(f'Ошибка! Последним должен быть Ник')
        else:
            print(f"Ошибки нет! Последний Ник")


    def test_3(self):
        name_3 = runnner_2.Tournament(90, self.obj1, self.obj2, self.obj3)
        all_results = name_3.start()
        self.assertTrue(all_results[3], self.obj3)
        if all_results[3] != "Ник":
            print(f'Ошибка! Последним должен быть Ник')
        else:
            print(f"Ошибки нет! Последний Ник")

    def test_4 (self):
        name_3 = runnner_2.Tournament(6, self.obj1, self.obj2, self.obj3)
        all_results = name_3.start()
        self.assertTrue(all_results[3], self.obj3)
        if all_results[3] != "Ник":
            print(f'Ошибка! Последним должен быть Ник')
        else:
            print(f"Ошибки нет! Последний Ник")
            
if __name__ == '__main__':
    unittest.main()

