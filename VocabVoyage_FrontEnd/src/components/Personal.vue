<script setup>
import { ref, onMounted } from 'vue';
import { userLogout, getUserStudyData ,getUserSigninRecord} from "../api/user";

import { adminCheck , adminExportData } from "../api/admin";

import router from '../router';
import Calender from "./Calender.vue"



// http://vocab-voyage.oss-cn-beijing.aliyuncs.com/kk.jpg
// const avatarUrl = ""; // 示例图片地址,替换成真实的图片路径或链接
const data = ref({
    name: '110',
    radio: '12345@qq.com',
    checkbox: [],
    select: '',
    multipleSelect: [],
    oldPassword: '110',
    newPassword: '',
    confirmPassword: '',
    phone: '110'
});

const add = () => {
    console.log(data.value);
    dialog.value = false;
};

const reset = () => {
    data.value = {
        name: '',
        radio: '',
        checkbox: [],
        date: '',
        select: '',
        multipleSelect: [],
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
    };
    dialog.value = false;
};

const dialog = ref(false);

const dialogClose = () => {
    console.log("关闭");
};


const handleReturnButton = async ()=>{
    router.push("/EnglishStudy").then(() => {
            window.location.reload(); // 刷新页面
        });
}

const handleAdminButton = async ()=>{
    const res = await adminCheck();
    console.log(res);

    if(res.data.code == 1){
        router.push("/AdminPage").then(() => {
            window.location.reload(); // 刷新页面
        });
    }else{
        alert("进入管理员页面失败！请检查登录账号是否有管理员权限！")
        console.log(res)
    }


}

const handleLogoutButton = async ()=>{
    const res = await userLogout();
    console.log(res)

    if(res.data.code == 1){
        alert(res.data.message);
        router.push("/").then(() => {
            window.location.reload(); // 刷新页面
        });
        
    }else{
        alert("退出登录失败！")
        console.log(res.data.message)
    }

}

const studyData = ref(null); // 用于存储学习数据

// 在组件加载时请求学习数据
onMounted(async () => {
    const res = await getUserStudyData();
    if (res.data.code === 1) {
        studyData.value = res.data.data; // 存储返回的学习数据
    } else {
        console.error("获取学习数据失败:", res.data.message);
    }
});

</script>

<template>

    <div class="container">
        <!-- <div class="info-text">基本信息</div> -->
        <div class="avatar-container">
            <img src="../../public/kk.png" class="avatar-style bg-gray-circle" />
            <!-- <avatar :src="avatarUrl" size="large" class="avatar-style bg-gray-circle"></avatar> -->
            <calender style="width: 300px;height: 300px;"></calender>
        </div>

        <!-- <Calender style="width: 300px;height: 300px;"></Calender> -->

        <div class="user-info">用户个人信息</div>
        <div class="user-detail">
            <div>账号名：{{ data.name }}</div>
            <div>手机号：(+86){{ data.phone }}</div>

            <div>密码："安全"
                <el-button @click="dialog = true" class="reset-btn">重置</el-button>
            </div>
        </div>
        <!-- <hr> -->
        <!-- <div class="progress-info">用户记录信息</div>
        <div class="user-detail-extra">
            <div>开通时间：<span>2024/12/15 14:32:37 GMT+08:00</span></div>
            <div>姓名：{{ data.name }}</div>
            <div>认证信息：<span>在校学生</span></div>
            <div>联系地址：<span>中国湖北省武汉市洪山区湖北省武汉市武汉理工大学南湖校区 430070</span></div>
            <div>所背词书：<span>六级词书</span></div>
        </div> -->
        <hr>

        <div class="progress-info">用户学习信息</div>
        <div class="user-study-info user-detail-extra" v-if="studyData">
            <div>总共记忆的词汇：<span>{{ studyData.total_memorized_words }}</span></div>
            <div>单词平均熟练度：<span>{{ studyData.average_proficiency }}</span></div>
        </div>
        <div v-else>加载学习信息中...</div>




        <div class="close-btn-container">
            <!-- <div class="progress-info">关闭个人信息</div> -->
            <el-button type="primary" class="close-btn" @click="handleReturnButton">返回</el-button>
            <el-button type="warning" class="close-btn" @click="handleAdminButton">进入管理员界面</el-button>
            <el-button type="danger" class="close-btn" @click="handleLogoutButton">退出登录</el-button>
        </div>
        <el-dialog v-model="dialog" width="700" title="修改密码" draggable @close="dialogClose">
            <el-form label-width="100">
                <el-form-item label="手机号：">
                    <el-input v-model="data.name" placeholder="请填写手机号" disabled />
                </el-form-item>

                <el-form-item label="原密码：">
                    <el-input v-model="data.oldPassword" placeholder="请填写原密码" disabled />
                </el-form-item>

                <el-form-item label="新密码：">
                    <el-input v-model="data.newPassword" placeholder="请填写新密码" />
                </el-form-item>

                <el-form-item label="请确认：">
                    <el-input v-model="data.confirmPassword" placeholder="请再次填写新密码" />
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="add">确认</el-button>
                    <el-button @click="reset">取消</el-button>
                </el-form-item>
            </el-form>
        </el-dialog>
    </div>
</template>

<style scoped>
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.info-text {
    font-size: 1.5rem;
    color: #000;
}

.avatar-container {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.avatar-style {
    background-color: gray;
    border-radius: 50%;
    width: 200px;
    height: 200px;
}

.user-info {
    font-size: 1.5rem;
    color: #000;
    margin-top: 20px;
    /* margin-left: 20px; */
}

.user-detail,
.user-detail-extra {
    font-size: 1rem;
    color: #808080;
    margin-top: 20px;
}

.user-detail div,
.user-detail-extra div {
    margin-bottom: 10px;
}

hr {
    margin: 20px 0;
    border: none;
    border-top: 1px solid #ccc;
}

.progress-info {
    font-size: 1.5rem;
    color: #000;
}

.close-btn-container {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-top: 20px;
}

.close-btn {
    margin-left: 20px;
}

.reset-btn {
    margin-left: 10px;
    font-size: 1rem;
    padding: 5px 10px;
}

el-dialog {
    font-size: 1rem;
    color: #000;
}

el-form-item label {
    font-size: 1rem;
    color: #000;
}

el-input {
    width: 100%;
    font-size: 1rem;
    color: #000;
}
</style>