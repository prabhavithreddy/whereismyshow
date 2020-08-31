import React, { useState } from 'react';
import Titles from './Titles';
import ProviderCarousel from './ProviderCarousel'
import Header from '../Header/Header';
import Footer from '../Footer/Footer';
import Container from 'react-bootstrap/Container';
export default function App() {
  const [items, setState] = useState([])
  const UpdateResults = (data)=>{
    setState(data);
  };
  return (
    <>
      <header>
        <Header />
      </header>
      <nav/>
      <section>        
        <Container>
          <ProviderCarousel />
          {/*<Titles Items = {items}/>  */}
          {/* <Titles/> */}
        </Container>
      </section>
      <aside/>
      <footer class="site-footer unique-color-dark"><Footer /></footer>
    </>
  );
}