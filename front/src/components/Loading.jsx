import { Toilet } from 'lucide-react'
import style from './Loading.module.css'
import PropTypes from 'prop-types'


const Loading = ({ isLoading }) => {
  if (!isLoading) return null

  return (
    <div className={style.container}>
      <Toilet size={32} className={style.loading}/>
    </div>
  )
}

Loading.propTypes = {
  isLoading: PropTypes.bool.isRequired,
}

export default Loading
