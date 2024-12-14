<template>
    <div class="tabs-container" :style="{ width: containerWidth + 'px', height: containerHeight + 'px' }">
      <el-tabs>
        <el-tab-pane label="Tab 1">Content 1</el-tab-pane>
        <el-tab-pane label="Tab 2">Content 2</el-tab-pane>
        <el-tab-pane label="Tab 3">Content 3</el-tab-pane>
      </el-tabs>
      <div class="resizer horizontal" @mousedown="onMouseDownHorizontal"></div>
      <div class="resizer vertical" @mousedown="onMouseDownVertical"></div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const containerWidth = ref(400);
  const containerHeight = ref(300);
  let isResizingHorizontal = ref(false);
  let isResizingVertical = ref(false);
  let startX = 0;
  let startY = 0;
  
  const onMouseDownHorizontal = (event) => {
    isResizingHorizontal.value = true;
    startY = event.clientY; // 记录初始 Y 坐标
  
    window.addEventListener('mousemove', onMouseMoveHorizontal);
    window.addEventListener('mouseup', onMouseUp);
  };
  
  const onMouseDownVertical = (event) => {
    isResizingVertical.value = true;
    startX = event.clientX; // 记录初始 X 坐标
  
    window.addEventListener('mousemove', onMouseMoveVertical);
    window.addEventListener('mouseup', onMouseUp);
  };
  
  const onMouseMoveHorizontal = (event) => {
    if (isResizingHorizontal.value) {
      const dy = event.clientY - startY; // 计算鼠标移动的 Y 距离
      containerHeight.value += dy; // 调整高度
      startY = event.clientY; // 更新初始 Y 坐标
    }
  };
  
  const onMouseMoveVertical = (event) => {
    if (isResizingVertical.value) {
      const dx = event.clientX - startX; // 计算鼠标移动的 X 距离
      containerWidth.value += dx; // 调整宽度
      startX = event.clientX; // 更新初始 X 坐标
    }
  };
  
  const onMouseUp = () => {
    isResizingHorizontal.value = false;
    isResizingVertical.value = false;
    window.removeEventListener('mousemove', onMouseMoveHorizontal);
    window.removeEventListener('mousemove', onMouseMoveVertical);
    window.removeEventListener('mouseup', onMouseUp);
  };
  </script>
  
  <style>
  .tabs-container {
    position: relative;
    border: 1px solid #ccc;
    overflow: hidden;
  }
  
  .resizer {
    position: absolute;
    background: #ccc;
    cursor: ew-resize; /* 默认光标 */
  }
  
  .resizer.horizontal {
    width: 100%;
    height: 10px;
    bottom: 0; /* 放在底部 */
    left: 0;
    cursor: ns-resize; /* 垂直拖动光标 */
  }
  
  .resizer.vertical {
    width: 10px;
    height: 100%;
    right: 0; /* 放在右侧 */
    top: 0;
    cursor: ew-resize; /* 水平拖动光标 */
  }
  </style>
  