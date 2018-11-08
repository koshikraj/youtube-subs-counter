import React, { Component } from 'react';
import logo from './logo.svg';
import GOLD from './gold.png';
import SILVER from './silver.png';
import './App.css';

import CountUp from 'react-countup';

const API = "http://www.topsubs.xyz:8888/";

const GREEN = '#a5c955';

const RED = '#e1c85e';


class App extends Component {

    constructor(props) {
        super(props);
        this.state = {pewdiepieCount: 69005000,
            tseriesCount: 68050000,
            lastpewdiepieCount: 0,
            lasttseriesCount: 0,
            pewdiepieUrl: "",
            tseriesUrl: "",
            loaded: false,
            winner: "pewdiepie"};


    }



    componentWillMount() {


        fetch(API + 'channel?username=tseries')
            .then(response => response.json())
            .then(response => {
                console.log(response);
                this.setState({ tseriesCount: response.data.subscribers, loaded: true, tseriesUrl: response.data.url});
            });

        fetch(API + 'channel?username=pewdiepie')
            .then(response => response.json())
            .then(response => {
                console.log(response);
                this.setState({pewdiepieCount: response.data.subscribers,loaded: true, pewdiepieUrl: response.data.url});
            });

        setInterval(() => { fetch(API + 'subscompare')
            .then(response => response.json())
            .then(response => {
                console.log(response);

                this.setState({lastpewdiepieCount: this.state.pewdiepieCount, lasttseriesCount: this.state.tseriesCount});
                this.setState({pewdiepieCount: response.data.pewdiepie, tseriesCount: response.data.tseries, loaded: true});
            }); }, 10000);

    }

    componentDidMount(){

    }



  render() {
    return (
        <div style={{"display": "flex", "flex-direction": "column"}}  >

            <div style={{"text-align": "center", "margin": 50}}> <span style={{"font-family": "sans-serif", "font-size": 25}}>Follow the <a href="https://twitter.com/rajkoshik" target="_blank">twitter bot</a> to get notified when T series overtakes PewDiePie </span>

             <a href="https://github.com/koshikraj/youtube-subs-counter" target="_blank">
                <img style={{"position": "absolute", "top": 0, "right": 0, "border": 0}} src="https://camo.githubusercontent.com/38ef81f8aca64bb9a64448d0d70f1308ef5341ab/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f6461726b626c75655f3132313632312e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png"/>
             </a>
            </div>


            <div style={{ "display": "flex", "flex-wrap":"wrap"}}>





                <div style={{"display": "flex", "align-items": "center", "flex-direction": "column"}}>

                    <img height="100" width="100" src={this.state.tseriesCount>this.state.pewdiepieCount ? GOLD : SILVER}/>

                <div style={{"display": "flex", "flex-direction":"column"
                , "margin": "100px", "background-color": this.state.tseriesCount>this.state.pewdiepieCount ? GREEN : RED, "padding": 30}}>


                <div style={{"display": "flex", "flex-direction":"row", "align-items": "center"}}>
                <img height="100" width="100" src={this.state.tseriesUrl}/>
                <span>
                    T-series
                </span>
                </div>

            <div className="subs-counter-border">
                    {this.state.loaded ?
                   <CountUp start={this.state.lasttseriesCount} end={this.state.tseriesCount} duration={1}
                                                 className="subs-counter"/>:<div className="subs-counter"> loading... </div>
                }
              </div>
                </div>
            </div>

                <div style={{"display": "flex", "align-items": "center", "flex-direction": "column"}}>


                <img height="100" width="100" src={this.state.pewdiepieCount > this.state.tseriesCount ? GOLD : SILVER}/>

                    <div style={{"display": "flex", "flex-direction":"column",
                "margin": "100px", "background-color": this.state.pewdiepieCount > this.state.tseriesCount ? GREEN : RED, "padding": 30}}>
                <div style={{"display": "flex", "flex-direction":"row", "align-items": "center"}}>
                <img height="100" width="100" src={this.state.pewdiepieUrl}/>
                <span>
                    PewDewPie
                </span>
                </div>
                <div className="subs-counter-border">
                  {this.state.loaded ?
                      <CountUp start={this.state.lastpewdiepieCount} end={this.state.pewdiepieCount} duration={1}
                               className="subs-counter"/>:<div className="subs-counter"> loading... </div>
                  }

              </div>
                    </div>
          </div>
        </div>

      </div>
  );
  }
}

export default App;
