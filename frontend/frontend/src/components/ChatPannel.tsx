"use client"
import {useEffect, useRef} from "react"
import Message from "./Message"
import { ChatMessage } from "@/types/chat"

type ChatProps = {
  messages: ChatMessage[]
}

const ChatPannel = ({ messages }: ChatProps) => {

  const bottomRef = useRef<HTMLDivElement | null>(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({behavior : "smooth"})
  },[messages])


  return (
    <div className="bg-red-900 rounded-tr-2xl backdrop-blur-3xl w-1/2 pb-30
                    flex flex-col gap-3 p-4 overflow-y-auto chat-scroll">
      {messages.length === 0 && (
        <p className="text-gray-400 text-md text-center mt-10">
          Start talking to Alex
        </p>
      )}

      {messages.map((msg) => (
        <Message key={msg.id} {...msg} />
      ))}
    </div>
  )
}

export default ChatPannel
