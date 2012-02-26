# Create your views here.
import time
from apps.calendar_app.models import Entry
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
import calendar
from MySQLdb.times import TimeDelta
from django.forms.models import modelformset_factory
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect


mnames = 'January February March April May June July August September  October November December'
mnames = mnames.split()
date = ()
import datetime

@login_required
def main(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year, year+1, year+2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # are there entry(s) for this month; current month?
            entries = Entry.objects.filter(date__year=y, date__month=n+1)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(current=current,  entry=entry, name=month, n=n+1 ))
        lst.append((y, mlst))
    
    return render_to_response('calendar/calendar_page.html', dict(years=lst, user=request.user, year=year, reminders=reminders(request)),
                              context_instance=RequestContext(request))

@login_required
def month(request, year, month, change=None):
    """Listing of days in `month`."""
    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = datetime.datetime(year, month, 15), TimeDelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]

    # init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    nyear, nmonth, nday = time.localtime()[:3]
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        if day:
            entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day)
            if day == nday and year == nyear and month == nmonth:
                current = True

        lst[week].append((day, entries, current))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1
    return render_to_response('calendar/month.html', dict(year=year, month=month, user=request.user,month_days=lst, mname=mnames[month-1], reminders=reminders(request)),
                              context_instance=RequestContext(request))
@login_required
def day(request, year, month, day):
    """Entries for the day."""

    EntriesFormset = modelformset_factory(Entry, extra=1, exclude=("creator", "date"),
                                          can_delete=True)

    if request.method == 'POST':
        formset = EntriesFormset(request.POST)
        if formset.is_valid():
            # add current user and date to each entry & save
            entries = formset.save(commit=False)
            for entry in entries:
                entry.creator = request.user
                print year,month,day
                entry.date = datetime.datetime(int(year),int(month),int(day))
                entry.save()
            return HttpResponseRedirect(reverse("month", args=(year, month)))

    else:
        # display formset for existing enties and one extra form
        formset = EntriesFormset(queryset=Entry.objects.filter(date__year=year,
            date__month=month, date__day=day, creator=request.user))
    return render_to_response("calendar/day.html", add_csrf(request, entries=formset, year=year,
            month=month, day=day), context_instance=RequestContext(request))


def add_csrf(request, ** kwargs):
    """Add CSRF and user to dictionary."""
    d = dict(user=request.user, ** kwargs)
    d.update(csrf(request))
    return d

def reminders(request):
    """Return the list of reminders for today and tomorrow."""
    year, month, day = time.localtime()[:3]
    #print time.localtime()[:3]
    reminders = Entry.objects.filter(date__year=year, date__month=month,
                                   date__day=day, creator=request.user, remind=True)
    tomorrow = datetime.datetime.now() + TimeDelta(days=1)
    year, month, day = tomorrow.timetuple()[:3]
    return list(reminders) + list(Entry.objects.filter(date__year=year, date__month=month,
                                   date__day=day, creator=request.user, remind=True))
