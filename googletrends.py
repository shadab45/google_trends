from pytrends.request import TrendReq

trends = TrendReq()

enter_name = input("search here  : ")

trends.build_payload(kw_list=[enter_name])
data = trends.interest_by_region()
data = data.sort_values(by=enter_name, ascending=False)
data = data.head(5)

print(data)
