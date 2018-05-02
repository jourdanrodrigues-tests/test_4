import React from 'react'
import styled from 'styled-components'

const size = '1.2em'

const Wrapper = styled.span`
  color: white;
  display: flex;
  width: ${size};
  height: ${size};
  font-size: 12pt;
  border-radius: 50%;
  border: 2px dashed #404247; // Temporary
  align-items: center;
  justify-content: center;
`

const Level = () => (
  <Wrapper>
    4
  </Wrapper>
)

export default Level
