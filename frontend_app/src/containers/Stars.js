import React from 'react'
import styled from 'styled-components'

const Wrapper = styled.span`
  margin-right: 1em;
  color: #DBEAFF;
  
  i:not(:last-child) {
    margin-right: .2em;
  }
`

const Stars = () => (
  <Wrapper>
    <i className="fa fa-star"/>
    <i className="fa fa-star"/>
    <i className="fa fa-star"/>
    <i className="fa fa-star"/>
    <i className="fa fa-star"/>
  </Wrapper>
)

export default Stars
