import { Toilet } from 'lucide-react'
import PropTypes from 'prop-types'

Loading.propTypes = {
  isLoading: PropTypes.bool.isRequired,
}

const Loading = ({ isLoading }) => {
  if (!isLoading) return null

  return (
    <div className="loading">
      Loading...
      <Toilet />
    </div>
  )
}

export default Loading
