'use client'
import ChatMessage from "./ChatMessage"
import { Message } from "@/types/chat"

const ChatWindow = ({messages}: {messages: Message[]}) => {
  return (
    <div className="flex flex-col gap-2 p-4 h-[70vh] overflow-y-auto border rounded-lg">
      {messages.map((msg, i) => (
        <ChatMessage key={i} {...msg} />
      ))}
    </div>
  )
}

export default ChatWindow