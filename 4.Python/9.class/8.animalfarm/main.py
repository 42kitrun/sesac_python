from farm import Farm
from cat import Cat
from dog import Dog

if __name__ == "__main__":
    dog = Dog('Buddy')
    cat = Cat('Kitty')
    farm = Farm('seSAC')

    farm.add_animals(dog)
    farm.add_animals(cat)

    dog.speak()
    cat.speak()

    dog.move(2)
    cat.move(3)

    print(dog)
    print(cat)
    
    # Pythonic (파이썬 스러운~)
    for _ in range(10):
        dog.move()
        cat.move()
    
    farm.feed_all(10)

    # farm.show_all()

