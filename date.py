class Date:
    dd = 2
    mm = 12
    yy = 2019

    def __init__(self, dd=2, mm=12, yy=2019):
        self.dd = dd
        self.mm = mm
        self.yy = yy

    def display(self):
        print(self.dd, self.mm, self.yy)

    def __repr__(self):
        """ In place of display - Operator overloading """
        print(str(self.dd), str(self.mm), str(self.yy))

    def calNewDate1(self, days):
        while self.dd > 31:
            if self.mm in [1, 3, 5, 7, 8, 10, 12] and self.dd > 31:
                """ Handle 31 days - month """
                self.dd -= 31
                self.mm += 1
            elif self.mm not in [1, 2, 3, 5, 7, 8, 10, 12] and self.dd > 30:
                """ Handle 30 days - month """
                self.dd -= 30
                self.mm += 1
            elif self.mm == 2:
                """ Handle Leap Year for Feb """
                if self.yy % 4 == 0 and self.dd > 29:
                    self.dd -= 29
                    self.mm += 1
                elif self.yy % 4 != 0 and self.dd > 28:
                    self.dd -= 28
                    self.mm += 1
            if self.mm == 13:
                self.mm = 1
                self.yy += 1
        return self

    def calNewDate2(self, days):
        while self.dd > 28:
            if self.mm in [1, 3, 5, 7, 8, 10, 12] and self.dd > 31:
                """ Handle 31 days - month """
                self.dd -= 31
                self.mm += 1
                if self.mm == 13:
                    self.mm = 1
                    self.yy += 1
            elif self.mm in [4, 6, 9, 11] and self.dd > 30:
                """ Handle 30 days - month """
                self.dd -= 30
                self.mm += 1
            elif self.mm == 2 and self.yy % 4 == 0 and self.dd > 29:
                """ Handle Leap Year for Feb """
                self.dd -= 29
                self.mm += 1

            elif self.mm == 2 and self.yy % 4 != 0 and self.dd > 28:
                """ Handle Non-Leap Year for Feb """
                self.dd -= 28
                self.mm += 1
            else:
                print("There is a problem: ", self.dd, self.mm, self.yy)
                return self
        return self

    def __add__(self, days):
        self.dd += days
        # self.calNewDate1(days)
        # print("Dates from method1: ")
        # self.display()
        self.calNewDate2(days)
        # print("Dates from method2: ")
        # self.display()
        return self

    def __iter__(self):
        self.dd = 1
        return self

    def __next__(self):
        x = self.dd, self.mm, self.yy
        self + 1
        return x


def testFor50Days(dd, mm, yy):
    counter = 1
    day = Date(dd, mm, yy)
    while counter <= 50:
        day = day+1
        day.display()
        counter += 1
    else:
        print("Counter is finished, date now: {}".format(otherDay.display()))


if __name__ == '__main__':
    today = Date()
    today.display()
    # print(today.dd, today.mm, today.yy)
    otherDay = Date(1, 12, 2019)
    otherDay.display()

    tomo = today + 5000
    tomo.display()

    testFor50Days(1, 12, 2019)
    # print(today)
