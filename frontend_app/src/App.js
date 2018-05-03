import React from 'react'
import 'font-awesome/css/font-awesome.min.css'

import Row from './containers/Row'

const apiUrl = process.env.API_URL.replace(/\/$/, '')

class App extends React.Component {
  constructor() {
    super()

    this.state = {songs: []}
  }

  componentWillMount() {
    _fetchSongs().then(songs => {
      this.setState({songs})
    })
  }

  render() {
    const songs = this.state.songs.map((song, i) => <Row key={i} song={song}/>)
    return <div>{songs}</div>
  }
}

export default App

function _fetchSongs() {
  return fetch(apiUrl + '/songs/').then(response => response.json())
}
