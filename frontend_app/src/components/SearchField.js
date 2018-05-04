import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import {colors} from '../constants'


const Wrapper = styled.div`
  height: 4em;
  display: flex;
  padding-left: 1em;
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

const Input = styled.input`
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

class SearchField extends React.Component {
  constructor() {
    super()

    this.state = {hasText: false}

    this.handleChange = _handleChange.bind(this)
  }

  render() {
    const {hasText} = this.state
    const LabelComponent = hasText ? LabelWithText : Label
    return (
      <Wrapper>
        <Input id="search" size="40" onChange={this.handleChange} />
        <LabelComponent htmlFor="search">Type here to search a song</LabelComponent>
      </Wrapper>
    )
  }
}

SearchField.propTypes = {
  handleChange: PropTypes.func,
}

export default SearchField

function _handleChange(element) {
  this.setState({hasText: !!element.target.value})
  this.props.handleChange(element)
}
