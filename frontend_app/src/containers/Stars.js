import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import {apiFetch} from '../utils'

const Wrapper = styled.span`
  color: #DBEAFF;
  font-size: 14pt;
  margin-right: 1em;
`

const I = styled.i`
  cursor: pointer;

  &:not(:last-child) {
    margin-right: .2em;
  }
`

class Stars extends React.Component {
  constructor({rating}) {
    super()

    this.state = {rating}
    this.starClickWrapper = _starClickWrapper.bind(this)
  }

  render() {
    const {songId} = this.props
    const {rating} = this.state
    const stars = []

    for (let i = 1; i < 6; i++) {
      let className
      if (i <= rating) {
        className = 'fa fa-star'
      } else if (i - rating < 1) {
        className = 'fa fa-star-half-o'
      } else {
        className = 'fa fa-star-o'
      }

      stars.push(<I className={className} key={i} onClick={this.starClickWrapper(songId, i)}/>)
    }

    return <Wrapper>{stars}</Wrapper>
  }
}

Stars.propTypes = {
  songId: PropTypes.string,
  rating: PropTypes.number,
}

export default Stars

function _starClickWrapper(songId, rating) {
  return () => {
    apiFetch(`/songs/rating/${songId}/`, 'post', {rating})
      .then(() => {
        this.setState({rating})
      })
  }
}
