const fetchMessages = async () => {
    // const response = await fetch('http://localhost:3001/messages')
    // return await response.json()

    // This is a mock implementation of fetching data from an API.
    // sleep for 1 second to simulate network latency
    await new Promise(resolve => setTimeout(resolve, 1000))

    return [
      { id: 1, text: "The quick brown fox jumps over the lazy dog.", score: 7.5, likes: 0 },
      { id: 2, text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.", score: 6.8, likes: 0 },
      { id: 3, text: "To be or not to be, that is the question.", score: 9.2, likes: 0 },
      { id: 4, text: "All that glitters is not gold.", score: 8.5, likes: 0 },
      { id: 5, text: "A journey of a thousand miles begins with a single step.", score: 7.9, likes: 0 },
    ]
}

const incermentFlush = async (id) => {
    // const response = await fetch(`http://localhost:3001/messages/${id}/like`, { method: 'POST' })
    // return await response.json()

    // This is a mock implementation of incrementing likes.
    // sleep for 1 second to simulate network latency
    await new Promise(resolve => setTimeout(resolve, 1000))

    return { id, likes: 1 }
}

export {fetchMessages, incermentFlush}
    