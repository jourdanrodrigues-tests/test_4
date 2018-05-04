import React from 'react'
import PropTypes from 'prop-types'

import Song from './Song'


const Songs = ({songs}) => <div>{songs.map(_songsMap)}</div>

Songs.propTypes = {
  songs: PropTypes.arrayOf(PropTypes.object),
}

export default Songs

function _songsMap(song, i) {
  return <Song key={i} song={song}/>
}
