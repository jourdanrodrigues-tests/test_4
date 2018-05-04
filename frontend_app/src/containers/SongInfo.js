import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import LevelDisplay from '../components/LevelDisplay'
import Stars from './Stars'

const Wrapper = styled.div`
  flex-grow: 1;
  display: flex;
  padding-left: 1em;
  align-items: center;
`

const DataWrapper = styled.div`
  color: white;
  margin-left: 1em;
`

const Artist = styled.span`
  color: #878789;
`

const SubData = styled.div`
  font-size: 10pt;
  margin-top: .5em;
`

const SongInfo = ({title, artist, rating, difficulty, level}) => (
  <Wrapper>
    <LevelDisplay level={level} difficulty={difficulty}/>
    <DataWrapper>
      <span>{title}</span>
      <SubData>
        <Stars rating={rating}/>
        <Artist>{artist}</Artist>
      </SubData>
    </DataWrapper>
  </Wrapper>
)

SongInfo.propTypes = {
  artist: PropTypes.string,
  rating: PropTypes.number,
  title: PropTypes.string,
}

export default SongInfo
