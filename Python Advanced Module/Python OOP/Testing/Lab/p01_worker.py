class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correctly(self):
        worker = Worker('Test', 100, 10)

        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_is_worker_energy_raises(self):
        worker = Worker('Test', 100, 10)

        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)
        worker.rest()
        self.assertEqual(12, worker.energy)

    def test_is_worker_work_with_negative_energy(self):
        worker = Worker('Test', 100, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_is_worker_work_with_zero_energy(self):
        worker = Worker('Test', 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_is_worker_money_are_raised(self):
        worker = Worker('Test', 100, 10)

        self.assertEqual(0, worker.money)
        worker.work()
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_is_worker_energy_decreased(self):
        worker = Worker('Test', 100, 10)

        worker.work()
        self.assertEqual(9, worker.energy)
        worker.work()
        self.assertEqual(8, worker.energy)

    def test_worker_get_info(self):
        worker = Worker('Test', 100, 10)

        result = worker.get_info()
        expected = 'Test has saved 0 money.'
        self.assertEqual(expected, result)

        worker.work()

        result = worker.get_info()
        expected = 'Test has saved 100 money.'
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
