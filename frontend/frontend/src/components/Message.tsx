import { ChatMessage } from "@/types/chat"

const Message = ({ role, text }: ChatMessage) => {
  const isAgent = role === "agent"

  return (
    <div
      className={`max-w-[80%] px-4 py-3 mt-2 rounded-2xl text-md
        ${isAgent 
          ? "bg-amber-800 text-amber-100 self-start rounded-tl-none"
          : "bg-red-800 text-white self-end rounded-tr-none"
        }`}
    >
      {text}
    </div>
  )
}

export default Message
