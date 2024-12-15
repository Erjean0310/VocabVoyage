<template>
    <el-autocomplete
        v-model="state"
        :fetch-suggestions="querySearchAsync"
        placeholder="请输入单词"
        @select="handleSelect"
        :prefix-icon="Search"
    />
</template>

<script lang="ts" setup>

import { Search } from '@element-plus/icons-vue';

import { onMounted, ref } from 'vue'
import axios from 'axios'

const state = ref('')

interface WordItem {
id: number
spell: string
}

const links = ref<WordItem[]>([])

const querySearchAsync = async (queryString: string, cb: (arg: any) => void) => {
if (queryString.trim() === '') {
    cb([])
    return
}

// TODO改成实际url
try {
    const response = await axios.get(`http://xpvyrs.natappfree.cc/word/search?query=${queryString}`)
    const { data } = response.data
    const suggestions = data.map((item: WordItem) => ({ value: item.spell }))

    console.log(suggestions)
    cb(suggestions)
} catch (error) {
    console.error('Error fetching word suggestions:', error)
    cb([])
}
}

const handleSelect = (item: WordItem) => {
console.log('Selected word:', item)
emit('select', item.value)
}


// 声明 emit 函数
const emit = defineEmits(['select'])

</script>