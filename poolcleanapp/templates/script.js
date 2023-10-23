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
    });
    this.prevDiv.addEventListener("click", (_) => {
      this.removeMonth();
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
          this.bodyDivs[index].classList.add("cal-day__day--selected");
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