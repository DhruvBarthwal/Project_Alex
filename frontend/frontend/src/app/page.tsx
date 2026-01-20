'use client';
import ChatInput from '@/components/ChatInput';
import ChatWindow from '@/components/ChatWindow';
import { useState } from 'react';
import { Message } from '@/types/chat';
import { sendMessage } from '@/lib/api';

const page = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [lastEmailId, setLastEmailId] = useState<string | null>(null);


  async function handleSend(text: string){

    setMessages((prev) => [...prev, {role: "user", content: text}]);

    const data = await sendMessage(text, lastEmailId);

    if(data.email_id){
      setLastEmailId(data.email_id);
    }

    if(data.deleted == true){
      setLastEmailId(null);
    }

    setMessages((prev) =>[
      ...prev,
      {role: "assistant", content: data.response},
    ]);
  }
  return (
<main className="max-w-3xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Project Alex 🧠📬</h1>
      <ChatWindow messages={messages} />
      <ChatInput onSend={handleSend} />
    </main>
  )
}

export default page