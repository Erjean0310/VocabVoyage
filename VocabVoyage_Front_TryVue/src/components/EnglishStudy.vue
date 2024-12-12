<template>

<div class="common-layout">
    <el-container>
    <el-header>
        <el-input
            v-model="input"
            style="width: 50%"
            placeholder="Please input"
            clearable
        />
        <el-button :icon="Search" circle />


    </el-header>

    <el-container>
        <el-main>Main</el-main>
        <el-aside width="200px">Aside</el-aside>
    </el-container>

    </el-container>
</div>

</template>

<script setup>
import {Search} from '@element-plus/icons-vue'

</script>

<style scoped>
</style>