const appointments = JSON.parse(document.getElementById("appointments").textContent);

var currentDay = Date();

// compares a string with format "mm/dd/yyyy" to a Date variable
function isSameDay(dateStr, dateVar) {
  const options = {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  };
  return dateStr == dateVar.toLocaleDateString('en-US', options);
}

// logic for how to offset the y-coord when putting task in daily view
function dayViewMinuteOffset(minute) {
  if (minute >= 0 && minute < 15) {
    return 0;
  }
  if (minute >= 15 && minute < 30) {
    return 1;
  }
  if (minute >= 30 && minute < 45) {
    return 2;
  }
  else {
    return 3;
  }
}

// takes in a string of HH:MM in military time,
// and returns it as HH:MM A.M/P.M
function militaryToRegular(time) {
  // assume am
  period = "A.M";
  leading = ""
  // get hour as integer
  hour = parseInt(time.substring(0,2))

  if (hour >= 12)
    period = "P.M";

  if (hour > 12)
    hour -= 12;

  if (hour < 10)
    leading = "0";

  return leading + hour + time.substring(2) + " " + period;
}

// create a cell in the daily view with the name of appointment,
// the time, have the time be in the right location
// NOTE: temporaily each appointment is 30 minutes in length
// day: Date variable of the day of appointments
function printSelectedApts(day) {
  // reset daily task
  var container = document.getElementById('dayTask');
  container.innerHTML = '';

  for (var apt of appointments) {
    if (!isSameDay(apt.appdate, day)) {
      continue;
    }
    // create div for appointment
    var div = document.createElement('div');

    // figure out location of div
    var hour = parseInt(apt.apptime.substring(0, 2));
    var min = parseInt(apt.apptime.substring(3, 5));
    var timeLocStart = hour * 4 + 1 + dayViewMinuteOffset(min);
    var timeLocEnd = timeLocStart + 2;
    // set attributes
    div.style.gridRow = timeLocEnd + " / " + timeLocStart;
    div.className = "dayview-cell";

    // populate data in cell
    var divTitle = document.createElement('div');
    divTitle.className = "dayview-cell-title";
    divTitle.textContent = apt.cname + "'s Appointment";

    var divTime = document.createElement('div');
    divTime.className = "dayview-cell-time";
    divTime.textContent = militaryToRegular(apt.apptime);

    div.appendChild(divTitle);
    div.appendChild(divTime);
    container.appendChild(div);
  }
}

class Calendar {
  constructor() {
    this.monthDiv = document.querySelector(".cal-month__current");
    this.headDivs = document.querySelectorAll(".cal-head__day");
    this.bodyDivs = document.querySelectorAll(".cal-body__day");
    this.nextDiv = document.querySelector(".cal-month__next");
    this.prevDiv = document.querySelector(".cal-month__previous");
  }

  init() {
    moment.locale(window.navigator.userLanguage || window.navigator.language);

    this.month = moment();
    this.today = this.selected = this.month.clone();
    this.weekDays = moment.weekdaysShort(true);

    this.headDivs.forEach((day, index) => {
      day.innerText = this.weekDays[index];
    });

    this.nextDiv.addEventListener("click", (_) => {
      this.addMonth();
      this.addIndicator();
    });
    this.prevDiv.addEventListener("click", (_) => {
      this.removeMonth();
      this.addIndicator();
    });

    this.bodyDivs.forEach((day) => {
      day.addEventListener("click", (e) => {
        const date =
          +e.target.innerHTML < 10
            ? `0${e.target.innerHTML}`
            : e.target.innerHTML;

        if (e.target.classList.contains("cal-day__month--next")) {
          this.selected = moment(
            `${this.month.add(1, "month").format("YYYY-MM")}-${date}`
          );
        } else if (e.target.classList.contains("cal-day__month--previous")) {
          this.selected = moment(
            `${this.month.subtract(1, "month").format("YYYY-MM")}-${date}`
          );
        } else {
          this.selected = moment(`${this.month.format("YYYY-MM")}-${date}`);
        }

        this.update();
      });
    });

    this.update();

    // add indicator
    this.addIndicator();
  }

  update() {
    this.calendarDays = {
      first: this.month.clone().startOf("month").startOf("week").date(),
      last: this.month.clone().endOf("month").date()
    };

    this.monthDays = {
      lastPrevious: this.month
        .clone()
        .subtract(1, "months")
        .endOf("month")
        .date(),
      lastCurrent: this.month.clone().endOf("month").date()
    };

    this.monthString = this.month.clone().format("MMMM YYYY");

    this.draw();
  }

  // changes color of a day in Calendar to green to signify
  // there are appointments for that day.
  addIndicator() {
    // variables to keep track of only 1-31 of selected month
    // and not the days of other months.
    var startSearching = 0;
    var prev = 0;

    // iterate through each day of calendar
    this.bodyDivs.forEach((day) => {
      // reset colors
      if (day.classList.contains("cal-day__day--indicator")) {
        day.classList.remove("cal-day__day--indicator");
      }
      // only start searching when we look at the first day of month
      if (startSearching == 0 && day.innerText == 1) {
        startSearching = 1;
      }
      if (startSearching == 1) {
        for (var apt of appointments) {
          if (parseInt(apt.appdate.substring(3, 5)) == day.innerText &&
          (parseInt(apt.appdate.substring(0, 2)) - 1) == this.month.month() &&
          prev < day.innerText) {
            day.classList.add("cal-day__day--indicator"); 
          }
        }
        prev = day.innerText;
      }
    });
  }

  addMonth() {
    this.month.add(1, "month");

    this.update();
  }

  removeMonth() {
    this.month.subtract(1, "month");

    this.update();
  }

  draw() {
    this.monthDiv.innerText = this.monthString;

    let index = 0;

    if (this.calendarDays.first > 1) {
      for (
        let day = this.calendarDays.first;
        day <= this.monthDays.lastPrevious;
        index++
      ) {
        this.bodyDivs[index].innerText = day++;

        this.cleanCssClasses(false, index);

        this.bodyDivs[index].classList.add("cal-day__month--previous");
      }
    }

    let isNextMonth = false;
    for (let day = 1; index <= this.bodyDivs.length - 1; index++) {
      if (day > this.monthDays.lastCurrent) {
        day = 1;
        isNextMonth = true;
      }

      this.cleanCssClasses(true, index);

      if (!isNextMonth) {
        if (day === this.today.date() && this.today.isSame(this.month, "day")) {
          this.bodyDivs[index].classList.add("cal-day__day--today");
        }

        if (
          day === this.selected.date() &&
          this.selected.isSame(this.month, "month")
        ) {
          this.addIndicator();
          this.bodyDivs[index].classList.add("cal-day__day--selected");
          this.bodyDivs[index].classList.remove("cal-day__day--indicator");
          printSelectedApts(this.selected.toDate());
        }

        this.bodyDivs[index].classList.add("cal-day__month--current");
      } else {
        this.bodyDivs[index].classList.add("cal-day__month--next");
      }

      this.bodyDivs[index].innerText = day++;
    }
  }

  cleanCssClasses(selected, index) {
    this.bodyDivs[index].classList.contains("cal-day__month--next") &&
      this.bodyDivs[index].classList.remove("cal-day__month--next");
    this.bodyDivs[index].classList.contains("cal-day__month--previous") &&
      this.bodyDivs[index].classList.remove("cal-day__month--previous");
    this.bodyDivs[index].classList.contains("cal-day__month--current") &&
      this.bodyDivs[index].classList.remove("cal-day__month--current");
    this.bodyDivs[index].classList.contains("cal-day__day--today") &&
      this.bodyDivs[index].classList.remove("cal-day__day--today");
    if (selected) {
      this.bodyDivs[index].classList.contains("cal-day__day--selected") &&
        this.bodyDivs[index].classList.remove("cal-day__day--selected");
    }
  }
}

const cal = new Calendar();
cal.init();


$("cal-month__previous").on("click",function(){
  $(this).addClass("clicked");
})

setTimeout(()=>{cal-month__previous.classList.remove("clicked")},1500);

$("cal-month__next").on("click",function(){
  $(this).addClass("clicked");
})

setTimeout(()=>{cal-month__next.classList.remove("clicked")},1500);


