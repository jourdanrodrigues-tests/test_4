import React from 'react'
import styled from 'styled-components'

import {cssMultiply, mediaMobile} from '../utils'
import logo from '../assets/logo.png'

const width = '4em'
const height = '3em'

const mobileMultiplier = .7
const mobileWidth = cssMultiply(width, mobileMultiplier)
const mobileHeight = cssMultiply(height, mobileMultiplier)


const Wrapper = styled.div`
  width: ${width};
  height: ${height};
  border-radius: 7px;
  background: #4FC613 url(${logo}) no-repeat center;
  background-size: auto 70%;
  
  ${mediaMobile} {
    width: ${mobileWidth};
    height: ${mobileHeight};
  }
`

const Logo = () => <Wrapper/>

export default Logo
