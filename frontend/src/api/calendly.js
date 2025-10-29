export async function fetchAvailability(date, apptType){
  const res = await fetch(`/api/calendly/availability?date=${date}&appointment_type=${apptType}`)
  return res.json()
}

export async function bookSlot(payload){
  const res = await fetch('/api/calendly/book', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(payload)})
  return res.json()
}
