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
  border: 2px dashed #404247; // Temporary
  align-items: center;
  justify-content: center;
`

const Level = ({level, difficulty}) => (
  <Wrapper>
    {level}
  </Wrapper>
)

Level.propTypes = {
  level: PropTypes.number,
  difficulty: PropTypes.number,
}

export default Level
