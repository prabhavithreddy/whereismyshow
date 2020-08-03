import React, { useState } from 'react';
import Form from './Form';
import Titles from './Titles';

export default function App() {
  const [items, setState] = useState([])
  const UpdateResults = (data)=>{
    setState(data);
  };
  return (
    <div>
        <Form UpdateResults = {UpdateResults}/>
        <Titles Items = {items}/>
    </div>
  );
}