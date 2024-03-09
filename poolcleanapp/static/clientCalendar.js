// temp fake data
var fakeProvider = {
    name: "Company #1"
  };
  
  // NOTE: fake data as only one apptime, but model has separate variables
  // for the date and the time.
  var appointments = [
    {
      apptime: new Date(2024, 1, 26, 9, 0, 0),
      cl: "John Doe",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 26, 10, 30, 0),
      cl: "Adam Smith",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 26, 13, 0, 0),
      cl: "David Johnson",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 26, 14, 30, 0),
      cl: "Emily Wilson",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 26, 15, 15, 0),
      cl: "James Anderson",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 26, 16, 30, 0),
      cl: "Ashley Martinez",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 27, 10, 0, 0),
      cl: "Jeff Daniels",
      provider: fakeProvider
    },
    {
      apptime: new Date(2024, 1, 25, 12, 0, 0),
      cl: "Sarah Troop",
      provider: fakeProvider
    }
  ];
  
  
  var currentDay = Date();
  
  // compares 2 Date variables if they land on the same month, day and year
  function isSameDay(date1, date2) {
    return date1.getFullYear() === date2.getFullYear() &&
           date1.getMonth() === date2.getMonth() &&
           date1.getDate() === date2.getDate();
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
  
  // create a cell in the daily view with the name of appointment,
  // the time, have the time be in the right location
  // NOTE: temporaily each appointment is 30 minutes in length
  // day: Date variable of the day of appointments
  function printSelectedApts(day) {
    // reset daily task
    var container = document.getElementById('dayTask');
    container.innerHTML = '';
  
    for (var apt of appointments) {
      if (!isSameDay(apt.apptime, day)) {
        continue;
      }
      // create div for appointment
      var div = document.createElement('div');
  
      // figure out location of div
      var hour = apt.apptime.getHours();
      var min = apt.apptime.getMinutes();
      var timeLocStart = hour * 4 + 1 + dayViewMinuteOffset(min);
      var timeLocEnd = timeLocStart + 2;
      // set attributes
      div.style.gridRow = timeLocEnd + " / " + timeLocStart;
      div.className = "dayview-cell";
  
      // populate data in cell
      var divTitle = document.createElement('div');
      divTitle.className = "dayview-cell-title";
      divTitle.textContent = apt.cl + "'s Appointment.";
  
      var divTime = document.createElement('div');
      divTime.className = "dayview-cell-time";
      divTime.textContent = apt.apptime.toLocaleTimeString().substring(0, apt.apptime.toLocaleTimeString().length - 6);
  
      div.appendChild(divTitle);
      div.appendChild(divTime);
      container.appendChild(div);
    }
  }
  
  class Calendar {
    constructor() {
      this.monthDiv = document.querySelector(".cal-month__current");
      this.headDivs = document.querySelectorAll(".cal-head__day");
      this.bodyDivs = document.querySelectorAll(".cal-body__day");   ////////////////
      this.nextDiv = document.querySelector(".cal-month__next");
      this.prevDiv = document.querySelector(".cal-month__previous");
  
      this.selectedDay = null; // Initialize selected day as null
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
  
  // Update selected day
        this.selectedDay = this.selected;
  // Call function to display timings
      displayTimings(); 
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
            if (apt.apptime.getDate() == day.innerText &&
            apt.apptime.getMonth() == this.month.month() &&
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
  
  
  
  
  
  // Define array of available timings
  var timings = [
    "12:00", "12:30",
    "1:00", "1:30",
    "2:00", "2:30",
    "3:00", "3:30",
    "4:00", "4:30",
    "5:00", "5:30",
    "6:00", "6:30",
    "7:00", "7:30"
  ];

    // Define array of scheduled timings
  var scheduledTimings = [
    "1:00", "3:30",
    "4:30", "6:00" 
  ];
  
// Function to display timings when a day is selected
function displayTimings() {
    const timingsContainer = document.querySelector('.timings-buttons');
    const submit = document.querySelector('.schedule');
    timingsContainer.innerHTML = ''; // Clear previous buttons
    submit.disabled = true; // Disable the schedule button initially
  
    // Check if a day is selected
    if (cal.selectedDay !== null) {
      // Generate timing buttons
      timings.forEach(timing => {
        const button = document.createElement('button');
        button.textContent = timing;
        button.classList.add('schedule');
        timingsContainer.appendChild(button);
        button.disabled = false;
  
        // Add event listener to change color on click
        button.addEventListener('click', () => {
          button.classList.toggle('selected'); // Toggle selected class on click
  
          if (button.classList.contains('selected')) {
            submit.disabled = false; // Enable the schedule button when a timing is selected
            submit.classList.add('selected'); // Add the 'selected' class to the submit button
          } else {
            submit.disabled = true; // Disable the schedule button when no timing is selected
            submit.classList.remove('selected'); // Remove the 'selected' class from the submit button
          }
        });
  
        // Check if a timing is already scheduled, if so disable it from being chosen again. 
        const isScheduled = scheduledTimings.some(pair => {
          const [start, end] = pair.split('-');
          return timing === start || timing === end;
          
        });
  
        if (isScheduled) {
          button.classList.add('scheduled');
          button.disabled = true;
          button.classList.add('scheduled');
          submit.disabled = true;
        }
      });
    }
  }


 

