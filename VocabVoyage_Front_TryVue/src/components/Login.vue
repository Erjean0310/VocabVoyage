<template>
  <div class="login-container">
    <el-card class="login-form" shadow="hover" >
      <h1 class="in-1">WELCOME</h1>

      <el-form :model="form" ref="formRef" label-width="0" >
        <el-form-item class="in-2 input_box">
          <el-input
            :style="'--el-input-border-color:rgba(0,0,0,0);`:'"
            v-model="form.phone"
            placeholder="phone"
            prefix-icon="el-icon-user"
            clearable
          />
        </el-form-item>

        <el-form-item class="in-2 input_box">
          <el-input
            :style="'--el-input-border-color:rgba(0,0,0,0)'"
            v-model="form.password"
            type="password"
            placeholder="password"
            prefix-icon="el-icon-lock"
            clearable
          />
        </el-form-item>

        <el-form-item class="in-3">
          <!-- <el-checkbox v-model="form.remember">记住密码</el-checkbox> //TODO 记住密码功能-->
        </el-form-item>

        <el-form-item class="in-3" label-width="auto">
            <!-- <button @click="handleLogin">登录</button> -->
            <el-button 
              style="background-color: aliceblue;color: black;"  
              size = "large" 
              @click="handleLogin">登录</el-button>
        </el-form-item>
      </el-form>

      <p class="reg in-3">
        还没有账号？
        <el-link type="warning" :to="{ path: '/signup' }" >注册</el-link>
      </p>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  phone: '',
  password: '',
  remember: false,
});

const handleLogin = () => {
  // 登录逻辑
  console.log('登录信息:', form.value);
};
</script>

<style scoped>

a{
  font-size: 20px;
  color: #ffffff;
}
.login-container {

  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url(../../public/back.jpg);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  z-index: -1;
  text-align: center;
  align-items: center;
}

.login-container::after{
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.2);
    z-index: 0;
}

.login-form {
  width: 35%;
  padding: 50px 10px;
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  color: white;
  z-index: 1;


  
}

.input_box{
    border: 1px solid white;
    display: flex;
    align-items: center;
    justify-content: space-between; 
    margin-bottom: 40px;
    height: 60px;
    width: 100%;
    border-radius: 50px;
    box-shadow: 0 0 5px rgba(255, 255, 255, 0.459);

}

/* 背景色设置为透明 */
/* 提示框的字体颜色 */
/* 输入框颜色 */
/* 去除输入时边框颜色 */
:deep(.el-input__wrapper) {
background: transparent;
}

:deep(input::-webkit-input-placeholder) {
  color: #ffffff;
}

:deep(.el-input__inner) {
  background-color: rgba(0, 0, 0, 0) !important;
    color: #ffffff;
    font-size: 30px;
}

:deep(.el-input__wrapper) {
    box-shadow: none !important;
    /* border-bottom: 1px solid black; */
    border-radius: 0;
}



h1 {
  font-size: 3rem;
  margin-bottom: 50px;
  letter-spacing: 3px;
  animation: reloadA 1s ease-out forwards;
  opacity: 0;
  animation-delay: 0.2s;
}

.in-1{
    animation: reloadA 0.8s ease-out forwards;
    opacity: 0;
    animation-delay: 0.1s;
}
.in-2{

    animation: reloadA 1.0s ease-out forwards;
    opacity: 0;
    animation-delay: 0.2s;
}

.in-3{
    animation: reloadA 1.2s ease-out forwards;
    opacity: 0;
    animation-delay: 0.4s;
}

.in-4{
    animation: reloadA 1.4s ease-out forwards;
    opacity: 0;
    animation-delay: 0.6s;
}
button{
    font-size: 1.2rem;
    height: 60px;
    width: 100%;
    border-radius: 50px;
    font-weight: 600;
    letter-spacing: 1px;
    margin-bottom: 25px;
    cursor: pointer;
    transition: 0.3s;
    border-color: rgba(0, 0, 0, 0);
}
button:hover{
    background-color: rgb(221, 221, 221);
}


.reg {
  font-size: 1.2rem;
  color: white;
  margin-top: 40px;
}
</style>

<style>
@keyframes reloadA {
  from {
    transform: translateY(250px);
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>