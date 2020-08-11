import React, { Component, useState } from 'react';

export default function Title(props){
    const profile = props.Profile;
    return (
        <div key = {profile.Id} className="Profile">
            <img src = {profile.ImageUrl} width ={300} height = {150} alt={profile.Title}/>
            <div className="ProfileContent">
                <h2>{profile.Title}</h2>
                <img src = {profile.Provider.Icon} alt = {profile.Provider.Name}/><br/>
                <a href = {profile.Provider.Url}>Watch Now</a>
            </div>
        </div>
    );
}