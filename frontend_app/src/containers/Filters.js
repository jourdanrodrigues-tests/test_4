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
    <LevelFilter setFilter={setLevelFilter} handleChange={handleFilter} levels={levels}/>
    <TextFilter setFilter={setTextFilter} handleChange={handleFilter}/>
  </Wrapper>
)

Filters.propTypes = {
  handleFilter: PropTypes.func,
  setTextFilter: PropTypes.func,
  setLevelFilter: PropTypes.func,
  levels: PropTypes.arrayOf(PropTypes.number),
}

export default Filters


