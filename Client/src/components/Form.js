import React, { useState } from 'react';
import Search from './Search'

const fetch = require("node-fetch");

export default function Form(props){
    const [title, setState] = useState('');
    const postData = (url)=>{
        fetch(url)
        .then(resp=>resp.json())
        .then(result=>{
            props.UpdateResults(result);
        });
    };
    const handleSubmit = (event)=>{
        event.preventDefault();
        postData("http://127.0.0.1:9000/api/v1/getresultstest?title=test");
        //props.UpdateResults(Feed());
    };
    return(
            <div>
                <form onSubmit = {handleSubmit}>
                    <Search/>
                </form>
            </div>
        )
}