
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

@font-face {
  font-family: 'Showcard Gothic';
  src: url('../src/fonts/SHOWG.TTF') format('truetype');
  font-weight: normal;
  font-style: normal;
}

</style>
