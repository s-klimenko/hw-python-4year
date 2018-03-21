class UniqObject:
    instance = None

    def __init__(self):
        if self.instance:
            print('instance already exists')


    @classmethod
    def create_object(cls):
        if not cls.instance:
            cls.instance = UniqObject()
        return cls.instance


obj1 = UniqObject()
print(obj1.create_object())
obj2 = UniqObject()
print(obj2.create_object())
