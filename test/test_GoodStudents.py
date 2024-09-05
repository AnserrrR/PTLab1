# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.GoodStudents import GoodStudents


class TestGoodStudents:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, int]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100)
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97)
            ],
            "Сидоров Иван Николаевич": [
                ("математика", 90),
                ("русский язык", 85),
                ("физика", 88)
            ],
            "Кузнецова Мария Викторовна": [
                ("математика", 55),
                ("химия", 72)
            ]
        }
        expected_good_students_count = 2
        return data, expected_good_students_count

    def test_init_good_students(self,
                                input_data: tuple[DataType, int]) -> None:
        good_students = GoodStudents(input_data[0])
        assert input_data[0] == good_students.data

    def test_calc_good_students(self,
                                input_data: tuple[DataType, int]) -> None:
        good_students = GoodStudents(input_data[0])
        good_students_count = good_students.calc()
        assert good_students_count == input_data[1]
