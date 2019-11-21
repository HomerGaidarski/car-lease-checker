import requests


def main():
    print("--------STARTING LEASE SEARCH---------")
    leaseTraderApi = "https://api.leasetrader.com/api/Lease/SearchData/"
    requestJson = {"UserId": 0, "searchKey": "bmw m4", "Searchtype": "", "searchprocess": "", "yearTo": 0, "sortby": "",
                   "sorttype": "", "sortorder": "", "rowcount": 12, "yearlist": [], "miles": 0, "MonthPay": 0,
                   "MilesPM": 0, "makelist": [], "stylelistdata": "", "stylelist": [], "modellist": [], "statelist": [],
                   "colorlist": [], "categorylist": [], "TypeList": "", "pagenumber": 0, "make": 0, "car_model": 0,
                   "year": 0, "Zip": "", "Type": 0, "newused": 0, "Vstyle": 0, "series": 0, "fromyr": 0, "YearTo": 0,
                   "Maxmonth": "", "Minmonth": "", "incentives": False, "MonthR": 0, "Zipcode": 0, "budgetfrom": 0,
                   "budgetto": 0, "DealerList": True, "Lnumber": 0, "FuelEff": "", "EngineId": 0, "FulesV": 0,
                   "Vdoor": 0, "Tranmission": 0, "Dtrain": 0, "Advyear": 0, "AdvToyear": 0, "currentPage": 1,
                   "searchval": "", "Param": "Search", "MoreType": "", "StatusType": "", "MinMonthPay": "",
                   "MaxMonthPay": "", "fuellist": [], "enginelist": [], "transmissionlist": [], "drivetrainlist": [],
                   "listingId": "", "list_searchType": [], "country": "", "state": "", "city": "", "latitude": "",
                   "longitude": "", "IP_Address": "2605:6000:151c:86d5:493e:93c8:3406:5c09"}
    response = requests.post(url=leaseTraderApi, json=requestJson)
    print(response.json())


if __name__ == "__main__":
    main()
