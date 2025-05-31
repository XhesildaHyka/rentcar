// 1. Funksione për menaxhimin e makinave në Local Storage
function loadCars() {
    const savedCars = localStorage.getItem('hykaRentalCars');
    return savedCars ? JSON.parse(savedCars) : [
        // Makinat default
        {
            id: 1,
            name: "VW Golf 7",
            image: "assets/images/golf7.jpg",
            description: "Makina ideale për qytet dhe udhëtime të shkurtra.",
            price: "35€/ditë",
            available: true
        },
        {
            id: 2,
            name: "Mercedes C220",
            image: "assets/images/mercedes.jpg",
            description: "Luks dhe performancë. Përsosur për udhëtime të gjata.",
            price: "70€/ditë",
            available: true
        }
    ];
}

function saveCars(carsArray) {
    localStorage.setItem('hykaRentalCars', JSON.stringify(carsArray));
}

// 2. Variabla globale
let cars = loadCars();

// 3. Funksioni për të shfaqur makinat në faqen e rezervimit
function displayCars() {
    const carsGrid = document.getElementById('cars-grid');
    if (!carsGrid) return;
    
    carsGrid.innerHTML = '';
    
    cars.forEach(car => {
        const carCard = document.createElement('div');
        carCard.className = 'car-card';
        carCard.innerHTML = `
            <img src="${car.image}" alt="${car.name}" onerror="this.src='assets/images/default-car.jpg'">
            <div class="car-info">
                <h3>${car.name}</h3>
                <p>${car.description}</p>
                <p class="price">${car.price}</p>
                <button class="btn ${car.available ? '' : 'disabled'}" 
                        onclick="selectCar(${car.id})" 
                        ${car.available ? '' : 'disabled'}>
                    ${car.available ? 'Rezervo Tani' : 'Jo në dispozicion'}
                </button>
            </div>
        `;
        carsGrid.appendChild(carCard);
    });
}

// Funksioni për zgjedhjen e makinës
function selectCar(carId) {
    const car = cars.find(c => c.id === carId);
    if (car) {
        document.getElementById('selectedCar').value = car.name;
        document.getElementById('cars-grid').style.display = 'none';
        document.getElementById('reservation-form').style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
}

// 4. Funksione për panelin e adminit
function displayCarsForEdit() {
    const editCarsList = document.getElementById('editCarsList');
    if (!editCarsList) return;
    
    editCarsList.innerHTML = '';
    
    cars.forEach(car => {
        const carItem = document.createElement('div');
        carItem.className = 'edit-car-item';
        carItem.innerHTML = `
            <div>
                <h4>${car.name}</h4>
                <p>${car.description}</p>
                <p>${car.price}</p>
            </div>
            <div class="edit-car-actions">
                <button class="btn toggle-btn" onclick="toggleCarAvailability(${car.id})">
                    ${car.available ? 'Bëj të padisponueshme' : 'Bëj të disponueshme'}
                </button>
                <button class="btn delete-btn" onclick="deleteCar(${car.id})">Fshi</button>
            </div>
        `;
        editCarsList.appendChild(carItem);
    });
}

function toggleCarAvailability(carId) {
    const car = cars.find(c => c.id === carId);
    if (car) {
        car.available = !car.available;
        saveCars(cars);
        displayCarsForEdit();
        displayCars(); // Përditëson edhe faqen e rezervimit
    }
}

function deleteCar(carId) {
    cars = cars.filter(c => c.id !== carId);
    saveCars(cars);
    displayCarsForEdit();
    displayCars();
}

// 5. Funksioni për shtimin e makinave të reja
function addNewCar(carData) {
    const newId = cars.length > 0 ? Math.max(...cars.map(c => c.id)) + 1 : 1;
    const newCar = {
        id: newId,
        ...carData,
        available: true
    };
    cars.push(newCar);
    saveCars(cars);
    return newCar;
}

// 6. Funksioni për login
function login() {
    const email = document.getElementById('adminEmail').value;
    const password = document.getElementById('adminPassword').value;

    if (email === 'autohyka@gmail.com' && password === 'HykaAdmin1981//') {
        document.getElementById('loginSection').style.display = 'none';
        document.getElementById('adminSection').style.display = 'block';
        displayCarsForEdit();
    } else {
        alert('Email ose fjalëkalim i pasaktë!');
    }
}

// 7. Funksione për upload të fotove
let uploadedImageData = '';

function handleImage(file) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = function (e) {
        uploadedImageData = e.target.result;
        document.getElementById('dropZone').textContent = "Foto e ngarkuar!";
    };
    reader.readAsDataURL(file);
}

// 8. Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    displayCars();
    
    // Admin page specific
    if (document.getElementById('addCarForm')) {
        const dropZone = document.getElementById('dropZone');
        const fileInput = document.getElementById('newCarImageFile');

        dropZone.addEventListener('click', () => fileInput.click());
        dropZone.addEventListener('dragover', e => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });
        dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
        dropZone.addEventListener('drop', e => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
            const file = e.dataTransfer.files[0];
            handleImage(file);
        });
        fileInput.addEventListener('change', e => {
            const file = e.target.files[0];
            handleImage(file);
        });

        document.getElementById('addCarForm').addEventListener('submit', function(e) {
            e.preventDefault();

            if (!uploadedImageData) {
                alert("Ju lutem ngarkoni një foto!");
                return;
            }

            const newCar = {
                name: document.getElementById('newCarName').value,
                image: uploadedImageData,
                description: document.getElementById('newCarDesc').value,
                price: document.getElementById('newCarPrice').value
            };

            addNewCar(newCar);
            displayCarsForEdit();
            this.reset();
            document.getElementById('dropZone').textContent = "Hidh këtu foton ose kliko për ta zgjedhur";
            uploadedImageData = '';
            alert('Makina u shtua me sukses!');
        });
    }

    // Reservation form handling
    const reservationForm = document.getElementById('reservationForm');
    if (reservationForm) {
        reservationForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const carModel = document.getElementById('selectedCar').value;
            const fullName = document.getElementById('fullName').value;
            const phone = document.getElementById('phone').value;
            const email = document.getElementById('email').value;
            const pickupLocation = document.getElementById('pickupLocation').value;
            const pickupDate = document.getElementById('pickupDate').value;
            const returnDate = document.getElementById('returnDate').value;
            
            const days = Math.ceil((new Date(returnDate) - new Date(pickupDate)) / (1000 * 60 * 60 * 24));
            
            if (days < 3) {
                alert('Rezervimi minimal është 3 ditë!');
                return;
            }
            
            emailjs.send('service_r955159', 'template_0k885ma', {
                car_model: carModel,
                full_name: fullName,
                phone: phone,
                email: email,
                pickup_location: pickupLocation,
                pickup_date: pickupDate,
                return_date: returnDate,
                days: days
            })
            .then(function() {
                alert('Rezervimi u dërgua me sukses! Do t\'ju kontaktojmë së shpejti.');
                reservationForm.reset();
                document.getElementById('cars-grid').style.display = 'grid';
                document.getElementById('reservation-form').style.display = 'none';
            }, function(error) {
                alert('Gabim gjatë dërgimit. Ju lutem provoni përsëri ose na kontaktoni direkt.');
                console.error('EmailJS error:', error);
            });
        });
    }
    
    // Date picker restrictions
    const today = new Date().toISOString().split('T')[0];
    const pickupDateInput = document.getElementById('pickupDate');
    if (pickupDateInput) {
        pickupDateInput.min = today;
        
        pickupDateInput.addEventListener('change', function() {
            const returnDateInput = document.getElementById('returnDate');
            returnDateInput.min = this.value;
            returnDateInput.value = '';
        });
    }
});