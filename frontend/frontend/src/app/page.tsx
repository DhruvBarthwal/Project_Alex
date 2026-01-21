'use client';
import ChatInput from '@/components/ChatInput';
import ChatWindow from '@/components/ChatWindow';
import { useState } from 'react';
import { Message } from '@/types/chat';
import { sendMessage } from '@/lib/api';

const page = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [lastEmailId, setLastEmailId] = useState<string | null>(null);
  const [compose, setCompose] = useState<{
    to: string | null;
    subject: string | null;
    body: string | null;
  }>({
    to: null,
    subject: null,
    body: null,
  });


  async function handleSend(text: string) {
  // 1️⃣ show user message
  setMessages((prev) => [...prev, { role: "user", content: text }]);

  // 2️⃣ send message + stored context to backend
  const data = await sendMessage(
    text,
    lastEmailId,
    compose.to,
    compose.subject,
    compose.body
  );

  // 3️⃣ STORE EMAIL ID (read / delete flow)
  if (data.email_id) {
    setLastEmailId(data.email_id);
  }

  if (data.deleted === true) {
    setLastEmailId(null);
  }

  // 4️⃣ COMPOSE FLOW MEMORY (THIS IS THE IMPORTANT PART)
  if (data.response?.includes("Who do you want to send")) {
    // starting compose
    setCompose({ to: null, subject: null, body: null });
  }

  if (data.response?.includes("What is the subject")) {
    setCompose((prev) => ({ ...prev, to: text }));
  }

  if (data.response?.includes("What should the email say")) {
    setCompose((prev) => ({ ...prev, subject: text }));
  }

  if (data.response?.includes("send this email")) {
    setCompose((prev) => ({ ...prev, body: text }));
  }

  if (data.response?.includes("email has been sent")) {
    setCompose({ to: null, subject: null, body: null });
  }

  // 5️⃣ show assistant message
  setMessages((prev) => [
    ...prev,
    { role: "assistant", content: data.response },
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