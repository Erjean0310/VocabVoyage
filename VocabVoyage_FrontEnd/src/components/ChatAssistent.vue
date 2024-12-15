<template>
    <div class="chat-container">
      <div class="chat-messages">
        <div v-for="(message, index) in messages" :key="index" class="message">
          <div :class="['message-bubble', message.role]">
            <span v-if="message.streaming">{{ message.content }}</span>
            <span v-else>{{ message.content }}</span>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="Type your message..."
        />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive } from 'vue'
  
  const messages = reactive([])
  const newMessage = ref('')
  
  const sendMessage = async () => {
    if (newMessage.value.trim()) {
      messages.push({ role: 'user', content: newMessage.value, streaming: false })
      newMessage.value = ''
  
      const response = await fetch('http://127.0.0.1:5000/chat', {//TODO 改成后端api接口
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ messages })
      })
  
      if (response.status === 200) {
        const reader = response.body.getReader()
        const decoder = new TextDecoder()
        let assistantMessage = ''
        messages.push({ role: 'assistant', content: '', streaming: true })
  
        while (true) {
          const { value, done } = await reader.read()
          if (done) break
  
          const chunk = decoder.decode(value, { stream: true })
          assistantMessage += chunk
          messages[messages.length - 1].content += chunk
        }
  
        messages[messages.length - 1].streaming = false
      } else {
        console.error('Error:', response.status)
      }
    }
  }
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    height: 500px;
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
  }
  
  .chat-messages {
    flex-grow: 1;
    padding: 10px;
    overflow-y: auto;
  }
  
  .message {
    margin-bottom: 10px;
  }
  
  .message-bubble {
    padding: 8px 12px;
    border-radius: 20px;
    max-width: 60%;
    word-wrap: break-word;
  }
  
  .user {
    background-color: #dcf8c6;
    margin-left: auto;
  }
  
  .assistant {
    background-color: #e2e2e2;
  }
  
  .chat-input {
    display: flex;
    padding: 10px;
    border-top: 1px solid #ccc;
  }
  
  .chat-input input {
    flex-grow: 1;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
  }
  
  .chat-input button {
    margin-left: 10px;
    padding: 5px 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }
  </style>