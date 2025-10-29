import React, {useEffect, useState} from 'react'
import {fetchAvailability} from './api/calendly'

export default function App(){
  const [slots, setSlots] = useState([])
  useEffect(()=>{
    fetchAvailability('2025-10-30','consultation').then(r=>setSlots(r.available_slots||[]))
  },[])
  return (
    <div style={{padding:20}}>
      <h2>Available slots</h2>
      <ul>
        {slots.map(s=> (
          <li key={s.start_time}>{s.start_time} - {s.end_time} : {s.available? 'Free':'Booked'}</li>
        ))}
      </ul>
    </div>
  )
}
