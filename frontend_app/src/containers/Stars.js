import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

const Wrapper = styled.span`
  margin-right: 1em;
  color: #DBEAFF;
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
    const {rating} = this.state
    const stars = []

    for (let i = 1; i < 6; i++) {
      let className
      if (i < rating) {
        className = 'fa fa-star'
      } else if ((rating - i) % 1 !== 0) {
        className = 'fa fa-star-half-o'
      } else {
        className = 'fa fa-star-o'
      }

      stars.push(<I className={className} key={i} onClick={this.starClickWrapper(i + 1)}/>)
    }

    return <Wrapper>{stars}</Wrapper>
  }
}

Stars.propTypes = {
  rating: PropTypes.number,
}

export default Stars

function _starClickWrapper(rating) {
  return () => {
    this.setState({rating: rating})
  }
}
