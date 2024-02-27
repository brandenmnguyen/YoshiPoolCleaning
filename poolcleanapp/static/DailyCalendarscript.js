<!doctype html>
{% load static %}
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" 
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script defer src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <link href='{% static "payment_page.css" %}' rel="stylesheet">
    <title>Payment</title>
  </head>
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
    this.bodyDivs = document.querySelectorAll(".cal-body__day");
    this.nextDiv = document.querySelector(".cal-month__next");
    this.prevDiv = document.querySelector(".cal-month__previous");
  }

  <script>
    document.addEventListener("DOMContentLoaded", function() {
        document.getElementById('submitButton').addEventListener('click', function() {
            document.getElementById('paymentMethod').submit()
            document.getElementById('cardInfo').submit()
        });
    })

    function showAdditionalForm() {
        var additionalForm = document.getElementById('cardInfo');
        additionalForm.style.display = 'block';

        var radioButtons = document.getElementsByName('option');
        for (var i = 0; i < radioButtons.length; i++) {
            radioButtons[i].addEventListener('click', function() {
                if (this.value !== 'manualCard') {
                    additionalForm.style.display = 'none';
                }
            })
        }
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
  </script>

  <body>
    <div class="row align-items-center d-flex" style="height: 100vh; background-image: url('PaymentImage.png');">
        <div class="col-md-12 col-lg-8">
            <form method="POST" id="paymentMethod" name="paymentMethod">
                {% csrf_token %}
                <div>
                    <div class="shadow form-check payment-option mt-5 mx-4">
                        <input type="radio" class="form-check-input" name="option" id="option1" value="paypal">
                        <label class="form-check-label" for="option1">
                        <img src="{% static "PayPal.svg.png" %}" alt="PayPal">
                        </label>
                    </div>
                    <div class="shadow form-check payment-option mt-5 mx-4">
                        <input type="radio" class="form-check-input" name="option" id="option2" value="googlePay">
                        <label class="form-check-label" for="option2">
                        <img src="{% static "Google_Pay_Logo.svg.png" %}" alt="Google Pay">
                        </label>
                    </div>
                    <div class="shadow form-check payment-option mt-5 mx-4">
                        <input type="radio" name="option" id="option3" class="form-check-input" value="applePay">
                        <label class="form-check-label" for="option3">
                        <img src="{% static "2560px-Apple_Pay_logo.svg.png" %}" alt="Apple Pay">
                        </label>
                    </div>
                    <div class="shadow form-check payment-option my-5 mx-4">
                        <input type="radio" name="option" id="option4" value='manualCard' class="form-check-input" onclick="showAdditionalForm()">
                        <label class="form-check-label" for="option4">
                        <img src="{% static "Visa_Inc._logo.svg.png" %}" alt="Visa" style="height: 30px;">
                        <img src="{% static "Mastercard-logo.svg.png" %}" alt="MasterCard">
                        <img src="{% static "2560px-Discover_Card_logo.svg.png" %}" alt="Discover" style="height: 17px;">
                        <img src="{% static "American_Express_logo_(2018).svg" %}" alt="American Express">
                        </label>
                        <div id="cardInfo" style="display: none;">
                            <div class="mt-4 form-group row">
                                <label for="cardNumber" class="mb-3 col-sm-3 col-form-label" style="text-align: right;">Credit/Debit Number</label>
                                <div class="col-sm-8">
                                    <input type="text" class="form-control" id="cardNumber" name="card_number" placeholder="**** **** **** ****">
                                </div>
                            </div>
                            <div class="mb-3 form-group row">
                                <label for="cardName" class="col-sm-3 col-form-label" style="text-align: right;">Card Name</label>
                                <div class="col-sm-8">
                                    <input type="text" class="form-control" id="cardName" name="card_name">
                                </div>
                            </div>
                            <div class="mb-3 form-group row">
                                <label for="expDate" class="col-sm-2 offset-sm-2 col-form-label" style="text-align: right;">Expiry Date</label>
                                <div class="col-sm-2">
                                    <input type="text" class="form-control" id="expDate" name="exp_date" placeholder="MM/YY">
                                </div>
                                <label for="secCode" class="col-sm-2 col-form-label" style="text-align: center;" style="text-align: right;">Secturity Code (CCV)</label>
                                <div class="col-sm-2">
                                    <input type="text" class="form-control" id="secCode" name="ccv" placeholder="***">
                                </div>
                            </div>
                            <div class="mb-3 form-group row">
                                <label for="email" class="col-sm-3 col-form-label" style="text-align: right;">Email Address</label>
                                <div class="col-sm-8">
                                    <input type="email" class="form-control" name="card_email" id="email">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </div>

        <div class="col-lg-4">
            {% if msg %}
            <div class="container">
                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                    {{ msg }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            </div>
            {% endif %}

            <div class="shadow order-summary row my-5 mx-4">
                <h4 class="text-center mb-3 mt-3">
                    <span class="order-title fs-1">Order<br>Summary</span>
                </h4>

                <div class="order-info">
                    <ul class="list-group mb-3 px-2">
                        <li class="list-group-item d-flex justify-content-between lh-sm pt-3">
                            <span>Pool Supplies ($349.99)</span>
                            <span>x1</span>
                        </li>
                        <li class="list-group-item"></li>
                        <li class="list-group-item"></li>
                        <li class="list-group-item"></li>
                        <li class="list-group-item d-flex justify-content-between lh-sm">
                            <span>Subtotal:</span>
                            <span>$349.99</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between lh-sm">
                            <span>Shipping:</span>
                            <span>$4.55</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between lh-sm">
                            <span>Additional Tax:</span>
                            <span>$0.75</span>
                        </li>
                        <li class="list-group-item d-flex justify-content-between lh-sm pb-3">
                            <h3 style="font-weight: bold;">Total:</h3>
                            <h3 style="font-weight: bold;">$355.30</h3>
                        </li>
                    </ul>
                </div>
                
                <div class="form-check mb-4" style="display: flex; justify-content: center;">
                    <input class="form-check-input me-2" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">I understand and agree to the terms and conditions</label>
                </div>
        if (
          day === this.selected.date() &&
          this.selected.isSame(this.month, "month")
        ) {
          this.addIndicator();
          this.bodyDivs[index].classList.add("cal-day__day--selected");
          this.bodyDivs[index].classList.remove("cal-day__day--indicator");
          printSelectedApts(this.selected.toDate());
        }

                <input class="btn btn-lg col-8 offset-2 mb-4" type="submit" id="submitButton" value="PROCEED TO CHECKOUT">
            </div>
        </div>
    </div>
  </body>
</html>