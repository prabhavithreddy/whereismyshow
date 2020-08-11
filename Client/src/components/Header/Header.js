import React, { useState, useEffect} from 'react';

class Header extends React.Component{
    constructor(props) {
        super(props);
    }

    render(){
        return(
            <h2 className="title">
                Search My Show
            </h2>
        );
    }
}

export default Header;