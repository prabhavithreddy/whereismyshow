import React, { Component, useState } from 'react';
import TextBox from './TextBox'
import Button from './Button'

export default function Search(){
    return(
        <div>
            <TextBox width={100}/>
            <Button name={"Search"} />
        </div>
    );
}