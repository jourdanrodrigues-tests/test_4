import React from 'react'

import Row from './containers/Row'
import SearchField from './components/SearchField'

const apiUrl = process.env.API_URL.replace(/\/$/, '')

class App extends React.Component {
  constructor() {
    super()

    this.state = {
      songs: [],
      unfilteredSongs: []
    }
    this.filterSongs = _filterSongs.bind(this)
  }

  componentWillMount() {
    _fetchSongs().then(songs => {
      this.setState({songs, unfilteredSongs: songs})
    })
  }

  render() {
    return (
      <div>
        <SearchField handleChange={this.filterSongs}/>
        {this.state.songs.map(_songsMap)}
      </div>
    )
  }
}

export default App

function _songsMap(song, i) {
  return <Row key={i} song={song}/>
}

function _fetchSongs() {
  return fetch(apiUrl + '/songs/').then(response => response.json())
}

function _filterSongs(event) {
  const value = event.target.value
  if (!value) {
    this.setState({songs: this.state.unfilteredSongs})
  }
  const songs = this.state.unfilteredSongs
  const regex = new RegExp(value)
  const filteredSongs = songs.filter(({title, artist}) => regex.test(title) || regex.test(artist))

  this.setState({songs: filteredSongs})
}
