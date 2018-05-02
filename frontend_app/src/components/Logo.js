import React from 'react'
import styled from 'styled-components'

import logo from '../assets/logo.png'

const Wrapper = styled.div`
  width: 4em;
  height: 3em;
  border-radius: 7px;
  background: #4FC613 url(${logo}) no-repeat center;
  background-size: auto 70%;
`

const Logo = () => <Wrapper/>

export default Logo
