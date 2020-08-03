import React, { useState } from 'react';
import Title from './Title' 
const fetch = require("node-fetch");
export default function Titles(props) {
    //const titles = props.Items;
    const [titles, setState] = useState([])
    const postData = (url)=>{
        fetch(url)
        .then(resp=>resp.json())
        .then(result=>{
            setState(result);
        });
    };
    postData("http://127.0.0.1:9000/api/v1/getresultstest?title=test");
    return(
        <div>
            {
                titles.map(title => <Title Profile = {title}/>)
            }
        </div>
    );
}