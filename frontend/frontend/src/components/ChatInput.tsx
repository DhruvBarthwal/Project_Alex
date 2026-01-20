'use client';
import {useState} from 'react'

const ChatInput = ( {onSend} : {onSend : (text : string) => void}) => {

    const [text, setText] = useState("");

return (
    <div className="flex gap-2 mt-4">
      <input
        className="flex-1 border rounded px-3 py-2"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type here..."
      />
      <button
        className="bg-black text-white px-4 py-2 rounded"
        onClick={() => {
          if (!text.trim()) return;
          onSend(text);
          setText("");
        }}
      >
        Send
      </button>
    </div>
  )
}

export default ChatInput