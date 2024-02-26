from tabulate import tabulate

class Member:
    data_user = {
        'Rosy' : [5,8,'Gold'],
        'Agus' : [8,15,'Platinum'],
        'Ana' : [4,9,'Silver']
    }

    table_benefit = [
        ['Platinum', '15%', 0.15, 'Benefit Gold + Silver + Cashback'],
        ['Gold', '10%', 0.1, 'Benefit Silver + Voucher Ojek Online'],
        ['Silver', '8%', 0.08, 'Voucher Makanan']
    ]

    header_benefit = ['Membership', 'Monthly Expense (Juta)', 'Monthly Income (Juta)', 'Plan']

    table_requirement = [
        ['Platinum', 8, 15],
        ['Gold', 6, 10],
        ['Silver', 5, 7]
    ]

    header_requirement = ['Membership', 'Monthly Expense (Juta)', 'Monthly Income (Juta)', 'Plan']

    def __init__(self):
        self.username = None
        self.monthly_expense = None
        self.monthly_income = None
        self.member = None

    def login(self, username):
        if username in self.data_user:
            self.username == username
            self.monthly_expense = self.data_user[username][0]
            self.monthly_income = self.data_user[username][1]
            self.member = self.data_user[username][2]
        else:
            pass

    def register(self, username, monthly_expense, monthly_income):
        self.username = username
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income
        self.member = None
        self.data_user[username] = [monthly_expense, monthly_income, None]

    def show_benefit(self):
        print("Menampilkan Benefit Membership")
        print(tabulate(self.table_benefit, self.header_benefit))

    def show_requirement(self):
        print("Menampilkan Requirement Membership")
        print(tabulate(self.table_requirement, self.header_requirement))

    def menghitung_jarak(self, point1, point2):
        """
        Menggunakan Euclidean Distance
        """
        jarak = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
        return jarak
    
    def predict_user(self):
        distance = {}

        for req in self.table_requirement:
            type_membership = req[0]
            point_req = req[1:3]

            dist = self.menghitung_jarak([self.monthly_expense, self.monthly_income], point_req)
            distance[type_membership] = dist

        min_distance = min(distance, key = distance.get)
        self.member = min_distance
        self.data_user[self.username][2] = min_distance

    def calculate_total(self, list_belanja):
        """
        total_belanja = [100_000, 200_000, 10_000]
        """
        discount_member = [i[2] for i in self.table_benefit if i[0] == self.member]

        total = sum(list_belanja) - (discount_member[0]*sum(list_belanja))
        print(f'Total belanja setelah diskon {total}')


