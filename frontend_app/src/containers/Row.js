import React from 'react'
import styled from 'styled-components'

import Logo from '../components/Logo'
import Level from '../components/Level'
import OptionsButton from '../components/OptionsButton'

const border = '1px solid #212327'
const padding = '2em'

const Wrapper = styled.div`
  height: 4em;
  display: flex;
  padding: 0 ${padding};
  align-items: center;
  background-color: #0E0E12;
  justify-content: space-between;
  
  &:not(:last-child) {
    border-top: ${border};
  }

  &:last-child {
    border-bottom: ${border};
  }
`

const InfoWrapper = styled.div`
  flex-grow: 1;
  padding-left: 1em;
`

const Row = () => (
  <Wrapper>
    <Logo/>
    <InfoWrapper>
      <Level/>
    </InfoWrapper>
    <OptionsButton/>
  </Wrapper>
)

export default Row
