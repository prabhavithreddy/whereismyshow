import React, { useState, useEffect} from 'react';
//import ItemsCarousel from 'react-items-carousel';
import Carousel from 'react-multi-carousel';
import range from 'lodash/range';

const fetch = require("node-fetch");

class ProviderCarousel extends React.Component{
    
    constructor(props) {
        super(props);
        this.state = {providers:[]};
        this.responsive = {
            superLargeDesktop: {
              // the naming can be any, depends on you.
              breakpoint: { max: 4000, min: 3000 },
              items: 5
            },
            desktop: {
              breakpoint: { max: 3000, min: 1024 },
              items: 3
            },
            tablet: {
              breakpoint: { max: 1024, min: 464 },
              items: 2
            },
            mobile: {
              breakpoint: { max: 464, min: 0 },
              items: 1
            }
          };
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
    changeActiveItem(activeItemIndex){
        this.setState({ activeItemIndex });
    }
    render(){
        return(
          <div width="500px">
            <Carousel
                    style={{width:"500px"}}
                    swipeable={false}
                    draggable={false}
                    responsive={this.responsive}
                    ssr={true} // means to render carousel on server-side.
                    infinite={true}
                    autoPlay={false}
                    autoPlaySpeed={1000}
                    keyBoardControl={true}
                    customTransition="all .5"
                    transitionDuration={500}
                    containerClass="carousel-container"
                    removeArrowOnDeviceType={["tablet", "mobile"]}
                    deviceType={this.props.deviceType}
                    dotListClass="custom-dot-list-style"
                    itemClass="carousel-item-padding-20-px"
            >
                {
                    this.state.providers.map(provider=>
                            <img key={provider.id} src={provider.logo} alt = {provider.name} width={"auto"} height={150}/>
                    )
                }
            </Carousel>    
          </div>
        );        
    }
}
export default ProviderCarousel;