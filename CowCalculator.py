class CowCalculator(object):
    def __init__(self, cow_data=None, cow_increment=0, cow_buy=0, money_total=0):

        if cow_data is None:
            cow_data = []


        self.cow_increment = cow_increment
        self.cow_buy = cow_buy

        self.money_total = money_total

        self.adult_cow_data_total = cow_data

        self.adult_cow_total = int()
        self.child_cow_total = int()

        # ADULT_COW_COUNTING
        b = 0
        for a in self.adult_cow_data_total:
            b = b + 1

        self.adult_cow_total = b


        # NEW_ADULT_COW_DATA ADDING_TO OLD_ADULT_COW_DATA
        for a in range(self.adult_cow_total + 1, self.cow_increment + self.cow_buy + 1):
            self.new_cow_data = {"cow_number": a,
                                 "cow_age": 36,
                                 "cow_adult": True,
                                 "cow_child": False,
                                 "milk_age": 0}
            self.adult_cow_data_total.append(self.new_cow_data)
            pass

        # ADULT_COW_COUNTING
        b = 0
        for a in self.adult_cow_data_total:
            b = b + 1

        # NEW_CHILD_COW_DATA ADDING_TO OLD_CHILD_COW_DATA
        for a in range(self.adult_cow_total + 1, self.cow_increment + self.cow_buy + 1):
            self.new_cow_data = {"cow_number": a,
                                 "cow_age": 0,
                                 "cow_adult": False,
                                 "cow_child": True,
                                 "milk_age": 0}
            self.adult_cow_data_total.append(self.new_cow_data)
            pass

        self.active_cow = int()
        self.new_baby_cow = int()

        # ADULT_COW_DATA_UPDATING
        for k in self.adult_cow_data_total:

            k["cow_age"] += 1

            if k["cow_age"] > 36:
                k["cow_adult"] = True
                k["cow_child"] = False

            if k["cow_adult"]:
                k["milk_age"] += 1
                if k["milk_age"] < 10:
                    self.active_cow += 1

            if k["milk_age"] == 14:
                self.new_baby_cow += 1
                k["milk_age"] = 0



        income = self.money_total + self.active_cow * 20000
        use = self.child_cow_total * 1000 + self.adult_cow_total * 9000
        self.money_total = income - use

    def returning_method(self):
        aa2 = self.adult_cow_data_total
        aa3 = self.cow_increment
        aa4 = self.cow_buy
        aa5 = self.money_total
        aa6 = self.adult_cow_total
        return aa2, aa3, aa4, aa5, aa6
