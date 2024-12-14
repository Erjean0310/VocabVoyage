
<template>

<!-- <button @click="goToSignup">前往注册页面</button> -->
<!-- <router-view name="/Signup"></router-view> -->
  <!-- <Study></Study> -->
  <!-- <EnglishStudy></EnglishStudy> -->
  
  <!-- <test></test> -->
  <!-- <Login></Login> -->
  <!-- <Signup></Signup> -->
  <!-- <ChatAssistent ></ChatAssistent> -->

  <router-view></router-view>
</template>

<script setup>


import Study from './components/Study.vue';
import EnglishStudy from './components/EnglishStudy.vue';
import Login from './components/Login.vue';
import ChatAssistent from './components/ChatAssistent.vue';
import Signup from './components/Signup.vue';
import test from './components/test.vue';

import { useRouter } from 'vue-router';

// 使用 useRouter 钩子函数来获取路由实例
const router = useRouter();

// 定义一个方法用于跳转
const goToSignup = () => {
  router.push('/Signup');
};
</script>


<style scoped>

*{
  margin: 0;
}

</style>
