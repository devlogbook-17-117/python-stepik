class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Перебираем элементы списка по очереди.
        for i in range(len(nums)):
            # Ищем второй элемент, начиная со следующего,
            # чтобы не использовать один и тот же элемент дважды.
            for j in range(i + 1, len(nums)):
                # Проверяем, равна ли сумма двух элементов target.
                if nums[i] + nums[j] == target:
                    # Возвращаем индексы найденных элементов.
                    return [i, j]