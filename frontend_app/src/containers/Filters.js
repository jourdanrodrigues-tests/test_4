import React from 'react'
import PropTypes from 'prop-types'
import styled from 'styled-components'

import TextFilter from '../components/TextFilter'
import LevelFilter from '../components/LevelFilter'


const Wrapper = styled.div`
  height: 4em;
  display: flex;
  align-items: center;
  justify-content: space-around;
`

const Filters = ({handleFilter, setTextFilter, setLevelFilter, levels}) => (
  <Wrapper>
    <LevelFilter handleChange={_getLevelFilter(setLevelFilter, handleFilter)} levels={levels}/>
    <TextFilter handleChange={_getTextFilter(setTextFilter, handleFilter)}/>
  </Wrapper>
)

Filters.propTypes = {
  handleFilter: PropTypes.func,
  setTextFilter: PropTypes.func,
  setLevelFilter: PropTypes.func,
  levels: PropTypes.arrayOf(PropTypes.number),
}

export default Filters

function _getTextFilter(setFilter, handleFilter) {
  return element => {
    setFilter(element.target.value)
    handleFilter()
  }
}

function _getLevelFilter(setFilter, handleFilter) {
  return element => {
    const {checked, value} = element.target
    const action = checked ? 'add' : 'delete'

    setFilter(action, +value)
    handleFilter()
  }
}


