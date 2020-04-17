import React, { Component } from 'react'
import Table from './Table'
import Form from './Form';
import axios from 'axios';


class App extends Component {
  state = {
    characters: [],
  }
removeCharacter = (index,id) => {
	const {characters } = this.state
	axios.delete('http://localhost:5000/users/'+id+'/')

	this.setState({
		characters: characters.filter((character, i) => {
		return i !== index;})
	})
		console.log(characters)
	}

handleSubmit = character => {
   this.makePostCall(character).then( callResult => {
      console.log(callResult)

         this.setState({ characters: [...this.state.characters, callResult] });
   });
 }
	render(){
		const {characters } = this.state;
		
		return(
		<div className = "container">
		<Table characterData = {characters} removeCharacter = {this.removeCharacter} />
		<Form handleSubmit = {this.handleSubmit}/>
		</div>
		)
	}
componentDidMount() {
   axios.get('http://localhost:5000/users')
    .then(res => {
      const characters = res.data.users_list;
      this.setState({ characters });
    })
    .catch(function (error) {
      //Not handling the error. Just logging into the console.
      console.log(error);
    });
}
makePostCall(character){
   return axios.post('http://localhost:5000/users', character)
    .then(function (response) {
      console.log(response);
      if(response.status === 201){
          return response.data};
    }).catch(function (error) {
      console.log(error);
      return false;
    });
 }
}

export default App;