document.addEventListener('DOMContentLoaded',init)

function init(){
    const map = L.map('map').setView([29.10, -110.97], 4)
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map)

    const fetchGetRequest = async(url,func)=>{
      try {
        const response = await fetch(url)
        const json = await response.json()
        return func(json)
        
      } catch (error) {
        console.log(error)
        
      }
    }
    const addAllPlacesToMap=(json)=>{
      console.log(json)
    }
    fetchGetRequest('/api/v1/places',addAllPlacesToMap)
  
}
//29.1026, -110.97732.