import React, {Component} from "react"

class Body extends Component{
    constructor(props){
        super(props);
        this.state={
            prev_component_state:'Some previous component state',
        };
    }
    // changing state.
    newStateSet=()=>{
        this.setState(
            // property that need to be updated
            {prev_component_state:"State Changed"}
        )
        console.log('State changed')
    }
    render(){
        let data = this.props.body_property; // when some_var is in app.js which is a property for Body
        return(
            <div>
                <h2>{data}</h2>
                {/* Channging states on button click*/}
                <button onClick={()=>alert("You have clicked the button.")}
                onClick={this.newStateSet}>{this.state.prev_component_state}</button>

            </div>
        )
    }
}

export default Body