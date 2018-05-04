import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import {colors} from '../constants'

const selectBorderRadius = '.5em'

const Wrapper = styled.div`
  padding: .5em 1em;
  background-color: gray;
  border-radius: 1em;
`

const Option = styled.label`
  color: #FFF;
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
  }

  render() {
    const {levels, handleChange} = this.props

    const _mapLevels = _getMapLevels(handleChange, this.state.selected)
    const _levels = _clearLevels(levels)



    const SelectStyled = styled.div`
      position: absolute;
      padding: .5em 1.2em;
      flex-direction: column;
      border: 2px solid gray;
      background-color: ${colors.backgroundColor};
      display: ${this.state.isOpen ? 'flex' : 'none'};
      border-bottom-left-radius: ${selectBorderRadius};
      border-bottom-right-radius: ${selectBorderRadius};
    `

    return (
      <Wrapper onClick={this.toggleSelect}>
        <Label>{this.state.title || 'Filter level'}</Label>
        <SelectStyled isOpen={this.state.isOpen}>
          {_levels.map(_mapLevels)}
        </SelectStyled>
      </Wrapper>
    )
  }
}

LevelFilter.propTypes = {
  handleChange: PropTypes.func,
  levels: PropTypes.arrayOf(PropTypes.number),
}

export default LevelFilter

function _getMapLevels(handleChange, selected) {
  return (level) => (
    <Option key={level}>
      <input type="checkbox" checked={selected.has(level)} onChange={handleChange} value={level}/>
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


