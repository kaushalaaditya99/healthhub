// components/Calendar.js

"use client";  // This tells Next.js that this component should be rendered on the client

import { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';

const TaskCalendar = () => {
  const [date, setDate] = useState(new Date());

  const onDateChange = (newDate) => {
    setDate(newDate);
  };

  return (
    <div className="p-6 bg-white rounded-md shadow-md">
      <h2 className="text-2xl font-semibold text-center mb-4">Task Calendar</h2>
      <Calendar onChange={onDateChange} value={date} />
      <p className="text-center mt-4">Selected Date: {date.toDateString()}</p>
    </div>
  );
};

export default TaskCalendar;