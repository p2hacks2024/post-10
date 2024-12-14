const fetchMessages = async () => {
    // const response = await fetch('http://localhost:3001/messages')
    // return await response.json()

    // This is a mock implementation of fetching data from an API.
    // sleep for 1 second to simulate network latency
    console.log('fetching data')
    await new Promise(resolve => setTimeout(resolve, 2000))

    return [
      { id: 1, text: "なんで電車、遅れてるのに理由の説明ないんだろう。", score: 7.5, likes: 0 },
      { id: 2, text: "また書類作成ミス…自分がやった方が早いんだけど。", score: 6.8, likes: 0 },
      { id: 3, text: "天気予報、雨って言ってたのにめっちゃ晴れてる…傘持ってきた意味ない。", score: 9.2, likes: 0 },
      { id: 4, text: "会議、なんでこんなに長いんだろう…中身ほぼないのに。", score: 8.5, likes: 0 },
      { id: 5, text: "Wi-Fiがまた繋がらない…こういう時に限って急ぎの作業あるんだよな。", score: 7.9, likes: 0 },
    ]
}

const incermentFlush = async (id) => {
    // const response = await fetch(`http://localhost:3001/messages/${id}/like`, { method: 'POST' })
    // return await response.json()

    // This is a mock implementation of incrementing likes.
    // sleep for 1 second to simulate network latency
    await new Promise(resolve => setTimeout(resolve, 2000))

    return { id, likes: 1 }
}

export {fetchMessages, incermentFlush}
    