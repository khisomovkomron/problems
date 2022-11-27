import random
import string
from dataclasses import dataclass, field


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
    
    def __post_init__(self) -> None:
        self._search_string = f'{self.name} {self.address}'
    

if __name__ == '__main__':
    
    person = Person(name='Komron', address='1237 Streend Downtown')
    # person = Person('Komron', '1237 Streend Downtown') # with kw_only=True this will not work
    # person.name = 'John' # with frozen=True this will not work
    # print(person['name'])
    print(person)