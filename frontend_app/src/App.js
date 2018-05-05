import React from 'react'

import {apiFetch} from './utils'
import Songs from './containers/Songs'
import Filters from './containers/Filters'

class App extends React.Component {
  constructor() {
    super()

    this.state = {
      songs: [],
      unfilteredSongs: [],
      levels: [],
      filters: {
        text: undefined,
        level: new Set(),
      },
    }

    this.filterSongs = _filterSongs.bind(this)
    this.setTextFilter = _setTextFilter.bind(this)
    this.setLevelFilter = _setLevelFilter.bind(this)
  }

  componentWillMount() {
    apiFetch('/songs/').then(songs => {
      this.setState({
        songs,
        unfilteredSongs: songs,
        levels: songs.map(({level}) => level),
      })
    })
  }

  render() {
    return (
      <div>
        <Filters handleFilter={this.filterSongs}
                 setTextFilter={this.setTextFilter}
                 setLevelFilter={this.setLevelFilter}
                 levels={this.state.levels}/>
        <Songs songs={this.state.songs}/>
      </div>
    )
  }
}

export default App

function _setTextFilter(value) {
  this.state.filters.text = value || undefined
}


/**
 * @param {String} action - Values are "add" and "remove" since "level" is a Set
 * @param {number} value
 */
function _setLevelFilter(action, value) {
  this.state.filters.level[action](value)
}

function _filterSongs() {
  const {text: textFilter, level: levelFilter} = this.state.filters

  if (!textFilter && !levelFilter) {
    this.setState({songs: this.state.unfilteredSongs})
    return
  }

  let songs = this.state.unfilteredSongs

  if (textFilter) {
    const regex = new RegExp(textFilter)
    songs = songs.filter(({title, artist}) => regex.test(title) || regex.test(artist))
  }

  if (levelFilter.size !== 0) {
    songs = songs.filter(({level}) => levelFilter.has(level))
  }

  this.setState({songs: songs})
}
