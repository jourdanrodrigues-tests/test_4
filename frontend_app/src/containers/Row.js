import React from 'react'
import styled from 'styled-components'

import OptionsButton from '../components/OptionsButton'

const border = '1px solid #212327'

const Wrapper = styled.div`
  height: 4em;
  width: 100%;
  display: flex;
  align-items: center;
  background-color: #0E0E12;
  
  &:not(:last-child) {
    border-top: ${border};
  }

  &:last-child {
    border-bottom: ${border};
  }
`

const Row = () => (
  <Wrapper>
    <OptionsButton/>
  </Wrapper>
)

export default Row
