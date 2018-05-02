import React from 'react'
import styled from 'styled-components'

import SongInfo from './SongInfo'
import Logo from '../components/Logo'
import OptionsButton from '../components/OptionsButton'
import {mediaMobile, cssMultiply} from '../utils'

const border = '1px solid #212327'
const padding = '2em'
const mobilePadding = cssMultiply(padding, .5)

const Wrapper = styled.div`
  height: 4em;
  display: flex;
  align-items: center;
  padding: 0 ${padding};
  background-color: #0E0E12;
  justify-content: space-between;
  
  &:not(:first-child) {
    border-top: ${border};
  }

  &:last-child {
    border-bottom: ${border};
  }
  
  ${mediaMobile} {
    padding: 0 ${mobilePadding}
  }
`

const Row = () => (
  <Wrapper>
    <Logo/>
    <SongInfo/>
    <OptionsButton/>
  </Wrapper>
)

export default Row
