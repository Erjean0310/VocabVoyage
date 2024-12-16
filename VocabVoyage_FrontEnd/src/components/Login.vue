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

             <!-- @click="userLogin(form)">登录</el-button> -->
        </el-form-item>
      </el-form>

      <p class="reg in-3">
        还没有账号？

        <el-link type="warning"  @click="handle_click_to_signup">注册</el-link>
         <!-- <el-button>注册</el-button> -->
      </p>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import request from "../request.js";
import { useRouter } from 'vue-router';
import {userLogin} from "../api/user.js";

const router = useRouter()

const form = ref({
  phone: '',
  password: '',
});

const handleLogin = async () => {
  // 登录逻辑

  const res = await userLogin(form.value);

  console.log(res)

  if(res.data.code == 1){

    console.log("返回信息显示登陆成功")
    router.push("/Home");

  }else{
    alert(res.data.message)
    
    console.log(res.data.message)
    form.value = {
      phone: '',
      password: '',
    }
  }

};

const handle_click_to_signup = ()=>{
  router.push("/Signup")

}
</script>

<style scoped lang="less">
@import "Login_Signup.less";

</style>