import React, { Component, useState } from 'react';
import Card from 'react-bootstrap/Card'
import Button from 'react-bootstrap/Button'
export default function Title(props){
    const profile = props.Profile;
    return (
        <Card style={{ width: '30rem', flexDirection: 'row' }}
        bg="dark"
        text="white"
        className="mb-2"
        >
            <Card.Img variant="left" src={profile.ImageUrl} width ={"300em"} height = {"180em"}/>
            <Card.Body>
                <Card.Title>{profile.Title}</Card.Title>
                <img src = {profile.Provider.Icon} alt = {profile.Provider.Name}/><br/>
                <Button variant="danger" href = {profile.Provider.Url} target="_blank">Watch Now</Button>
            </Card.Body>
        </Card>
    );
}