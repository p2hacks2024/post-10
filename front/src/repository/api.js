const fetchMessages = async () => {
  const response = await fetch("http://54.168.2.235/messages");

  const data = await response.json();

  console.log(data);
    
  return data;

    // return [
    //   { id: 1, text: "なんで電車、遅れてるのに理由の説明ないんだろう。", score: 7.5, likes: 0 },
    //   { id: 2, text: "また書類作成ミス…自分がやった方が早いんだけど。", score: 6.8, likes: 0 },
    //   { id: 3, text: "天気予報、雨って言ってたのにめっちゃ晴れてる…傘持ってきた意味ない。", score: 9.2, likes: 0 },
    //   { id: 4, text: "会議、なんでこんなに長いんだろう…中身ほぼないのに。", score: 8.5, likes: 0 },
    //   { id: 5, text: "Wi-Fiがまた繋がらない…こういう時に限って急ぎの作業あるんだよな。", score: 7.9, likes: 0 },
    // ]
}

const incermentFlush = async (id) => {
    const response = await fetch(`http://54.168.2.235/incerment_flush/${id}`, {
      method: "PUT",
    });
  
    return await response.json()
}

export {fetchMessages, incermentFlush}
    