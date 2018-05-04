import React from 'react'
import styled from 'styled-components'

import SongInfo from './SongInfo'
import {colors} from '../constants'
import Logo from '../components/Logo'
import {mediaMobile, cssMultiply} from '../utils'
import OptionsButton from '../components/OptionsButton'

const border = '1px solid #212327'
const padding = '2em'
const mobilePadding = cssMultiply(padding, .5)

const Wrapper = styled.div`
  height: 4em;
  display: flex;
  align-items: center;
  padding: 0 ${padding};
  justify-content: space-between;
  background-color: ${colors.backgroundColor};
  
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

const Row = ({song: {title, artist, rating, level, difficulty}}) => (
  <Wrapper>
    <Logo/>
    <SongInfo title={title} artist={artist} rating={rating} level={level} difficulty={difficulty}/>
    <OptionsButton/>
  </Wrapper>
)

export default Row
