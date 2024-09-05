# -*- coding: utf-8 -*-
from Types import DataType


class GoodStudents:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.count: int = 0

    def calc(self) -> DataType:
        self.count = 0
        for key in self.data:
            self.count += 1
            for subject in self.data[key]:
                if subject[1] < 76:
                    self.count -= 1
                    break

        return self.count
