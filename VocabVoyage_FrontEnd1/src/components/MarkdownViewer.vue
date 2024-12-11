<template>
  <div>
    <!-- 控制卡片显示的按钮 -->
    <button @click="toggleCardVisibility">{{ showCard ? '隐藏卡片' : '显示卡片' }}</button>
    
    <!-- 只有在 showCard 为 true 时才显示卡片 -->
    <div v-if="showCard" class="markdown-card" v-html="parsedMarkdown"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { marked } from 'marked'

// 接收传入的 Markdown 内容
const props = defineProps({
  markdownContent: {
    type: String,
    required: true
  }
})

// 定义响应式数据
const parsedMarkdown = ref('')
const showCard = ref(false) // 控制卡片显示与隐藏

// 组件挂载后解析 Markdown 内容
onMounted(() => {
  parsedMarkdown.value = marked(props.markdownContent)
})

// 切换卡片的显示状态
const toggleCardVisibility = () => {
  showCard.value = !showCard.value
}
</script>

<style scoped>
.markdown-card {
  background-color: white;
  border: 1px solid #ccc;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  max-width: 1200px;
  position: fixed;
  top: 45%;
  right: 5%;
  transform: translateY(-50%);
  z-index: 1000;
  text-align: left;
  
  /* 自定义字体 */
  font-family: 'Arial', sans-serif;
  font-size: 18px;
  color: #333;
}

button {
  position: fixed;
  top: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #2980b9;
}
</style>
