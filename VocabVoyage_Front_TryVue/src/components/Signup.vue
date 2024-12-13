<template>
<div class="login-container">
    <el-card class="login-form" shadow="hover" >
    <h1 class="in-1">WELCOME</h1>

    <el-form :model="form" ref="formRef" label-width="0" >

        <el-form-item class="in-2 input_box">
        <el-input
            :style="'--el-input-border-color:rgba(0,0,0,0);`:'"
            v-model="form.nick_name"
            placeholder="nick name"
            prefix-icon="el-icon-user"
        />
        </el-form-item>


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


        <el-form-item class="in-2 input_box">
        <el-input
            :style="'--el-input-border-color:rgba(0,0,0,0)'"
            v-model="form.confirm_password"
            type="password"
            placeholder="confirm password"
            prefix-icon="el-icon-lock"
        />
        </el-form-item>

        <!-- <el-form-item class="in-3">
            <el-checkbox v-model="form.remember">记住密码</el-checkbox>
        </el-form-item> -->

        <el-form-item class="in-3" label-width="auto">
            <!-- <button @click="handleLogin">注册</button> -->
            <el-button 
            style="background-color: aliceblue;color: black;"  
            size = "large" 
            @click="handleLogin">注册</el-button>
        </el-form-item>
    </el-form>

    <!-- <p class="reg in-3">
        还没有账号？
        <el-link type="warning" :to="{ path: '/signup' }" >注册</el-link>
    </p> -->
    </el-card>
</div>
</template>

<script setup>
import { ref } from 'vue';
import request from "../utils/request";


const form = ref({
    nick_name: '',
    phone: '',
    password: '',
    confirm_password: '',
});

const handleLogin = () => {
    console.log('注册信息:', form.value);

    let is_same_password = form.value.confirm_password === form.value.password;

    if(is_same_password){
        let url = "/users/register";
        request.post(url, form.value).then(res => {
            console.log("返回信息")
            console.log(res)

            if (res.code == '0') {
                alert("注册失败！" + res.message)
                console.log("成功接收到信息，但是出错")
            } else {
                console.log("注册成功！")
                alert("注册成功！")
            }
        })
    }else{
        alert("两次密码不一致！请重新输入！！！")
        console.log("两次密码输入不一致！！！")
    }
   


};
</script>


<style scoped lang="less">
@import "Login_Signup.less";

</style>

