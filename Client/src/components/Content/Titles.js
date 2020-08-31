import React, { useState } from 'react';
import Title from './Title' 
import PaginationList from '../Utils/Pagination'
import { Container } from 'react-bootstrap';
const fetch = require("node-fetch");


class Titles extends React.Component {
    constructor(){
        super();
        this.state = {titles:[
            {
              "ExternalLinks": [
                {
                  "Id": "tt11323316", 
                  "Name": "IMDB", 
                  "Url": "https://www.imdb.com/title/tt11323316"
                }, 
                {
                  "Id": "713496", 
                  "Name": "TMDB", 
                  "Url": "https://www.themoviedb.org/movie/713496"
                }
              ], 
              "Id": "5f0c5c4fcaefbd4898c34c96", 
              "ImageUrl": "images/image-not-available.jpg", 
              "Provider": {
                "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=8bc263d1-dd7b-40c0-98cd-f677eb14d81e_e12122020-07-28", 
                "Id": "5d84d6ddd95dc7385f6a43e9", 
                "Name": "Amazon Prime Video", 
                "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.84b94236-4857-bb3b-eebe-742a184abc70?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
              }, 
              "Title": "Penguin"
            }, 
            {
              "ExternalLinks": [
                {
                  "Id": "tt4052886", 
                  "Name": "IMDB", 
                  "Url": "https://www.imdb.com/title/tt4052886"
                }, 
                {
                  "Id": "63174", 
                  "Name": "TMDB", 
                  "Url": "https://www.themoviedb.org/tv/63174"
                }, 
                {
                  "Id": "Q19520525", 
                  "Name": "WIKI", 
                  "Url": "https://www.wikidata.org/wiki/Q19520525"
                }
              ], 
              "Id": "5d91416b302b840050ad2718", 
              "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/8698c96ae0e0038b81b661c8b2068ca1/Redirect", 
              "Provider": {
                "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                "Id": "5d84d6e1d95dc7385f6a4420", 
                "Name": "Netflix", 
                "Url": "https://www.netflix.com/title/80138262"
              }, 
              "Title": "Lucifer"
            }, 
            {
              "ExternalLinks": [
                {
                  "Id": "tt6067752", 
                  "Name": "IMDB", 
                  "Url": "https://www.imdb.com/title/tt6067752"
                }, 
                {
                  "Id": "564701", 
                  "Name": "TMDB", 
                  "Url": "https://www.themoviedb.org/movie/564701"
                }, 
                {
                  "Id": "Q55621418", 
                  "Name": "WIKI", 
                  "Url": "https://www.wikidata.org/wiki/Q55621418"
                }
              ], 
              "Id": "5e2ce0fb90c0e033a4883073", 
              "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/52a813360c68af256f523bf16052197e/Redirect", 
              "Provider": {
                "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                "Id": "5d84d6ddd95dc7385f6a43e9", 
                "Name": "Amazon Prime Video", 
                "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.90b54da0-3767-8327-44bb-156727659135?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
              }, 
              "Title": "Lucifer"
            },
            {
                "ExternalLinks": [
                  {
                    "Id": "tt11323316", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt11323316"
                  }, 
                  {
                    "Id": "713496", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/movie/713496"
                  }
                ], 
                "Id": "5f0c5c4fcaefbd4898c34c96", 
                "ImageUrl": "images/image-not-available.jpg", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=8bc263d1-dd7b-40c0-98cd-f677eb14d81e_e12122020-07-28", 
                  "Id": "5d84d6ddd95dc7385f6a43e9", 
                  "Name": "Amazon Prime Video", 
                  "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.84b94236-4857-bb3b-eebe-742a184abc70?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                }, 
                "Title": "Penguin"
              }, 
              {
                "ExternalLinks": [
                  {
                    "Id": "tt4052886", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt4052886"
                  }, 
                  {
                    "Id": "63174", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/tv/63174"
                  }, 
                  {
                    "Id": "Q19520525", 
                    "Name": "WIKI", 
                    "Url": "https://www.wikidata.org/wiki/Q19520525"
                  }
                ], 
                "Id": "5d91416b302b840050ad2718", 
                "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/8698c96ae0e0038b81b661c8b2068ca1/Redirect", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                  "Id": "5d84d6e1d95dc7385f6a4420", 
                  "Name": "Netflix", 
                  "Url": "https://www.netflix.com/title/80138262"
                }, 
                "Title": "Lucifer"
              }, 
              {
                "ExternalLinks": [
                  {
                    "Id": "tt6067752", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt6067752"
                  }, 
                  {
                    "Id": "564701", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/movie/564701"
                  }, 
                  {
                    "Id": "Q55621418", 
                    "Name": "WIKI", 
                    "Url": "https://www.wikidata.org/wiki/Q55621418"
                  }
                ], 
                "Id": "5e2ce0fb90c0e033a4883073", 
                "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/52a813360c68af256f523bf16052197e/Redirect", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                  "Id": "5d84d6ddd95dc7385f6a43e9", 
                  "Name": "Amazon Prime Video", 
                  "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.90b54da0-3767-8327-44bb-156727659135?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                }, 
                "Title": "Lucifer"
              },
              {
                "ExternalLinks": [
                  {
                    "Id": "tt11323316", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt11323316"
                  }, 
                  {
                    "Id": "713496", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/movie/713496"
                  }
                ], 
                "Id": "5f0c5c4fcaefbd4898c34c96", 
                "ImageUrl": "images/image-not-available.jpg", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=8bc263d1-dd7b-40c0-98cd-f677eb14d81e_e12122020-07-28", 
                  "Id": "5d84d6ddd95dc7385f6a43e9", 
                  "Name": "Amazon Prime Video", 
                  "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.84b94236-4857-bb3b-eebe-742a184abc70?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                }, 
                "Title": "Penguin"
              }, 
              {
                "ExternalLinks": [
                  {
                    "Id": "tt4052886", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt4052886"
                  }, 
                  {
                    "Id": "63174", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/tv/63174"
                  }, 
                  {
                    "Id": "Q19520525", 
                    "Name": "WIKI", 
                    "Url": "https://www.wikidata.org/wiki/Q19520525"
                  }
                ], 
                "Id": "5d91416b302b840050ad2718", 
                "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/8698c96ae0e0038b81b661c8b2068ca1/Redirect", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                  "Id": "5d84d6e1d95dc7385f6a4420", 
                  "Name": "Netflix", 
                  "Url": "https://www.netflix.com/title/80138262"
                }, 
                "Title": "Lucifer"
              }, 
              {
                "ExternalLinks": [
                  {
                    "Id": "tt6067752", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt6067752"
                  }, 
                  {
                    "Id": "564701", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/movie/564701"
                  }, 
                  {
                    "Id": "Q55621418", 
                    "Name": "WIKI", 
                    "Url": "https://www.wikidata.org/wiki/Q55621418"
                  }
                ], 
                "Id": "5e2ce0fb90c0e033a4883073", 
                "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/52a813360c68af256f523bf16052197e/Redirect", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                  "Id": "5d84d6ddd95dc7385f6a43e9", 
                  "Name": "Amazon Prime Video", 
                  "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.90b54da0-3767-8327-44bb-156727659135?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                }, 
                "Title": "Lucifer"
              },
              {
                "ExternalLinks": [
                  {
                    "Id": "tt11323316", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt11323316"
                  }, 
                  {
                    "Id": "713496", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/movie/713496"
                  }
                ], 
                "Id": "5f0c5c4fcaefbd4898c34c96", 
                "ImageUrl": "images/image-not-available.jpg", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=8bc263d1-dd7b-40c0-98cd-f677eb14d81e_e12122020-07-28", 
                  "Id": "5d84d6ddd95dc7385f6a43e9", 
                  "Name": "Amazon Prime Video", 
                  "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.84b94236-4857-bb3b-eebe-742a184abc70?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                }, 
                "Title": "Penguin"
              }, 
              {
                "ExternalLinks": [
                  {
                    "Id": "tt4052886", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt4052886"
                  }, 
                  {
                    "Id": "63174", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/tv/63174"
                  }, 
                  {
                    "Id": "Q19520525", 
                    "Name": "WIKI", 
                    "Url": "https://www.wikidata.org/wiki/Q19520525"
                  }
                ], 
                "Id": "5d91416b302b840050ad2718", 
                "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/8698c96ae0e0038b81b661c8b2068ca1/Redirect", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/NetflixIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                  "Id": "5d84d6e1d95dc7385f6a4420", 
                  "Name": "Netflix", 
                  "Url": "https://www.netflix.com/title/80138262"
                }, 
                "Title": "Lucifer"
              }, 
              {
                "ExternalLinks": [
                  {
                    "Id": "tt6067752", 
                    "Name": "IMDB", 
                    "Url": "https://www.imdb.com/title/tt6067752"
                  }, 
                  {
                    "Id": "564701", 
                    "Name": "TMDB", 
                    "Url": "https://www.themoviedb.org/movie/564701"
                  }, 
                  {
                    "Id": "Q55621418", 
                    "Name": "WIKI", 
                    "Url": "https://www.wikidata.org/wiki/Q55621418"
                  }
                ], 
                "Id": "5e2ce0fb90c0e033a4883073", 
                "ImageUrl": "https://utellyassets9-1.imgix.net/api/Images/52a813360c68af256f523bf16052197e/Redirect", 
                "Provider": {
                  "Icon": "https://utellyassets7.imgix.net/locations_icons/utelly/black_new/AmazonPrimeVideoIVAIN.png?w=92&auto=compress&app_version=5cb1e6a4-e86c-45a8-bd57-1fe10ea6e2ca_eww2020-07-18", 
                  "Id": "5d84d6ddd95dc7385f6a43e9", 
                  "Name": "Amazon Prime Video", 
                  "Url": "https://www.primevideo.com/detail/amzn1.dv.gti.90b54da0-3767-8327-44bb-156727659135?ie=UTF8&linkCode=xm2&tag=utellycom00-21"
                }, 
                "Title": "Lucifer"
              }
          ],
          pageOfItems: []
        };
        this.onChangePage = this.onChangePage.bind(this);
    }
    //const titles = props.Items;
    onChangePage(pageOfItems) {
        // update state with new page of items
        this.setState({ pageOfItems: pageOfItems });
    }
    postData(url){
        fetch(url)
        .then(resp=>resp.json())
        .then(result=>{
            setState(result);
        });
    }
    //postData("http://127.0.0.1:9000/api/v1/getresultstest?title=test");
    render(){
        return(
            <>
                <div className="titlesContainer">
                    {
                        this.state.pageOfItems.map(item => <Title Profile = {item} key={item.Id}/>)                        
                    }
                </div>
                <PaginationList items={this.state.titles} onChangePage={this.onChangePage} />
            </>
        );
    }
}
export default Titles;