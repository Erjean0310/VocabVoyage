<template>
  <div class="top_container">

    <div class="top_section">
        <!-- 上面的部分内容 -->
        <!-- <img src="http://vocab-voyage.oss-cn-beijing.aliyuncs.com/kk.jpg" style="width: 100px;height: 100px;"> -->

        <div class="menu" >
          <div class="search-container" style="display: flex; justify-content: center; align-items: center; flex: 1;">
            <el-input
              v-model="input2"
              style="max-width: 40%; margin: 0;"
              placeholder="search words"
              :prefix-icon="Search"
            />
            <el-button style="margin-left: 8px;">查找单词</el-button>
          </div>
          <el-button style="margin-left: 16px;" circle @click="drawer = true">
            <div style="width: 30px; height: 30px; overflow: hidden; border-radius: 50%;">
                <img src="http://vocab-voyage.oss-cn-beijing.aliyuncs.com/kk.jpg" alt="User Avatar" style="width: 100%; height: auto;" />
            </div>
            
          </el-button>
        </div>
        <!-- search -->


        <!-- user photo -->


    </div>




  </div>

  <div class="body_container">
    <div class="container">
      <div class="bottom-section">
        <div class="left-section">
          <!-- 左边的部分内容 -->

          <!-- TODO 高度写死问题 -->
          <el-scrollbar height="800px">
            <div v-for="item in 10" :key="item" class="scrollbar-demo-item">
              <div class="card">
                <a class="card1" href="#">
                  <div class="word_and_sound">
                    <p>This is heading</p>
                    <!-- TODO音标 -->
                    <el-button  
                      class="sound_button"
                      size="small" 
                      circle :icon="VideoPlay" 
                      @click="handle_sound" 
                      style="font-size: 24px; border-color: transparent; background-color: inherit;"
                    />
                  </div>
                  
                  <p class="small">Card description with lots of great facts and interesting details.</p>
                  <div class="go-corner" href="#">
                    <div class="go-arrow">
                      →
                    </div>
                  </div>
                </a>
              </div>
            </div>
          </el-scrollbar>

        </div>
        <div class="right-section">
          <div class="right-top">
            <!-- 右边上面的部分内容 -->

            <el-tabs type="border-card" class="detail_screen">
                <el-tab-pane label="Describe" class="markdown-card">
                    <!-- <div>123123</div> -->
                     <!-- TODO高度写死问题，滚动条问题 -->
                    <div v-html="parsedMarkdown" style="max-height: 600px; overflow-y: auto; "></div>
                </el-tab-pane>
                <el-tab-pane label="Chat">Chat</el-tab-pane>

            </el-tabs>



          </div>
          <div class="right-bottom">
            <!-- 右边下面的部分内容 -->
          </div>
        </div>
      </div>
    </div>


    <el-drawer v-model="drawer" title="I am the title" :with-header="false">
        <span>Hi there!</span>
        
    </el-drawer>


  </div>

</template>

<script setup>
import { onMounted, ref } from 'vue';

import { Search, VideoPlay } from '@element-plus/icons-vue';
import { marked } from 'marked';

const search_input = ref("")
const drawer = ref(false)

// // 接收传入的 Markdown 内容
// const props = defineProps({
//   markdownContent: {
//     type: String,
//     required: true
//   }
// })

const audio = new Audio('http://dict.youdao.com/dictvoice?type=1&audio=cancel');

const handle_sound = () => {
    audio.play();
}


const parsedMarkdown = ref(`
### 单词分析

  

**单词：** Baby

  

### 词义解析

  

"Baby"作为名词，代表婴儿、幼儿，是指在出生后到学步之前的人。除此之外，"Baby"也可以用来作为一个称呼，指代心爱的人，比如在情侣或夫妻之间通常用作温馨而甜蜜的昵称。

  

### 例句

  

1.  She cradled the baby in her arms. 她在怀里抱着婴儿。
2.  Our baby is learning to walk. 我们的婴儿正在学走路。
3.  He always calls me "baby". 他总是叫我“宝贝”。

  

### 词根分析

  

"Baby"这个词的词根是"babe"，来源于中古英语，也和其他诸如"bairn"的类似单词有关联，意为"婴儿"。

  

### 词缀分析

  

"Baby"这个词没有前后缀，是一个单根词。

  

### 发展历史和文化背景

  

"Baby"这个词起源于14世纪的英国，最初的用法是对新生儿的称呼。与此同时，这个词也可以用来称呼年纪较小的人，或者用作昵称表示亲昵和爱抚。

  

### 单词变形
// The baby in the cradle gurgled happily, his little hands reaching for the colorful mobile above. His mother sang a soft lullaby, her gentle voice filling the nursery.  
// 摇篮中的婴儿开心地咯咯笑着，他的小手伸向上面的彩色移动挂饰。他的妈妈温柔地唱着摇篮曲，她的声音充满了婴儿房。




    `)

    



// 组件挂载后解析 Markdown 内容
onMounted(() => {
  parsedMarkdown.value = marked(parsedMarkdown.value)
})



const handle_search = ()=>{
    // console.log(search_input.value)

    //TODO查单词

}


</script>



<style scoped>
@import "Card.less";

.top_section{
  width: 80%;

}
.menu{
  display: flex;
  justify-content: space-between;
  align-items: center;
  /* width: 80%; */
}
.body_container{
  display: flex;
  justify-content: center;
  align-items: center;
/* TODO演示颜色，后续可删除或替换背景 */
  background-color: rgb(113, 17, 17);
  /* 确保不出现滚动条 */
  /* overflow: hidden;  */
}
.container {
  display: flex;
  flex-direction: column;
  margin-top: 64px;
  /* 使整体占满视口高度，减去顶部固定高度 */
  height: calc(100vh - 64px); 

  width: 80%;

}

.top_container{
    position: fixed; /* 固定到页面顶部 */
    top: 0; /* 距离顶部0 */
    left: 0; /* 距离左侧0 */
    right: 0; /* 距离右侧0 */
    z-index: 1000; /* 确保在其他元素之上 */
    display: flex;
    justify-content: center;
    align-items: center;
    /* TODO演示颜色，后续可删除或替换背景 */
    background-color: rgb(17, 105, 163);
    height: 64px;
}

.top-section {
  /* 上面部分自适应内容高度 */
  flex: 0 0 64px; 
  height: 64px;
}

.bottom-section {
  display: flex;
  flex: 1; /* 下面部分占满剩余空间 */
}

.left-section {
  flex: 0 0 25%; /* 左边部分宽度 */
  /* overflow-y: auto; 使左边部分可滚动 */
  padding:16px 16px 16px 0px;
  /* TODO演示颜色，后续可删除或替换背景 */
  background-color: rgb(28, 212, 68);
}




/* TODO单词和声音 */
.word_and_sound{

  display: flex;
  justify-content: space-between;
  align-items: center;

}

.sound_button{

  right: 10px;
}

.right-section {
  display: flex;
  flex-direction: column;
  flex: 1; /* 右边部分占满剩余空间 */

  height: 100%;

}

.right-top {
  /* 右边上面部分占80% */
  flex: 0 0 80%; 
  padding:16px 0px 16px 16px;
  /* TODO演示颜色，后续可删除或替换背景 */
  background-color: blue;
  /* height: 80%; */
  /* max-height: 80%; */
}

.right-bottom {
    /* 右边下面部分占20% */
    /* flex: 0 0 20%; */
  flex: 1; 
  padding:16px 0px 16px 16px;
  /* TODO演示颜色，后续可删除或替换背景 */
  background-color: rgb(0, 187, 255);
  /* height: 20%; */
}

.detail_screen{
    height: 100%; /* 确保父元素的高度是100% */
    display: flex; /* 使用Flexbox布局 */
}

.markdown-card {
  max-height: 100%; /* 保持100%高度 */
  /* background-color: rgb(232, 11, 195); */
    /* padding-left: 20px; */
    /* text-align: left; */
  
  /* 自定义字体 */
  /* font-family: 'Arial', sans-serif; */
  /* font-size: 18px; */
  color: #333;
  background-color: aquamarine;
}



</style>