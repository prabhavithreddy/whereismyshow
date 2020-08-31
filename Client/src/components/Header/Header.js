import React, { useState, useEffect} from 'react';
import { Container, Row, Col, Navbar, Nav, FormControl, Form } from 'react-bootstrap';
// import Form from '../Content/Form';
class Header extends React.Component{
    constructor(props) {
        super(props);
    }

    render(){
        return(
                <Navbar collapseOnSelect bg="dark" variant="dark" expand="lg">
                    <Container fluid="md">
                        <Row>
                            <Col>
                                <Navbar.Brand href="#home">Watch Now</Navbar.Brand>
                                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                            </Col>
                            <Col>
                                <FormControl type="text" placeholder="Search for Movie or a Show" style={{width:"48rem"}}/>
                            </Col>
                            <Col>
                                <Navbar.Collapse id="responsive-navbar-nav">                    
                                    <Nav>
                                        <Nav.Link href="#deets">About</Nav.Link>
                                        <Nav.Link eventKey={2} href="#memes">Contact</Nav.Link>
                                    </Nav>
                                </Navbar.Collapse>
                            </Col>
                        </Row>
                    </Container>
                </Navbar>
        );
    }
}

export default Header;