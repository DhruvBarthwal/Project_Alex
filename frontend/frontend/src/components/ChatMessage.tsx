'use client'
import { Message } from '@/types/chat'

const ChatMessage = ({role , content} : Message) => {
  return (
    <div className= {`max-w-lg px-4 py-2 rounded-lg ${
        role == "user"
        ? "bg-blue-600 text-white self-end"
        : "bg-gray-200 text-black self-start"
    }`}>
        {content}
    </div>
  )
}

export default ChatMessage