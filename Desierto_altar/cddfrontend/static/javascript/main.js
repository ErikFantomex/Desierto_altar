document.addEventListener('DOMContentLoaded',init)

function init(){
    const map = L.map('map').setView([29.10, -110.97], 4)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map)
  
}
//29.1026, -110.97732.