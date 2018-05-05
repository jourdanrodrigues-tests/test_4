import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

const size = '1.7em'

const Wrapper = styled.span`
  color: white;
  display: flex;
  width: ${size};
  height: ${size};
  font-size: 10pt;
  border-radius: 50%;
  border: 2px solid #404247;
  align-items: center;
  justify-content: center;
`

const LevelDisplay = ({level}) => (
  <Wrapper>{level}</Wrapper>
)

LevelDisplay.propTypes = {
  level: PropTypes.number,
}

export default LevelDisplay
