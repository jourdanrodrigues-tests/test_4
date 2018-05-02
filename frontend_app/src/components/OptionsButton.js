import React from 'react'
import styled from 'styled-components'

import {cssMultiply} from '../utils'

const size = '1em'
const color = '#48494F'

const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: ${size};
  width: ${size};
  border-radius: 50%;
  border: 1px solid ${color};
  background-color: transparent;
`

const dotSize = '2px'
const dotStep = cssMultiply(dotSize, 2)

const Dots = styled.div`
  display: flex;
  align-items: center;

  &:after {
    transform: translateX(${dotStep});
  }

  &:before {
    transform: translateX(-${dotStep});
  }

  &:after, &:before {
    content: '';
    display: block;
    position: absolute;
  }

  &, &:after, &:before {
    height: ${dotSize};
    width: ${dotSize};
    border-radius: 50%;
    background-color: ${color};
  }
`

const OptionsButton = () => (
  <Wrapper>
    <Dots/>
  </Wrapper>
)

export default OptionsButton
