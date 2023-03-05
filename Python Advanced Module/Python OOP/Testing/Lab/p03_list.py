class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):

    def test_is_initialized_int_list(self):
        integer = IntegerList()
        self.assertEqual([], integer._IntegerList__data)

    def test_initialized_with_wrong_data_type(self):
        integer = IntegerList('asd', 5.2, 6.9)
        self.assertEqual([], integer._IntegerList__data)

    def test_initialized_with_correctly_data_type(self):
        integer = IntegerList(9, 'asd')
        self.assertEqual([9], integer._IntegerList__data)

    def test_get_data(self):
        integer = IntegerList(9, 'asd')
        self.assertEqual([9], integer._IntegerList__data)

        result = integer.get_data()
        self.assertEqual([9], result)

    def test_add_method_with_wrong_data_type(self):
        integer = IntegerList(9)
        self.assertEqual([9], integer._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            integer.add('5')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_method_with_correct_data_type(self):
        integer = IntegerList(9)
        self.assertEqual([9], integer._IntegerList__data)

        integer.add(10)
        self.assertEqual([9, 10], integer._IntegerList__data)

    def test_removes_el_on_given_index(self):
        integer = IntegerList(9)
        integer.remove_index(0)
        self.assertEqual([], integer._IntegerList__data)


    def test_removes_el_on_invalid_index(self):
        integer = IntegerList([9])

        with self.assertRaises(IndexError) as ex:
            integer.remove_index(2)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_element_at_the_removed_index(self):
        integer = IntegerList(9)
        result = integer.remove_index(0)
        self.assertEqual(9, result)

    def test_get_with_invalid_index(self):
        integer = IntegerList(9)

        with self.assertRaises(IndexError) as ex:
            # greater than length
            integer.get(2)
        self.assertEqual('Index is out of range', str(ex.exception))

        with self.assertRaises(IndexError) as ex:
            # equal to length
            integer.get(1)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_with_valid_index(self):
        integer = IntegerList(9)

        result = integer.get(0)
        self.assertEqual(9, result)

    def test_insert_data_invalid_index(self):
        integer = IntegerList(9)

        with self.assertRaises(IndexError) as ex:
            integer.insert(2, 10)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_data_with_invalid_data(self):
        integer = IntegerList(9)

        with self.assertRaises(ValueError) as ex:
            integer.insert(0, '10')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert_adds_element(self):
        integer = IntegerList(5)

        integer.insert(0, 10)
        self.assertEqual([10, 5], integer._IntegerList__data)

    def test_get_biggest(self):
        integer = IntegerList(5, 0, -8, -941, 100, 90)

        result = integer.get_biggest()
        self.assertEqual(100, result)

    def test_get_index(self):
        integer = IntegerList(5, 2, -8, -941, 100, 90)

        result = integer.get_index(2)
        self.assertEqual(1, result)


if __name__ == '__main__':
    main()
