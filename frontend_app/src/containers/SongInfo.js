import React from 'react'
import styled from 'styled-components'

import Level from '../components/Level'
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

const ArtistLabel = styled.span`
  color: #878789;
`

const SubData = styled.div`
  font-size: 10pt;
  margin-top: .5em;
`

const SongInfo = () => (
  <Wrapper>
    <Level/>
    <DataWrapper>
      <span>Scarborough fair - melody -</span>
      <SubData>
        <Stars/>
        <ArtistLabel>The Yousicians</ArtistLabel>
      </SubData>
    </DataWrapper>
  </Wrapper>
)

export default SongInfo
