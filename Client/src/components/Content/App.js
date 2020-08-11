import React, { useState } from 'react';
import Form from './Form';
import Titles from './Titles';
import ProviderCarousel from './ProviderCarousel'
export default function App() {
  const [items, setState] = useState([])
  const UpdateResults = (data)=>{
    setState(data);
  };
  return (
    <div>
      <Form UpdateResults = {UpdateResults} width={600}/>
      <ProviderCarousel />
      <Titles Items = {items}/> 
    </div>
  );
}