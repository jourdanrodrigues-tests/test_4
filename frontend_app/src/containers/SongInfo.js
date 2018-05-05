import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import LevelDisplay from '../components/LevelDisplay'
import Stars from './Stars'

const Wrapper = styled.div`
  flex-grow: 1;
  display: flex;
  padding-left: .5em;
  align-items: center;
`

const DataWrapper = styled.div`
  color: white;
  margin-left: .5em;
`

const Artist = styled.span`
  color: #878789;
`

const SubData = styled.div`
  font-size: 10pt;
  margin-top: .5em;
`

const SongInfo = ({id, title, artist, rating, difficulty, level}) => (
  <Wrapper>
    <LevelDisplay level={level}/>
    <DataWrapper>
      <span>{title}</span>
      <SubData>
        <Stars rating={rating} songId={id}/>
        <Artist>{artist}</Artist>
      </SubData>
    </DataWrapper>
  </Wrapper>
)

SongInfo.propTypes = {
  id: PropTypes.string,
  level: PropTypes.number,
  title: PropTypes.string,
  artist: PropTypes.string,
  rating: PropTypes.number,
  difficulty: PropTypes.number,
}

export default SongInfo
