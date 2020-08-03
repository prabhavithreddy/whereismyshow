import React, { useState } from 'react';

export default function TextBox(props){
    return(
        <input type="text" width={props.width}></input>
    );
}