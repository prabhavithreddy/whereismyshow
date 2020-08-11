import React, { useState, useEffect} from 'react';
import ItemsCarousel from 'react-items-carousel';
const fetch = require("node-fetch");

class ProviderCarousel extends React.Component{
    
    constructor(props) {
        super(props);
        this.state = {providers:[]};
        this.chevronWidth = 40;
        this.postData("http://127.0.0.1:5000/api/v1/getproviders");
    }
    postData(url){
        fetch(url)
        .then(resp=>resp.json())
        .then(result=>{
            this.setState({providers:result});
        });
    }
    componentDidMount(){
        
    }

    render(){
        return(
            <div style={{ padding: `0 ${this.chevronWidth}px` }}>
                <ItemsCarousel
                numberOfCards={2}
                gutter={20}
                leftChevron={<button>{'<'}</button>}
                rightChevron={<button>{'>'}</button>}
                outsideChevron
                chevronWidth={this.chevronWidth}
                >
                {
                    this.state.providers.map(provider=>
                        <div style={{ height: 200, background: '#EEE' }}>
                            <img key={provider.id} src={provider.logo} alt = {provider.name} width={"auto"} height = {200}/>
                        </div>
                    )
                }
                </ItemsCarousel>    
            </div>
        );        
    }
}
export default ProviderCarousel;