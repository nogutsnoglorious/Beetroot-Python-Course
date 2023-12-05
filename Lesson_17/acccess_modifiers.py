class Patient:
    def __init__(self, name, surname, doctor, weight, passport_number):
        self.name = name                    # public visibility
        self.surname = surname              # public —||—
        self.doctor = doctor                # public —||—
        self._weight = weight               # protected visibility
        self.__passport_number = passport_number   # private visibility

    def __private_method(self):
        pass


        # public
        # _protected
        # __private

