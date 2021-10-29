# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
from typing import List, Tuple, Union

my_family = ['father', 'mother', 'son']

# список списков приблизителного роста членов вашей семьи
my_family_height = ['father', 183], ['mother', 165], ['son', 95]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('rost ' + my_family[0] + ' ', my_family_height[0][1], 'cm')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum_height = 0
sum_height += my_family_height[0][1]
sum_height += my_family_height[1][1]
sum_height += my_family_height[2][1]
print(sum_height)
