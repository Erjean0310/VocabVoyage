<template>
    <div class="search-container" style="display: flex; justify-content: center; align-items: center; flex: 1;">

        <el-autocomplete
            v-model="state"
            style="max-width: 40%; margin: 0;  ;;;;;;"
            :fetch-suggestions="querySearchAsync"
            placeholder="search words"
            @select="handleSelect"
            :prefix-icon="Search"
        />

        <el-button @click="handleSelect({ value: state })" style="margin-left: 8px;">查找单词</el-button>
    </div>
</template>


<script setup>


import { Search } from '@element-plus/icons-vue';


import { onMounted, ref } from 'vue';
import axios from 'axios';
import { wordFuzzySearch } from '../api/word';

const state = ref('');


const querySearchAsync = async (queryString, cb) => {
  if (queryString.trim() === '') {
    cb([]);
    return;
  }

  // TODO改成实际url
  try {

    const response = await wordFuzzySearch(queryString)
    // const response = await axios.get(`http://ahv5jw.natappfree.cc/word/search?query=${queryString}`);
    const { data } = response.data;
    const suggestions = data.map((item) => ({ value: item.spell }));

    cb(suggestions);
  } catch (error) {
    console.error('Error fetching word suggestions:', error);
    cb([]);
  }
};

const handleSelect = (item) => {
  console.log('组件内选择上了:', item);
  // 将选中的单词通过事件传递给父组件
  emit('select', item.value);
};

// 声明 emit 函数
const emit = defineEmits(['select']);
</script>


<style scoped>
    
</style>