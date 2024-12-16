<template>  
    <div class="Home_conponents">
        <div class="left">
            <div class="title">
                <p class="title_text">VOCAB
                <br/>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——VOYAGE
                </p>
            </div>           
            <div class="description">
                <p class="description_text">
                    DESCRIPTION:<br/>
                    <u>Vocabulary Voyage is a English language learning website that provides users with a platform to learn English words and phrases. The website provides users with a variety of exercises and activities to help them improve their English language skills.</u>
                     
                </p>
            </div>
        </div>
        <div class="right">
            <div class="signIn_button">
                <button @click="handleSignIn" class="button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="60" viewBox="0 0 24 24" height="60" fill="none" class="svg-icon"><g stroke-width="2" stroke-linecap="round" stroke="#fff"><rect y="5" x="4" width="16" rx="2" height="16"></rect><path d="m8 3v4"></path><path d="m16 3v4"></path><path d="m4 11h16"></path></g></svg>
                    <span  class="lable"><u>sign in</u></span>
                </button>
            </div>
            <div class="english_study">
                <button class="goto_english_study_button" @click="showDialog = true"></button>
            </div>
        </div>


        <!-- 新增代码：弹出框 -->
        <div v-if="showDialog" class="dialog-overlay">
            <div class="dialog-box">
                <h3>Set Your Preferences</h3>
                <div class="slider-section">
                    <label for="word-percentage">Word Familiarity Percentage:</label>
                    <input
                        type="range"
                        id="word-percentage"
                        v-model="selectedPercentage"
                        min="10"
                        max="100"
                        step="10"
                    />
                    <span>{{ selectedPercentage }}%</span>
                </div>
                <div class="word-count-section">
                    <label>Word Count:</label>
                    <label><input type="radio" value="10" v-model="selectedWordCount" /> 10</label>
                    <label><input type="radio" value="20" v-model="selectedWordCount" /> 20</label>
                </div>
                <div class="dialog-actions">
                    <button @click="submitPreferences">Submit</button>
                    <button @click="showDialog = false">Cancel</button>
                </div>
            </div>
        </div>

    </div>
</template>


<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { userSignIn } from "../api/user";
import { getLearningWord } from "../api/word"

const router = useRouter()


const handleSignIn = async ()=>{
  console.log("start signin")
  const res = await userSignIn();
  console.log(res.data)
  const message = res.data.message;

  if(res.data.code == 0){
    alert(message)

  }else{
    alert(message);
    console.log("签到成功！")
  }


}

// 状态管理
const showDialog = ref(false); // 控制弹框显示
const selectedPercentage = ref(50); // 默认滑块值
const selectedWordCount = ref(10); // 默认单词数量

// 处理弹框提交
const submitPreferences = async () => {
    
    const res = await getLearningWord({
            new_word_weight: parseFloat((selectedPercentage.value / 100).toFixed(2)), // 转换为浮点数
            count: selectedWordCount.value,
        })

    console.log(res.data)
      
    emit_words("select_words",res.data.data)

    showDialog.value = false;
    router.push({ path: "/EnglishStudy", query: { wordIds: JSON.stringify(res.data.data) } });
};


// 声明 emit 函数
const emit_words = defineEmits(['select_words']);

</script>


<style> 
@import url('https://fonts.googleapis.com/css2?family=Bangers&family=Lexend:wght@100..900&family=Permanent+Marker&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

.Home_conponents{
    height: 96vh;
    width: 98vw; 
    display: flex;
}

body{
    z-index: -2;
    background-image: url(../../public/back3.jpg);
    background-repeat: no-repeat;
    background-size: cover;

}
body::after{
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to top, rgba(255, 255, 255, 0.319), rgba(255, 255, 255, 0));
    z-index: -1;
}
.sign_conponents{
    display: flex;
    justify-content: center;
    align-items: center;
}
.left{
    width: 50%;
    height: 100%;
    
}
.right{
    width: 48%;
    height: 100%;
    
}

.title{
    width: 100%;
    height: 60%;
    background-color: transparent;
    display: flex;                    /* 使其为flex容器 */
    justify-content: center;          /* 水平居中 */
    align-items: center;              /* 垂直居中 */
    flex-direction: column;           /* 纵向排列内容 */
}
.description{
    width: 100%;
    height: 40%;
    background-color: transparent;
    display: flex;                    /* 使其为flex容器 */
    justify-content: center;          /* 水平居中 */
    align-items: center;              /* 垂直居中 */
    flex-direction: column;           /* 纵向排列内容 */
}
.title_text{
    font-size: 6rem;
    font-family: 'Showcard Gothic';
    font-style: normal;
    font-weight: 400;
}
.description_text{
    top: 20%;
    font-size: 1.5rem;
    font-style: normal;
    padding-left: 10%;
    padding-bottom: 5%;
    padding-right: 15%;
    font-family: "Lexend", sans-serif;
    font-optical-sizing: auto;
    font-weight: 800;
    
}
.signIn_button{
    width: 100%;
    height: 70%;
    background-color: transparent;
    display: flex;                    /* 使其为flex容器 */
    justify-content: center;          /* 水平居中 */
    align-items: center;              /* 垂直居中 */
    flex-direction: column;           /* 纵向排列内容 */
}
.english_study{
    width: 100%;
    height: 28%;
    background-color: transparent;
    display: flex;
    justify-content: center;
}

.button {
  display: flex;
  flex-direction: column;         /* 改为列向排列 */
  justify-content: center;    /* 上对齐图标 */
  align-items: center;            /* 水平居中 */
  padding: 15px;                  /* 内边距适当调整 */
  gap: 15px;                       /* 图标与文字之间的间距 */
  height: 200px;                  /* 设置高度 */
  width: 200px;                   /* 设置宽度以形成正方形 */
  border: none ;
  background: #e530269d;
  border-radius: 20px;
  cursor: pointer;

}


.lable {
  line-height: 22px;
  font-size: 2rem;
  color: #fff;
  font-family: 'Showcard Gothic', sans-serif;
  letter-spacing: 1px;
  text-align: center;             /* 使文字居中 */

}

.button:hover {
  background: rgba(0, 0, 0, 0.646);
}

.button:hover .svg-icon {
  animation: slope 1s linear infinite;
}

.goto_english_study_button {
      display: inline-block; /* 确保按钮块状或内联块状 */
      width: 100%; /* 可根据需要设置 */
      height: 150px; /* 可根据需要设置 */
      position: relative; /* 为伪元素定位提供参考 */
      background-color:transparent; /* 按钮背景色 */
      border: none; /* 隐藏默认边框 */
      border-radius: 5px; /* 按钮圆角 */
      cursor: pointer; /* 鼠标指针样式 */
      overflow: hidden; /* 隐藏多余内容 */
      top: 30%;
      text-decoration: underline;
  }

  .goto_english_study_button::before {
      content: "S T A R T !"; /* 伪元素的内容 */
      text-decoration: underline;
      position: absolute; /* 伪元素绝对定位 */
      top: 50%; /* 垂直居中 */
      left: 50%; /* 水平居中 */
      transform: translate(-50%, -50%); /* 中心对齐 */
      font-size: 60px; /* 设置字体大小 */
      font-weight: 800; /* 设置字体粗细 */
      color: rgb(0, 0, 0); /* 设置文字颜色 */
      text-align: center; /* 文本居中 */
      pointer-events: none; /* 确保伪元素不影响按钮交互 */
      font-family: 'Showcard Gothic', sans-serif;
      margin-right: 10px
  }

  /* 新增代码：弹出框样式 */
.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.dialog-box {
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  width: 400px;
  text-align: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.dialog-box h3 {
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.slider-section {
  margin-bottom: 20px;
}

.slider-section label {
  display: block;
  margin-bottom: 10px;
  font-size: 1rem;
}

.slider-section input {
  width: 100%;
}

.word-count-section {
  margin-bottom: 20px;
}

.word-count-section label {
  margin-right: 10px;
  font-size: 1rem;
}

.dialog-actions {
  display: flex;
  justify-content: space-between;
}

.dialog-actions button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
}

.dialog-actions button:hover {
  background-color: #0056b3;
}

@keyframes slope {
  0% {
  }

  25% {
    transform: rotate(20deg);
  }
  75% {
    transform: rotate(-20deg);
  }


  100% {
    
  }
}

</style>