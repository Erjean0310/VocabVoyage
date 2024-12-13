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

          />
        </el-form-item>

        <el-form-item class="in-2 input_box">
          <el-input
            :style="'--el-input-border-color:rgba(0,0,0,0)'"
            v-model="form.password"
            type="password"
            placeholder="password"
            prefix-icon="el-icon-lock"

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
        <el-link type="warning"  :to="{ path: '/signup' }">注册</el-link>
      </p>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import request from "../utils/request";


const form = ref({
  phone: '',
  password: '',
});

const handleLogin = () => {
  // 登录逻辑
  console.log('登录信息:', form.value);

  let url = "/users/login";
    request.post(url, form.value).then(res => {
      console.log("Message received")
      console.log(res)
        if (res.code == '0') {
          alert("登录失败，手机号或密码错误！！")
          console.log("成功接收到信息，但是出错")

        } else {
          console.log("登录成功")

        }
    })


};
</script>

<style scoped lang="less">
@import "Login_Signup.less";

</style>