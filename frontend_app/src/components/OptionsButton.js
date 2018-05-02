import React from 'react'
import styled from 'styled-components'

const size = '2em'
const color = '#48494F'

const Wrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: ${size};
  width: ${size};
  border-radius: 50%;
  border: 2px solid ${color};
  background-color: transparent;
`

const dotSize = '5px'
const dotStep = multiply(dotSize, 1.7)

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

function multiply(string, multiplier) {
  return string.replace(/\d/, num => +num * multiplier)
}
