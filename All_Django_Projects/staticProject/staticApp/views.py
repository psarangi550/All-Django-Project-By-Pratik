from django.shortcuts import render
import datetime
import pytz
# Create your views here.
def home_view(request):
    # dt_arizona=datetime.datetime.now(tz=pytz.timezone("US/Arizona"))
    dt_india = datetime.datetime.now()
    tz_arizona=pytz.timezone("US/Arizona")
    dt1=datetime.datetime.now()
    dt2=tz_arizona.localize(dt1)
    dt_arizona=dt2.now().astimezone(tz_arizona)
    my_dict={"arizona":dt_arizona, "india":dt_india}
    return render(request, "staticApp/home.html",context=my_dict)
def profile_view(request):
    return render(request, "staticApp/profile.html")
# print( datetime.datetime.now(tz=pytz.timezone("Asia/Kolkata")))
# print(pytz.all_timezones)
for tz in pytz.all_timezones:
    print(tz)