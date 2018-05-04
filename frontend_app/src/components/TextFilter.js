import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import {colors} from '../constants'


const Wrapper = styled.div`
  display: flex;
  align-items: center;
  background-color: ${colors.backgroundColor};
`

const color = '#FFF'
const focusColor = '#CCC'
const delay = '.3s'

const Label = styled.label`
  color: ${color};
  position: absolute;
  transition: ${delay};
`

const labelCssPropsWhenText = `
  font-size: 8pt;
  color: ${focusColor};
  transform: translateY(-1.7em);
`

const LabelWithText = styled(Label)`
  ${labelCssPropsWhenText}
`

const Input = styled.input.attrs({size: 34})`
  height: 2em;
  border: none;
  color: white;
  user-select: none;
  background-color: transparent;
  border-bottom: 2px solid ${color};
  transition: ${delay};
  
  &:focus {
    border-bottom: 2px solid ${focusColor};
  }
  
  &:focus ~ ${Label} {
    ${labelCssPropsWhenText}
  }
`

class TextFilter extends React.Component {
  constructor() {
    super()

    this.state = {hasText: false}

    this.handleChange = _handleChange.bind(this)
  }

  render() {
    const LabelComponent = this.state.hasText ? LabelWithText : Label
    return (
      <Wrapper>
        <Input id="search" onChange={this.handleChange} />
        <LabelComponent htmlFor="search">Type here to search for a song</LabelComponent>
      </Wrapper>
    )
  }
}

TextFilter.propTypes = {
  handleChange: PropTypes.func,
}

export default TextFilter

function _handleChange(element) {
  this.setState({hasText: !!element.target.value})
  this.props.handleChange(element)
}
