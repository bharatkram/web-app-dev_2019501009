import React from 'react';
import {View, Button, Text, ScrollView, StyleSheet, Switch, TextInput} from 'react-native'
import {Constants} from 'expo'

let id = 0

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  part: {
    flex: 1,
  },
  button: {
    width:'20%',
  },
  textinput: {
    padding:5,
    borderColor:'black',
    borderWidth:2,
    width:'75%',
  }
})

const Todo = props => (
  <View style={styles.container}>
    <Button onPress={props.onDelete} title="delete" />
    <Text>{props.todo.text}</Text>
  </View>
)

export default class App extends React.Component {
  constructor() {
    super()
    this.state = {
      task: "",
      todos: [],
    }
  }

  handleText = (text) => {
    this.setState({task:text})
  }

  addTodo() {
    if (this.state.task != "") {
    id++
    const text = this.state.task
    this.setState({
      todos: [
        ...this.state.todos,
        {id: id, text: text, checked: false},
      ], 
    })
    }
  }

  removeTodo(id) {
    this.setState({
      todos: this.state.todos.filter(todo => todo.id !== id)
    })
  }

  render() {
    return (
      <View style={[styles.part]}>
        <View style = {styles.container}>
          <View style={[styles.textinput]}><TextInput placeholder="ToDo Activity..." onChangeText={this.handleText}/></View>
          <View style={[styles.button]}><Button onPress={() => this.addTodo()} title="Add" /></View>
        </View>
        <ScrollView style={styles.part}>
          {this.state.todos.map(todo => (
            <Todo
              onDelete={() => this.removeTodo(todo.id)}
              todo={todo}
            />
          ))}
        </ScrollView>
      </View>
    )
  }
}
