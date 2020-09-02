// 'React' must be in scope when using JSX thats why we imported react
import React,{ Component } from 'react';
import { Navbar } from 'reactstrap';
import Body from './Component/BodyComponent';
import {a} from './shared/shared';

// Parent Component
// State lifted up
class  App extends Component{
  constructor(props){
    super(props);
    this.parent_state = a;
  }
  render() {
    // we have to return jsx
    return (
      <div>
      <Navbar color='primary'>Using reactstrap</Navbar> {/*first component*/}
      <Body body_property={this.parent_state}/> {/* Second component */}
      </div>
    )
  }
}

export default App;