import random
import string
from dataclasses import dataclass, field, astuple, asdict, make_dataclass, replace


def generate_id() -> str:
    
    return ''.join(random.choices(string.ascii_letters, k=12))

# @dataclass
@dataclass(slots=True) # slots does not work like dict, it removes keys and stores only variables
# @dataclass(kw_only=True) # does not allow to instantiate class with only args, need to add keywords
# @dataclass(frozen=True) # 3does not allow to add new variables to class)
class Person:
    
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)
    # phone: tuple[int] = astuple(tuple_factory=tuple)
    
    def __post_init__(self) -> None:
        self._search_string = f'{self.name} {self.address}'
    
    
NewPerson = make_dataclass(cls_name='New_person', fields=['name', 'address'], init=True, repr=True)

if __name__ == '__main__':
    new_person = NewPerson(name='Farish', address='1234 Street Downtown')
    person = Person(name='Komron', address='1237 Street Downtown')
    # person = Person('Komron', '1237 Streend Downtown') # with kw_only=True this will not work
    # person.name = 'John' # with frozen=True this will not work
    # print(person['name'])
    print(astuple(person))
    print(asdict(person))
    print(person)
    
    print(new_person)
    new1_person = replace(new_person, name='Komron')
    print(new1_person)
    new1_person.name = 'Farish'
    print(new1_person)
    setattr(new1_person, 'address', 'name')
    getattr(new1_person, 'address')
    print(getattr(new1_person, 'address'))
    # delattr(new1_person, 'address')
    print(new1_person.name)

    