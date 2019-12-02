import requests


def main():
    print("--------LEASE SEARCH---------")

    # filters
    make = "BMW"
    model = "M4"
    maxMonthlyCost = "1000"
    maxMonths = "16"

    leaseTraderApi = "https://api.leasetrader.com/api/Lease/SearchData/"
    requestJson = {"UserId": 0, "searchKey": "", "Searchtype": "", "searchprocess": "", "yearTo": 0, "sortby": "",
                   "sorttype": "Payment_low", "sortorder": "", "rowcount": 12, "yearlist": [], "miles": 0, "MonthPay": 0, "MilesPM": 0,
                   "makelist": [make], "stylelistdata": "", "stylelist": [], "modellist": [model], "statelist": [], "colorlist": [],
                   "categorylist": [], "TypeList": "", "pagenumber": 0, "make": 0, "car_model": 0, "year": 0, "Zip": "", "Type": 0,
                   "newused": 0, "Vstyle": 0, "series": 0, "fromyr": 0, "YearTo": 0, "Maxmonth": maxMonths, "Minmonth": "0",
                   "incentives": False, "MonthR": 0, "Zipcode": 0, "budgetfrom": 0, "budgetto": 0, "DealerList": True, "Lnumber": 0,
                   "FuelEff": "", "EngineId": 0, "FulesV": 0, "Vdoor": 0, "Tranmission": 0, "Dtrain": 0, "Advyear": 0, "AdvToyear": 0,
                   "currentPage": 1, "searchval": "", "Param": "Search", "MoreType": "", "StatusType": "", "MinMonthPay": "",
                   "MaxMonthPay": maxMonthlyCost, "fuellist": [], "enginelist": [], "transmissionlist": [], "drivetrainlist": [], "listingId": "",
                   "list_searchType": [], "country": "", "state": "", "city": "", "latitude": "", "longitude": "",
                   "IP_Address": "2605:6000:151c:86d5:f880:52ee:380f:78ed"}
    # call api
    response = requests.post(url=leaseTraderApi, json=requestJson)
    # extract list of cars
    cars = response.json()['Data']['AllCarList']

    # filter cars under $1000 a month and sort cheapest to most expensive
    # not needed, api has this filter
    # carsUnder900 = list(filter(lambda x: float(x['monthlypayment'].replace(',', '')) < 1000.0, cars))
    cars = sorted(cars, key=lambda x: x['monthlypayment'])

    # print stats
    print(cars)
    print()
    print(len(cars), "{} {}s under ${} per month".format(make, model, maxMonthlyCost))
    print("{:20}    {:20}   {:15}   {:23}".format("Monthly Payment", "Lease End Date", "Miles Per Month", "Url"))
    for car in cars:
        print("{:20}    {:20}   {:15}   {:23}".format(car['monthlypayment'], car['LeaseEndFullDate'], car['MilesPerMonth'], "https://www.leasetrader.com/listing/{}".format(car['Url'])))


if __name__ == "__main__":
    main()
