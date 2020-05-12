from calculator import Calculator
from room import Room

calc = Calculator()

room = Room(
    input('Qual a largura do cômodo? '),
    input('Qual a profundidade do cômodo? ')
)

print(
    'A área das paredes é: ',
    calc.calculate_wall_area(
        room
    )
)

print(
    'A área do teto é: ',
    calc.calculate_roof_area(
        room
    )
)

print(
    'A litragem de tinta necessária é: ',
    calc.calculate_required_liter()
)
