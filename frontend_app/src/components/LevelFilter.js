import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import {colors} from '../constants'
import {mediaDesktop} from '../utils'

const selectBorderRadius = '.5em'

const Wrapper = styled.div`
  cursor: pointer;
  padding: .5em 1em;
  border-radius: 1em;
  background-color: gray;
  
  ${mediaDesktop} {
    margin-right: 2em;
  }
`

const Option = styled.label`
  color: #FFF;
  display: flex;
  font-size: 14pt;
  align-items: center;
  justify-content: space-between;
  
  &:not(:first-child) {
    margin-top: .5em
  }
`

const Input = styled.input`
  padding: 10px;
`

const Label = styled.span`
  color: #FFF;
`

class LevelFilter extends React.Component {
  constructor() {
    super()

    this.state = {
      title: null,
      isOpen: false,
      selected: new Set(),
    }

    this.toggleSelect = _toggleSelect.bind(this)
    this.handleChange = _handleChange.bind(this)
    this.mapLevels = _mapLevels.bind(this)
  }

  render() {
    const {levels} = this.props

    const _levels = _clearLevels(levels)

    const SelectStyled = styled.div`
      min-width: 4em;
      position: absolute;
      padding: .5em 1.2em;
      flex-direction: column;
      border: 2px solid gray;
      background-color: ${colors.backgroundColor};
      border-top-right-radius: ${selectBorderRadius};
      display: ${this.state.isOpen ? 'flex' : 'none'};
      border-bottom-left-radius: ${selectBorderRadius};
      border-bottom-right-radius: ${selectBorderRadius};
    `

    return (
      <Wrapper onClick={this.toggleSelect}>
        <Label>{this.state.title || 'Filter level'}</Label>
        <SelectStyled isOpen={this.state.isOpen}>
          {_levels.map(this.mapLevels)}
        </SelectStyled>
      </Wrapper>
    )
  }
}

LevelFilter.propTypes = {
  setFilter: PropTypes.func,
  handleChange: PropTypes.func,
  levels: PropTypes.arrayOf(PropTypes.number),
}

export default LevelFilter

function _mapLevels(level) {
  return  (
    <Option key={level}>
      <Input value={level}
             type="checkbox"
             onChange={this.handleChange}
             checked={this.state.selected.has(level)}/>
      {level}
    </Option>
  )
}

function _toggleSelect() {
  this.setState({isOpen: !this.state.isOpen})
}

function _clearLevels(levels) {
  // noinspection JSCheckFunctionSignatures
  return Array.from(new Set(levels.sort((num, next) => +num - (+next))))
}

function _handleChange(element) {
  const {checked, value} = element.target
  const action = checked ? 'add' : 'delete'

  this.props.setFilter(action, +value)
  this.props.handleChange(element)
}


