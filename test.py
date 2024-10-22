<!DOCTYPE html>
<html lang="en">
<head>
    <title>Dream Air</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            max-width: 600px;
            margin: auto;
        }
        h1, h2 {
            text-align: center;
        }
        .tabs {
            display: flex;
            justify-content: space-around;
            cursor: pointer;
            margin-bottom: 20px;
        }
        .tab {
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            outline: none;
            transition: background-color 0.3s;
        }
        .tab:hover {
            background-color: #0056b3;
        }
        .tab-content {
            display: none;
        }
        .active {
            display: block;
        }
        .seat-map {
            display: grid;
            grid-template-columns: repeat(8, 8);
            gap: 10px;
            margin-top: 20px;
        }
        .seat {
            width: 40px;
            height: 40px;
            background-color: #d4edda;
            border: 1px solid #ccc;
            border-radius: 5px;
            text-align: center;
            line-height: 40px;
            cursor: pointer;
        }
        .seat.reserved {
            background-color: #f8d7da;
            cursor: not-allowed;
        }
        .seat.selected {
            background-color: #007BFF;
            color: white;
        }

        .flight-list, .service-list {
            margin-top: 20px;
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 5px;
        }
        .flight-item {
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        input[type="text"],
        input[type="email"],
        input[type="password"],
        select,
        input[type="date"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
            margin-top: 10px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .hidden {
            display: none;
        }
        .cancel-button {
            background-color: #dc3545;
            color: white;
            border: none;
            cursor: pointer;
            margin-left: 10px;
        }
        .cancel-button:hover {
            background-color: #c82333;
        }
    </style>
</head>
<body>

<h1>Dream Air</h1>

<div class="tabs">
    <button class="tab active" onclick="showTab('customerManagement')">Customer Management</button>
    <button class="tab" onclick="showTab('availableFlights')">Available Flights</button>
    <button class="tab" onclick="showTab('bookingSection')">Book Flight</button>
    <button class="tab" onclick="showTab('bookedFlightsSection')">Booked Flights</button>
</div>

<!-- Customer Management Section -->
<div id="customerManagement" class="tab-content active">
    <div>
        <h2>Login</h2>
        <input type="text" placeholder="Username" id="loginUsername" required>
        <input type="password" placeholder="Password" id="loginPassword" required>
        <button onclick="loginUser()">Login</button>

        <div id="loginMessage" class="hidden"></div>

        <p>Don't have an account? <button onclick="showSignUp()">Sign Up</button></p>
    </div>
</div>

<!-- Sign Up Section -->
<div id="signUpSection" class="hidden">
    <div>
        <h2>Register</h2>
        <input type="text" placeholder="Username" id="registerUsername" required>
        <input type="email" placeholder="Email" id="registerEmail" required>
        <input type="password" placeholder="Password" id="registerPassword" required>
        <button onclick="registerUser()">Register</button>

        <p>Already have an account? <button onclick="showLogin()">Login</button></p>

        <div id="registerMessage" class="hidden"></div>
    </div>
</div>


<div id="availableFlights" class="tab-content">
    <div class="flight-list">
        <h2>Available Flights</h2>
        <div class="flight-item" data-id="101" data-departure="New York" data-arrival="London" data-date="2024-12-01" data-price="500">
            <strong>Flight 101:</strong> New York to London on 2024-12-01<br>
            Price: $500<br>
        </div>
        <div class="flight-item" data-id="202" data-departure="Los Angeles" data-arrival="Tokyo" data-date="2024-12-15" data-price="700">
            <strong>Flight 202:</strong> Los Angeles to Tokyo on 2024-12-15<br>
            Price: $700<br>
        </div>
        <div class="flight-item" data-id="303" data-departure="Paris" data-arrival="Berlin" data-date="2024-12-20" data-price="300">
            <strong>Flight 303:</strong> Paris to Berlin on 2024-12-20<br>
            Price: $300<br>
        </div>
        <!-- Add more flights as needed -->
    </div>
</div>

<div id="bookingSection" class="tab-content">
    <div>
        <h2>Booking Form</h2>

        <b>Departure City</b>
        <input type="text" id="departureCity" required>

        <b>Arrival City</b>
        <input type="text" id="arrivalCity" required>
        
        <b>Departure Date</b>
        <input type="date" id="flightDate" required>
        
        <label>
            <input type="checkbox" id="roundTrip" onclick="toggleRoundTrip()"> Round Trip
        </label>
        
        <div id="returnFields" class="hidden">
            <input type="date" id="returnDate">
        </div>

        <button onclick="findFlight()">Find Flights</button>
        
        <div id="foundFlights" class="flight-list hidden">
            <h3>Available Flights</h3>
            <div id="availableFlightsList"></div>
        </div>
        
        <div id="bookingForm" class="hidden">
            <h2>Passenger Details</h2>
            <input type="text" placeholder="Name" id="passengerName" required>
            <input type="email" placeholder="Email" id="passengerEmail" required>
            <input type="text" placeholder="Phone" id="passengerPhone" required>
            <div class="service-list">
                <h3>Purchase Services</h3>
                <label>
                    <input type="checkbox" id="extraBaggage"> Extra Baggage ($50)
                </label><br>
                <label>
                    <input type="checkbox" id="mealPreference"> Meal Preference ($30)
                </label><br>
                <label>
                    <input type="checkbox" id="travelInsurance"> Travel Insurance ($20)
                </label><br>
            </div>
            <div id="seatMapSection" class="hidden">
                <h3>Select Your Seat</h3>
                <div id="seatMap" class="seat-map"></div>
            </div>
            <button id="confirmBookingButton">Confirm Booking</button>
        </div>
    </div>
</div>

<div id="bookedFlightsSection" class="tab-content">
    <h2>Booked Flights</h2>
    <div id="bookedFlightsList" class="flight-list"></div>
</div>

<div id="confirmationSection" class="tab-content">
    <h1>Booking Confirmation</h1>
    <div id="confirmationDetails"></div>
    <button onclick="showTab('bookingSection')">Back to Booking</button>
</div>

<script>
    let currentFlight;
    let currentUser = null;

    function showTab(tabName) {
        const tabs = document.querySelectorAll('.tab-content');
        tabs.forEach(tab => {
            tab.classList.remove('active');
        });
        document.getElementById(tabName).classList.add('active');

        const tabButtons = document.querySelectorAll('.tab');
        tabButtons.forEach(tabButton => {
            tabButton.classList.remove('active');
        });
        event.currentTarget.classList.add('active');

        if (tabName === 'bookedFlightsSection') {
            displayBookedFlights();
        }
    }

    function registerUser() {
        const username = document.getElementById('registerUsername').value;
        const email = document.getElementById('registerEmail').value;
        const password = document.getElementById('registerPassword').value;

        if (!username || !email || !password) {
            alert("Please fill in all fields.");
            return;
        }

        let users = JSON.parse(localStorage.getItem('users')) || [];
        const userExists = users.some(user => user.username === username);
        
        if (userExists) {
            alert("Username already exists. Please choose another one.");
            return;
        }

        const newUser = { username, email, password };
        users.push(newUser);
        localStorage.setItem('users', JSON.stringify(users));
        alert("Registration successful! You can now log in.");
    }

    function loginUser() {
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        let users = JSON.parse(localStorage.getItem('users')) || [];
        const user = users.find(user => user.username === username && user.password === password);

        if (user) {
            currentUser = user;
            document.getElementById('loginMessage').innerText = "Login successful! Welcome, " + user.username;
            document.getElementById('loginMessage').classList.remove('hidden');
            showTab('bookingSection');
        } else {
            document.getElementById('loginMessage').innerText = "Invalid username or password.";
            document.getElementById('loginMessage').classList.remove('hidden');
        }
    }
    function showSignUp() {
        document.getElementById('customerManagement').classList.add('hidden');
        document.getElementById('signUpSection').classList.remove('hidden');
    }

    function showLogin() {
        document.getElementById('signUpSection').classList.add('hidden');
        document.getElementById('customerManagement').classList.remove('hidden');
    }


    function toggleRoundTrip() {
        const returnFields = document.getElementById('returnFields');
        returnFields.classList.toggle('hidden');
    }

    function findFlight() {
        const departureCity = document.getElementById('departureCity').value;
        const arrivalCity = document.getElementById('arrivalCity').value;
        const flightDate = document.getElementById('flightDate').value;
        const isRoundTrip = document.getElementById('roundTrip').checked;
        const returnDate = document.getElementById('returnDate').value;

        const flights = document.querySelectorAll('.flight-item');
        let foundFlights = [];

        flights.forEach(flight => {
            const flightDeparture = flight.dataset.departure;
            const flightArrival = flight.dataset.arrival;
            const flightDateData = flight.dataset.date;

            if (flightDeparture.toLowerCase() === departureCity.toLowerCase() &&
                flightArrival.toLowerCase() === arrivalCity.toLowerCase() &&
                flightDateData === flightDate) {
                foundFlights.push({ flight, direction: 'outbound' });
            }

            
            if (isRoundTrip && returnDate) {
                const returnFlightDeparture = flight.dataset.arrival; 
                const returnFlightArrival = flight.dataset.departure; 
                const returnFlightDateData = flight.dataset.date;

                if (returnFlightDeparture.toLowerCase() === arrivalCity.toLowerCase() &&
                    returnFlightArrival.toLowerCase() ===
                    departureCity.toLowerCase() &&returnFlightDateData
                    === returnDate) {
                    foundFlights.push({ flight, direction: 'return' })
                ;
                }
            }
        });

        displayFoundFlights(foundFlights);
    }

    function displayFoundFlights(flights) {
        const availableFlightsList = document.getElementById('availableFlightsList');
        availableFlightsList.innerHTML = ''; // Clear previous results

        if (flights.length === 0) {
            availableFlightsList.innerHTML = '<p>No flights found.</p>';
            document.getElementById('foundFlights').classList.remove('hidden');
            return;
        }

        flights.forEach(({ flight, direction }) => {
            const flightId = flight.dataset.id;
            const flightDeparture = flight.dataset.departure;
            const flightArrival = flight.dataset.arrival;
            const flightDate = flight.dataset.date;
            const flightPrice = flight.dataset.price;

            const flightDiv = document.createElement('div');
            flightDiv.innerHTML = `<strong>${direction === 'outbound' ? 'Outbound' : 'Return'} Flight ${flightId}:</strong> ${flightDeparture} to ${flightArrival} on ${flightDate}<br>Price: $${flightPrice}<br>`;
            const bookButton = document.createElement('button');
            bookButton.innerText = 'Book Flight';
            bookButton.onclick = () => prepareBooking(flightId, flightDeparture, flightArrival, flightDate, flightPrice, direction);
            flightDiv.appendChild(bookButton);
            availableFlightsList.appendChild(flightDiv);
        });

        document.getElementById('foundFlights').classList.remove('hidden');
    }

    function prepareBooking(flightId, departure, arrival, date, price, direction) {
        if (direction === 'outbound') {
            currentFlight = { flightId, departure, arrival, date, price, direction };

            const returnDate = document.getElementById('returnDate').value;
            if (document.getElementById('roundTrip').checked && returnDate) {
                    
                const returnFlight = { 
                    flightId: flightId, 
                    departure: arrival, 
                    arrival: departure, 
                    date: returnDate,
                    price: price 
                };
                currentFlight.returnFlight = returnFlight; 
            }
        }
        
        document.getElementById('bookingForm').classList.remove(
            'hidden');
        showSeatMap();
        document.getElementById('seatMapSection').classList.remove('hidden');
        document.getElementById('confirmBookingButton').onclick = () => confirmBooking();
    }

    let reservedSeats = JSON.parse(localStorage.getItem('reservedSeats')) || {};

    function showSeatMapForBooking(flight) {
        const seatMap = document.getElementById('seatMap');
        seatMap.innerHTML = ''; 

        const rows = 8; 
        const seatsPerRow = 8; 

        const reservedSeats = flight.selectedSeats.reduce((acc, seat) => {
            acc[seat] = true;
            return acc;
        }, {});

        for (let i = 0; i < rows; i++) {
            const rowDiv = document.createElement('div');
            rowDiv.style.display = 'flex'; 

            const rowLabel = String.fromCharCode(65 + i); 

            for (let j = 1; j <= seatsPerRow; j++) {
                const seatDiv = document.createElement('div');
                seatDiv.classList.add('seat');
                seatDiv.innerText = `${rowLabel}${j}`; 

                const seatKey = `${flight.flightId}-${rowLabel}${j}`;
                if (reservedSeats[seatKey]) {
                    seatDiv.classList.add('reserved');
                } else {
                    seatDiv.onclick = () => selectSeat(seatKey, seatDiv);
                }

                rowDiv.appendChild(seatDiv);
            }

            seatMap.appendChild(rowDiv);
        }
    }



    function selectSeat(seatKey, seatDiv) {
        if (seatDiv.classList.contains('selected')) {
            seatDiv.classList.remove('selected');
            delete reservedSeats[seatKey];
        } else {
            if (!seatDiv.classList.contains('reserved')) {
                seatDiv.classList.add('selected');
                reservedSeats[seatKey] = true;
            }
        }
    }

    function confirmBooking() {
        const passengerName = document.getElementById('passengerName').value;
        const passengerEmail = document.getElementById('passengerEmail').value;
        const passengerPhone = document.getElementById('passengerPhone').value;
        
        const extraBaggage = document.getElementById('extraBaggage').checked ? 50 : 0;
        const mealPreference = document.getElementById('mealPreference').checked ? 30 : 0;
        const travelInsurance = document.getElementById('travelInsurance').checked ? 20 : 0;

        let totalPrice = parseFloat(currentFlight.price) + extraBaggage + mealPreference + travelInsurance;

        if (currentFlight.returnFlight) {
            totalPrice += parseFloat(currentFlight.returnFlight.price);  // Ensure return flight price is added
        }

        const selectedSeats = Object.keys(reservedSeats).filter(seatKey => reservedSeats[seatKey]);

        let bookedFlights = JSON.parse(localStorage.getItem('bookedFlights')) || [];
        bookedFlights.push({ 
            ...currentFlight, 
            passengerName, 
            passengerEmail, 
            passengerPhone, 
            totalPrice, 
            username: currentUser.username, 
            selectedSeats: selectedSeats 
        });

        if (currentFlight.returnFlight) {
            bookedFlights[bookedFlights.length - 1].returnFlight = currentFlight.returnFlight;
        }

        localStorage.setItem('bookedFlights', JSON.stringify(bookedFlights));
        alert(`Booking confirmed for ${passengerName}. Total Price: $${totalPrice}`);
        
        // Confirmation details...
        showTab('confirmationSection');
    }


    function displayBookedFlights() {
        const bookedFlightsList = document.getElementById('bookedFlightsList');
        bookedFlightsList.innerHTML = ''; // Clear previous results

        let bookedFlights = JSON.parse(localStorage.getItem('bookedFlights')) || [];
        bookedFlights = bookedFlights.filter(flight => flight.username === currentUser.username);
        bookedFlights.forEach((flight, index) => {
            const flightDiv = document.createElement('div');
            flightDiv.innerHTML = `<strong>Booking ${index + 1}:</strong> Flight ${flight.flightId}, ${flight.passengerName}, Total Price: $${flight.totalPrice}, Seat Selected: ${flight.selectedSeats.join(', ')}<br>`;
            
            if (flight.returnFlight) {
                flightDiv.innerHTML += `
                    <strong>Return Flight ID: ${flight.returnFlight.flightId}</strong>,
                    Departure: ${flight.returnFlight.departure},
                    Arrival: ${flight.returnFlight.arrival},
                    Date: ${flight.returnFlight.date}<br>
                `;
            }

            const cancelButton = document.createElement('button');
            cancelButton.innerText = 'Cancel Booking';
            cancelButton.onclick = () => cancelBooking(flight.flightId); 
            cancelButton.classList.add('cancel-button');
                    
            flightDiv.appendChild(cancelButton);
            bookedFlightsList.appendChild(flightDiv);
        });

        if (bookedFlights.length === 0) {
            bookedFlightsList.innerHTML = '<p>No booked flights.</p>';
        }
    }

    function cancelBooking(flightId) {
        let bookedFlights = JSON.parse(localStorage.getItem('bookedFlights')) || [];
             
        bookedFlights = bookedFlights.filter(flight => flight.flightId !== flightId);
      
        localStorage.setItem('bookedFlights', JSON.stringify(bookedFlights));

        displayBookedFlights();
        alert(`Booking for Flight ${flightId} has been canceled.`);
    }

</script>
</body>
</html>
